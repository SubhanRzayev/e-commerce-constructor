from django.views.generic.base import TemplateView
from core.models import Contact, HeaderImage
from django.shortcuts import render
from core.forms import ContactForm
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from product.models import *

# Create your views here.


# def home(request):
#     return render(request,'index.html')


class SearchView(TemplateView):
    model = Product
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search',"")
        context["product_list"] = Product.objects.filter(title__icontains = search)
        return context


class IndexView(ListView):
    template_name = 'index.html'
    success_url = reverse_lazy('core:index')

    def get_queryset(self):
        return Product.objects.order_by('title')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = None
        categoryId = self.request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            products =  Product.get_all_products()
        context["categories_list"] = Category.get_all_categories()
        context['category'] = Category.objects.filter(image__isnull = False)[3:7]
        context["product_list"] = products
        context['products'] = Product.get_all_products()
        context['production'] = Product.objects.filter(is_published=True).order_by('created_at')[4:10]
        context["brand_list"] =  BrandSlider.objects.all()
        context['header_list'] = HeaderImage.objects.all()
        return context
    




class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('core:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        context =  super().form_valid(form)
        form.save()
        return context



    
