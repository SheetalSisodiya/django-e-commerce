from django.db import models
from django.contrib.auth.models import User



STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujrat', 'Gujrat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhan', 'Jharkhan'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Maharashtra', 'Maharashtra'),
    ('Madhaya Pradesh', 'Madhaya Pradesh'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Tripura', 'Tripura'),
    ('Telangana', 'Telangana'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman & Nicobar (UT)', 'Andaman & Nicobar (UT)'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra & Nagar Haveli and Daman & Diu (UT)', 'Dadra & Nagar Haveli and Daman & Diu (UT)'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField( max_length=200)
    city = models.CharField( max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def _str_(self):
        return self.name




CATEGORY_CHOICES = (
    ('C',"Camera"),
    ('M',"Men's Fasion"),
    ('W',"Women's Fasion"),
    ('S',"Sunglasses"),
    ('Sh',"Shoes"),
)



class Product(models.Model):
    product_name = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    brand = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product-img')

    def _str_(self):
        return self.product_name

class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return str(self.pk)
    
STATUS_CHOICES= (
    ('Accepted', 'Accepted'),
    ('ON the way', 'ON the way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)

class OrderPlaces(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    carts = models.ForeignKey(Carts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending...')

    def _str_(self):
        return self.product





    #  def__str__(self):
    #     return str(self.id)




