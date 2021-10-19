from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone


# Create your models here

class Product(models.Model):
    """
    relation
    """
    category = models.ForeignKey('Category',db_index=True,blank=True,null=True,related_name='product_category',on_delete=models.CASCADE)
    prices = models.ManyToManyField('Price',db_index=True,blank=True,related_name='product_prices')
    sizes = models.ManyToManyField('Size',db_index=True,blank=True,related_name='product_size')
    colors = models.ManyToManyField('Color',db_index=True,blank=True,related_name='product_color')
    

    title = models.CharField(max_length=50)
    price = models.DecimalField(default=0.00,max_digits=7,decimal_places=2)
    discount_price = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,blank=True,null=True)
    description = models.TextField(max_length=1000)
    quantity = models.PositiveIntegerField(default=1,null=True,blank=True)
    sale = models.IntegerField(default=0, blank=True, null=True)
    stock = models.BooleanField(default=False,)
    digital = models.BooleanField(default=False,null=True, blank=True)
    products_image = models.ImageField(upload_to = 'productimg')
    is_published = models.BooleanField(default=False, blank=True)

    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(self.id)


    def get_absolute_url(self):
        return reverse_lazy("product:product_detail", kwargs={
            "pk": self.pk
            })

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @property
    def new_price(self):
        if self.discount_price:
            return self.discount_price
        elif self.discount_price == 0 and self.sale != 0:
            return self.price * (100 - self.sale) // 100
        elif self.discount_price == 0 and self.sale ==0:
            return self.price * self.quantity
        else:
            return self.price


    @property
    def get_total(self):
        if self.discount_price:
            total =  self.price * self.quantity
            return total
        elif self.discount_price == 0 and self.sale !=0:
            x =  self.price * (100 - self.sale)//100
            return x * self.quantity
        elif self.discount_price == 0 and self.sale == 0:
            total = self.price * self.quantity
            return total
        else:
            total = self.discount_price * self.quantity
            return total
    



        






class Category(models.Model):

    category = models.ForeignKey('self',db_index=True,blank=True,null=True,related_name='categories',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50,default='fa fa-female')
    image = models.ImageField(upload_to = 'category_image',default = 'category.jpg')
    description = models.TextField(max_length=400,default="Some text")
    is_published = models.BooleanField(default=False,blank=True)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        if self.category:
            return f"{self.category.title} > {self.title}"
        return self.title

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')


class Color(models.Model):
    color = models.CharField(max_length=50,blank=True,null=True)
    is_published = models.BooleanField(default = False,blank=True)

    def __str__(self):
        return self.color

    
class Size(models.Model):
    size = models.CharField(max_length=50,blank=True,null=True)
    is_published = models.BooleanField(default = False,blank=True)

    def __str__(self):
        return self.size


class Image(models.Model):
    category = models.ForeignKey('Category',db_index=True,on_delete=models.CASCADE, related_name='category_image', null=True,blank=True,    )
    product = models.ForeignKey('Product',db_index=True,on_delete=models.CASCADE,null=True,blank=True,related_name='product_image')
    image = models.ImageField(upload_to = 'product_image',default = 'IMG.JPG')

    def __str__(self):
        return str(self.image)



class Price(models.Model):
    """
    Price model's save all products price range. 
    Ex: 0.00$ - 50.0$ , 50.00$ - 100.0$, 100.00$ - 150.0$ ...
    """
    #information
    price = models.CharField(max_length=50, default='0.00$ - 50.00$')

    is_published = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.price 



class BrandSlider(models.Model):
    image = models.ImageField(upload_to = 'brand_slider_image')
    


# 
# class SortBy(models.Model):
#     """
#     SortBy model's sorted by products to their categories.
#     Ex: Default, Accessoires, Bags, Chair...
#     """
#     #information
#     sortby = models.CharField(max_length=70,blank=True)

#     def __str__(self):
#         return self.sortby

#     class Meta:
#         verbose_name = 'SortBy'
#         verbose_name_plural = 'SortsBy'


