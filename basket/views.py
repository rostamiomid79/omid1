from django.shortcuts import render

from django.views.decorators.http import require_POST

@require_POST
def add_to_basket():

    response = HttoResponseRedirect(request.POST.get('next', '/'))
    basket_id = Basket.get_basket(request.COOKIES.get('basket_id', None))

    if basket is None:
        raise Http404

    response.set_cookie('basket_id', basket. id)



    if not basket.vaalidate_user(request.user):
        raise Http404

    form = AddToBasketForm(request.POST)
    if form.is_valid():
        form.save(basket=basket)
""""""
    product_id = request.POST.get('product_id', None)
    quantity = request.POST.get('quantity', 1)
    try:
        quantity = int(quantity)
    except:
        quantity = 1
    if product_id is not None:
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            pass
        else:
            basket.add(product, quantity)
""""""
    return response