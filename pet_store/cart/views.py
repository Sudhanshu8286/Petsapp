from django.http import JsonResponse
from django.shortcuts import render,redirect
from petsapp.models import Pet
from .models import Cart
from django.contrib import messages
from django.db.models import Sum

# Create your views here.



def add_to_cart(request,id):
    cart_id = request.session.session_key
    if cart_id == None:
        cart_id = request.session.create()

    pet = Pet.objects.get(id=id)
    price = pet.price
    user = request.user

    Cart(cart_id=cart_id,pet=pet,user=user,totalprice=price).save()
    messages.success(request,"Item Added to Cart Successfully")
    return redirect('/')


def cart_name(request):
    all_items = Cart.objects.filter(user=request.user)
    flag = all_items.exists()
    return render(request,'cart/cart_home.html',{'items':all_items,'flag':flag})


def delete_cart_product(request,id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    messages.success(request,"Item Removed From Cart Successfully")
    return redirect('cartpage')



def update_cart(request,id):
    p = request.POST.get('price')
    q = request.POST.get('qnt')
    p_id = request.POST.get('id')
    totalPrice = float(p) * int(q)
    Cart.objects.filter(id=p_id).update(quantity=q,totalprice=totalPrice)
   # total = Cart.objects.filter(user=request.user).aggregate(totalprice = Sum(F('totalprice') * F('quantity')))
    total_amount = Cart.objects.filter(user=request.user).aggregate(total=Sum ('totalprice'))['total'] or 0.0 
    return JsonResponse({'status':True,'totalprice':totalPrice,
    'total_amount':total_amount,})

