from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods
from django.db.models import Q
from django.http import HttpResponse
from catalogue.models import Product, Category, ProductType, Brand

def products_list(request):
    context = dict()

    context['products'] = Products.objects.select_related('category').all()

    #context = "\n".join([f"{product.title}, {product.upc}, {product.category.name}" for product in products])
   # return HttpResponse(context)
     return render(request, 'category/product_list.html', context=context)


def product_detail(request, pk):

    queryset = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(pk=upc))
    if queryset.exists():
        product = queryset.first()
  #      return HttpResponse(f"title:{product.title}")
  #  return HttpResponse("product does not exist")
        product = AddToBasketForm({"product" : product.id, 'quantity' : 1})
        return render(request, 'category/product_detail.html', {"product":product, "form":form})
    raise Http404


def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse("category does not exist")
    products = category.products.all()
    product_ids = [1, 2, 3]
    products = Products.objects.filter(id__in=product_ids)

    context = "\n".join([f"{product.title},{product.upc}" for product in products])
    return HttpResponse(context)





def products_search(request):
    title = request.GET.get('q')
    products = Product.objects.filter(
        is_active=True, title__icontains=title,
        category__name__icontains=title, category__is_active=True
    )
    products = Products.objects.filter(is_active=True).filter(
        title__icontains=title
    ).filter(category__name__icontains=title).filter(category__is_active=True).distinct()
    context = "\n".join([f"{product.title},{product.upc}" for product in products])
    return HttpResponse(f"search page:\n{context}")



@login_required(login_url='/admin/login/')
@require_http_methods(request_method_list=['GET','POST'])
def user_profile(request):
    return HttpResponse(f"Hello {request.user.username}")

@login_required
def wallet(request):
    pass
