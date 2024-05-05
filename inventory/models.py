from django.db import models
from cloudinary.models import CloudinaryField

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = CloudinaryField('image') 
    stock = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

class SaleModel(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.FloatField()
    user_id = models.ForeignKey('User',on_delete=models.CASCADE)

    class Meta:
        db_table = 'sales'

class SaleDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    subtotal = models.FloatField()
    products_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    sale_id = models.ForeignKey(SaleModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sale_details'