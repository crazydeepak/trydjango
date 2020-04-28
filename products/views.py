from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm, RawProductForm
from .models import Product


# Create your views here.


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    #     context={
    # 'title':obj.title,
    # 'desc':obj.description
    #     }
    context = {'object': obj}
    return render(request, "products/product_detail.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context={'form':my_form}
#     return render(request,"products/product_create.html",context)

# def product_create_view(request):
#     #print(request.GET)
#     #print(request.POST['q'])
#     if request.method == 'POST':
#         my_new_title=request.POST.get('title')
#         print("----------" + my_new_title+ "-----------")
#     #Product.objects.create('stitle'=my_new_title)
#     context={}
#     return render(request,"products/product_create.html",context)

def product_create_view(request):
    initial_data = {
        "title": "This is my default title"

    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,
                       initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {'form': form}
    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, my_id):
    # obj=Product.objects.get(id=my_id)
    # obj=get_object_or_404(Product,id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {"object": obj}
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()  # confirming delete
        print("----Deleting----")
        return redirect("../../")
    context = {"object": obj}
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    query_set = Product.objects.all()
    context = {"object_set": query_set}
    return render(request, "products/product_list.html", context)
