
from django.db.models import fields
from django.db.models.fields.related import ManyToManyField
from rest_framework import serializers
from ..models import Service,Customer,Organzition,Notification,BigService, SmallService,CustomerBill,ServiceBookDetails,BookService
from django.contrib.auth.models import Group,Permission,User
import json
class UserSerlizer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        exclude=["last_login","last_name","date_joined"]

class UserSerlizerEd(serializers.ModelSerializer):
    
    class Meta:
        model=User
        exclude=["last_login","last_name","date_joined","password"]

class GroupSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="__all__"

class PermissionSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields="__all__"  

class ServiceSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields="__all__"
    

class CustomerSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"


class OrganzitionSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Organzition
        fields="__all__"


class NotificationSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields="__all__"

class BigServiceSerlizer(serializers.ModelSerializer):
    class Meta:
        model=BigService
        fields="__all__"



class SmallServiceSerlizer(serializers.ModelSerializer):
    class Meta:
        model=SmallService
        fields="__all__"


class CustomerBillSerlizer(serializers.ModelSerializer):
    Customer=serializers.SerializerMethodField()
    Services=serializers.SerializerMethodField()
    Servicelist=serializers.SerializerMethodField()
    Servicelistname=serializers.SerializerMethodField()
    user=serializers.SerializerMethodField()
    def get_Customer(self, instance):
        return instance.cusotmer_id.name
    def get_Services(self, instance):
        Service=ServiceBookDetails.objects.filter(customer_bill_id=instance.id)
        return Service.count()
    def get_Servicelist(self, instance):
        Services=ServiceBookDetails.objects.filter(customer_bill_id=instance.id).values()
        return  Services
    def get_Servicelistname(self, instance):
            Services=self.get_Servicelist(instance);
            ServicesResult=[];
            for i in Services:
                if i['big_service_id'] is not None:
                    ServicesResult.append(BigService.objects.filter(id=i['big_service_id']).values())
                else:
                    ServicesResult.append(SmallService.objects.filter(id=i['small_service_id']).values())
            return ServicesResult
    def get_user(self, instance):
        if instance.user_id:
            user=User.objects.get(username=instance.user_id)
            return user.first_name
     
    class Meta:
        model=CustomerBill
        fields="__all__"

class ServiceBookDetailsSerlizer(serializers.ModelSerializer):
    Service=serializers.SerializerMethodField(read_only=True)
    Customer=serializers.SerializerMethodField()
    Price=serializers.SerializerMethodField()
    TotalPrice=serializers.SerializerMethodField()
    BillType=serializers.SerializerMethodField()
    BillDate=serializers.SerializerMethodField()
    class Meta:
        model=ServiceBookDetails
        fields="__all__"
    def get_Service(self, instance):
        if instance.big_service:
            return instance.big_service.service_desc.ser_desc
        elif instance.small_service:
            return instance.small_service.service_desc.ser_desc

    def get_Price(self, instance):
        if instance.big_service:
            return instance.big_service.price
        elif instance.small_service:
            return instance.small_service.price

    def get_Customer(self, instance):
        return instance.customer_bill_id.cusotmer_id.name
    def get_TotalPrice(self, instance):
        return instance.customer_bill_id.total_price
    def get_BillType(self, instance):
        return instance.customer_bill_id.bill_type
    def get_BillDate(self, instance):
        return instance.customer_bill_id.bill_date

        

class BookServiceSerlizer(serializers.ModelSerializer):
    
    class Meta:
        model=BookService
        fields="__all__"