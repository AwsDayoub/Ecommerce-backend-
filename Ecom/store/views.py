from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser , FormParser ,  FileUploadParser
from rest_framework import status , generics
from django.http import HttpResponse
from .models import *
from .serializer import *
from users.models import User
# Create your views here.

class ProductView(APIView):

    serializer_class = ProductWithImageSerializer

    def get(self, request):
        queryset = Product.objects.all()

        serializer = ProductWithImageSerializer(queryset, many=True, context={"request":request})
        user_info = {}
        if request.user.is_authenticated:
            user = User.objects.filter(username=request.user.username)
            user_info['is_authenticated'] = 1
            user_info['status'] = user.status
            user_info['id'] = user.id
        else:
            user_info['is_authenticated'] = 0
        return Response({'data': serializer.data , 'user_info': user_info} , status=status.HTTP_200_OK)



class AddProductWithImage(APIView):

    parser_classes = [ MultiPartParser ]

    def post(self , request):
        print(request.data)
        print()
        print(request.FILES)
        name = request.data['namee']
        price = request.data['price']
        image = request.FILES['image']
        product = Product.objects.create(namee=name, price=price, image=image)
        return HttpResponse('product successfuly added', status=status.HTTP_200_OK)

'''
    def post(self , request):
        serializer = ProductWithImageSerializer(data=request.data)
        print('Your Data: ' , request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            price = serializer.validated_data['price']
            image = request.FILES['image']
            product = Product.objects.create(namee=name, price=price, image=image)
            return Response(self.serializer_class(product).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class AddProduct(APIView):
    serializer_class = ProductSerializer
    def post(self , request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('product successfuly added', status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
        


class AddProductImage(APIView):

    parser_classes = [ MultiPartParser ]

    def put(self , request ): 
        product = Product.objects.last()
        '''
        serializer = AddImageProSerializer(data=request.data , instance = product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        '''
        serializer = AddImageProSerializer(data=request.data , instance = product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderItemView(generics.ListCreateAPIView):

    serializer_class = OrderItemSerializer
    
    def get(self, request):
        if Order.objects.last() == None:
            last_id = 0
        else:
            last_id = (Order.objects.last()).id + 1
        dict = [ {'new_id': last_id}]
        return Response(dict)

    def post(self, request):
        
        user = User.objects.get(username=request.data[len(request.data) - 1]['username'])
        order = Order.objects.create(complete=False, transaction_id='xxx' , user=user)
        data = request.data
        i = 0
        while i < len(data):
            if 'username' in data[i].keys():
                data.pop(i)
            else:
                i += 1
        fdata = []
        for i in range(len(data)):
            obj = {}
            for key in data[i]:
                if key == 'quantity' or key == 'product' or key == 'order':
                    obj[key] = data[i][key]
            fdata.append(obj)
        serializer = self.get_serializer(data=fdata, many=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    def get(self , request):
        orders = Order.objects.all().order_by('date_orderd')
        data = []
        for order in orders:
            ob = {}
            ob['order_num'] = order.id
            ob['customer_name'] = order.user.name
            ob['customer_address'] = order.user.address
            ob['cost'] = order.get_cart_total
            ob['complete'] = order.complete
            data.append(ob)
        #serializer = OrderSerializer(orders, many=True, context={"request":request})
        return Response(data, status=status.HTTP_200_OK)