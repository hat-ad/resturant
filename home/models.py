from django.db import models


product_type = [
  ("0", "Veg"),
  ("1", "Non-veg"),
]

product_category = [
  ("0", "Breakfast"),
  ("1", "Lunch"),
  ("2", "Snacks"),
  ("3", "Dinner"),
]

payment_method = [
    ("0", "Cash"),
    ("1", "Card"),
    ("2", "UPI")
]


class Table(models.Model):
    table_no = models.IntegerField(verbose_name='Table number', unique=True, default=0)
    seat = models.IntegerField(verbose_name='Number of seats', default=4)
    fill = models.IntegerField(verbose_name='Fill', default=0)

    class Meta:
        ordering = ['table_no',]

    def _str_(self):
        return 'Table no '+str(self.table_no)

    @property
    def is_free(self):
        if self.fill > 0:
            return False
        return True


class Waiter(models.Model):
    name = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ['name',]

    def _str_(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='product_image/')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=product_type)
    category = models.CharField(max_length=1, choices=product_category)
    price = models.FloatField(default=0.0)

    def _str_(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    def _str_(self):
        return self.email


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    total = models.FloatField(default=0.0)
    peoples = models.IntegerField(default=1)
    table_no = models.ForeignKey(Table, on_delete=models.PROTECT, null=True)
    payment_method = models.CharField(choices=payment_method, default='0', max_length=1, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.PROTECT, null=True)

    def get_order_items(self):
        return OrderItems.objects.filter(order=self)

    @property
    def cus_name(self):
        if self.customer == None:
            return 'Order Pending'
        return self.customer.name


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)


class PromoCode(models.Model):
    code = models.CharField(max_length=8, default='')
    discount = models.IntegerField(verbose_name='Discount (%)', default=0)