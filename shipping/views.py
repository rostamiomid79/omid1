from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods, require_GET
from shipping.forms import ShippingAddressForm
from shipping.models import ShippingAddress
from django.views.generic import ListView
@login_required
@requie_get
def address_list():
    queryset = ShippingAddress.objects.filter(user=request.user)
    return render(request, 'shippng/list.html/', {'queryset' : queryset})

class CustomerListView(ListView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class AddressListView(CustomerListView):
    model = ShippingAddress
   #template_name = 'shipping/list.html'
    def get_context_data(self, *args, object_list = None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['extra_data'] = self.get_queryset().count()
        return context
    @method_decorator(login_required)
    def get(self, request):
        queryset = ShippingAddress.objects.filter(user=request.user)
        return render(request, 'shippng/list.html/', {'queryset': queryset})


@login_required
@require_http_methods(request_method_list=['GET', 'POST'])
def address_create(request):
    if request.method == "POST":
        # validate and save form data
        form = ShippingAddressForm(request.Form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('address-list')
    # render form
    else:
        form = ShippingAddreeForm()
    return render(request, 'shipping/create.html', {'form' : form})

class AddressCreateView(FormView):
    form_class = ShippingAddressForm
    template_name = 'shipping/create.html'
    success_url = '/shipping/list/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return super().from_valid(form)