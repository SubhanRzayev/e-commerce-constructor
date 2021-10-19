from django.db.models.query_utils import Q
from django.http import request
from django.views.generic.base import TemplateView
from core.models import HeaderImage
from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.views.generic import ListView,DetailView
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator



from product.models import *
# Create your views here.

PRODUCTS_PER_PAGE = 1
class ProductView(ListView):
    model= Product
    template_name = 'product-list.html'
    context_object_name = 'product_list'
    paginate_by = 1


    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        



        product = Product.get_all_products()
        page = self.request.GET.get('page',1)
        product_paginator = Paginator(product,PRODUCTS_PER_PAGE)
        try:
            product = product_paginator.page(page)
        except EmptyPage:
            product = product_paginator.page(product_paginator.num_pages)
        except:
            product = product_paginator.page(PRODUCTS_PER_PAGE)


        products = None
        priceId = self.request.GET.get('price')
       
             


        categoryId = self.request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            products =  Product.get_all_products()
        context["categories_list"] = Category.get_all_categories()
        context['category'] = Category.objects.filter(image__isnull = False)[3:8]
        context["product_list"] = products
        context['products'] = Product.get_all_products()
        context["brand_list"] =  BrandSlider.objects.all()
        context['header_list'] = HeaderImage.objects.all()
        context['product'] = product
        context['page_obj'] = product
        context['is_paginated'] = True
        context['paginator'] = product_paginator
        context['prices'] = Price.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'

    
    def get_success_url(self):
        return reverse("product:product_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = None
        categoryId = self.request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            products =  Product.get_all_products()
        
        context["categories_list"] = Category.get_all_categories()
        context['category'] = Category.objects.filter(image__isnull = False)[3:8]
        context["product_list"] = products
        context['products'] = Product.get_all_products()
        context["brand_list"] =  BrandSlider.objects.all()
        context['header_list'] = HeaderImage.objects.all()
        
        context["category_list"] = Category.objects.order_by('title')
        context["brand_list"] =  BrandSlider.objects.all()
        return context
    


    

    

    
    


