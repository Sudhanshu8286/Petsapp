from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm
from .models import Orders
from cart.models import Cart
from datetime import date, datetime
import uuid

# Create your views here.

def place_order(request):
    form = OrderForm()
    current_user = request.user
    cart_items = Cart.objects.filter(user=current_user)
    cart_items_count = cart_items.count()
    total_amount = request.GET.get('totalamount',0.0) #Get the totalamount
    if cart_items_count <=0:
        return redirect('pets_list')
    if request.method == "POST":
        form = OrderForm(request.POST)
        data = Orders()
        if form.is_valid():
            data.user = request.user
            data.first_name = form.cleaned_data.get('first_name')
            data.last_name = form.cleaned_data.get('last_name')
            data.phone = form.cleaned_data.get('phone')
            data.email = form.cleaned_data.get('email')
            data.address = form.cleaned_data.get('address')
            data.country = form.cleaned_data.get('country')
            data.state = form.cleaned_data.get('state')
            data.city = form.cleaned_data.get('city')
            data.total = total_amount
            data.ip = request.META.get('REMOTE_ADDR')
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            unique_id = str(uuid.uuid4().fields[-1])[:5]
            orderNumber = f'ORD-{timestamp}.{unique_id}'
            data.order_number = orderNumber
            data.save()
            return HttpResponse("data inserted")
           
    return render(request,'orders/billing_page.html',{'form':form,'total':total_amount})
      
                            