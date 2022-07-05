from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Session

class Session_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

# class Account_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = '__all__'
#
# class User_Serializer(serializers.ModelSerializer):
#     isAdmin = serializers.SerializerMethodField(read_only=True)
#     account = Account_Serializer()
#     authnetID = serializers.CharField(source='account.authnetID')
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'isAdmin', 'account', 'authnetID']
#     def get_isAdmin(self, obj):
#         return obj.is_staff
#
# class User_Serializer_With_Token(User_Serializer):
#     token = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'token', 'authnetID']
#
#     def get_token(self, obj):
#         token = RefreshToken.for_user(obj)
#         return str(token.access_token)
#
#
# class Stripe_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stripe
#         fields = '__all__'
#
# class Store_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = '__all__'
#
# class Review_Serializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Review
#         fields = '__all__'
#
#     def get_user(self, obj):
#         user = obj.user
#         serialized_user = User_Serializer(user, many=False)
#         return serialized_user.data
#
# class Product_Serializer(serializers.ModelSerializer):
#     reviews = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     def get_reviews(self, obj):
#         all_reviews = obj.review_set.all()
#         serialized_reviews = Review_Serializer(all_reviews, many=True)
#         return serialized_reviews.data
#
# class Content_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Content
#         fields = '__all__'
#
# class Collage_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Collage
#         fields = '__all__'
#
# class Coupon_Serializer(serializers.ModelSerializer):
#     storeName = serializers.ReadOnlyField(source='store.name')
#     class Meta:
#         model = Coupon
#         fields = ( 'id', 'user', 'store', 'storeName', 'code', 'discount', 'expiry', 'description', 'createdAt' )
#
# class Address_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = '__all__'
#
# class Order_Address_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderAddress
#         fields = '__all__'
#
# class Order_Item_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = '__all__'
#
# class Order_Serializer(serializers.ModelSerializer):
#     orderItems = serializers.SerializerMethodField(read_only=True)
#     deliveryAddress = serializers.SerializerMethodField(read_only=True)
#     user = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Order
#         fields = '__all__'
#
#     def get_orderItems(self, obj):
#         items = obj.orderitem_set.all()
#         serializer = Order_Item_Serializer(items, many=True)
#         return serializer.data
#
#     def get_deliveryAddress(self, obj):
#         try:
#             address = Order_Address_Serializer(obj.deliveryaddress, many=False).data
#         except:
#             address = False
#         return address
#
#     def get_user(self, obj):
#         user = obj.user
#         serializer = User_Serializer(user, many=False)
#         return serializer.data
