from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Service(models.Model):
    ser_desc=models.CharField(max_length=255,unique=True)
    ser_type=models.SmallIntegerField(default=0)
   

    def __str__(self):
        return self.ser_desc+" - "+str(self.ser_type)

class BigService(models.Model):
    ser_name=models.CharField(max_length=255,blank=True, null=True)
    ser_type=models.CharField(max_length=50,blank=True, null=True)
    ser_number=models.IntegerField(blank=True, null=True)
    service_desc=models.ForeignKey(Service,on_delete=models.CASCADE,null=True,blank=True,related_name="servsbi_type")
    price=models.FloatField(default=0.0)
    Condition=models.SmallIntegerField(default=1)
    def __str__(self):
        return str(self.service_desc)



class SmallService(models.Model):
    ser_name=models.CharField(max_length=255,blank=True, null=True)
    ser_number=models.IntegerField(blank=True, null=True)
    service_desc=models.ForeignKey(Service,on_delete=models.CASCADE,null=True,blank=True,related_name="servsma_type")
    price=models.FloatField(default=0.0)
    Condition=models.SmallIntegerField(default=1)
    def __str__(self):
        return str(self.service_desc)

#Display All service to choose




class Organzition(models.Model):
    name=models.CharField(max_length=50)



class Customer(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=255,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    email=models.TextField(null=True,blank=True)
    organzition_id=models.ForeignKey(Organzition,on_delete=models.CASCADE,null=True,blank=True,related_name="cus_org")

    def __str__(self):
        return self.name


#Generate a unique Bill for Integration service with signle Bill request
class CustomerBill(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="bill_user")
    cusotmer_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True,related_name="bill_cust")
    bill_date=models.DateField(auto_now=True)
    bill_number=models.IntegerField()
    bill_type=models.IntegerField()
    total_price=models.FloatField(default=0.0)

    
    def __str__(self):
        return str(self.cusotmer_id)+" - "+str(self.total_price) 


#bill details for every product in bill
class ServiceBookDetails(models.Model):
    customer_bill_id=models.ForeignKey(CustomerBill,on_delete=models.CASCADE,null=True,blank=True,related_name="book_bill_Customer")
    big_service=models.ForeignKey(BigService,on_delete=models.CASCADE,null=True,blank=True,related_name="serv_bigserv")
    small_service=models.ForeignKey(SmallService,on_delete=models.CASCADE,null=True,blank=True,related_name="serv_smallserv")



#bill general detail for transportation purpose
class BookService(models.Model):
    customer_bill_id=models.ForeignKey(CustomerBill,on_delete=models.CASCADE,null=True,blank=True,related_name="book_bill")
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="book_user")
    organzition_id=models.ForeignKey(Organzition,on_delete=models.CASCADE,null=True,blank=True,related_name="book_org")
    book_date=models.DateField(blank=True,null=True)
    travel_date=models.DateField(blank=True,null=True)
    arrival_date=models.DateField(blank=True,null=True)
    internal_travel_date=models.DateField(blank=True,null=True)
    internal_arrival_date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.customer_bill_id+"-"+str(self.book_date) 


class Notification(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="notif_user")
    service_id=models.ForeignKey(BookService,on_delete=models.CASCADE,null=True,blank=True,related_name="notif_serv")
    message=models.TextField()
    Notification_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.service_id+"-"+self.message 
    

    

