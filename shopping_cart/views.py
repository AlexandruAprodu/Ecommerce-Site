from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from .models import Order, OrderItem, ShippingAddress
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import ShippingAddressForm
from django.contrib import messages
from users.models import Profile


def add_to_cart(request, **kwargs):
    # get the user profile
    # user_profile = get_object_or_404(User, user=request.user)
    # filter products by id
    product = Products.objects.filter(id=kwargs.get('item_id', "")).first()
    product2 = Products.objects.get(id=kwargs.get('item_id', ""))
    if product2.stock > 0:
        product2.stock -= 1
        product2.save()
    # create orderItem of the selected product
    order_item, _ = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, _ = Order.objects.get_or_create(owner=request.user, shipped=False)
    user_order.items.add(order_item)
    user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    url = request.GET.get('return_to')
    if not url:
        url = reverse('ecomm:index')
    return redirect(url)


def get_user_pending_order(request):
    # get order for the correct user
    # user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=request.user, shipped=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    else:
        return 0


def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/shopping_cart.html', context)


def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    product = Products.objects.get(id=item_id)
    product.stock += 1
    product.save()
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    url = request.GET.get('return_to')
    if not url:
        url = reverse('shopping_cart:order_details')
    return redirect(url)


def shipping_address(request):
    if request.method == 'POST':
        shipping_address_form = ShippingAddressForm(request.POST)
        if shipping_address_form.is_valid():

            shipping_address_model = shipping_address_form.save(commit=False)
            shipping_address_model.user_id = request.user.id
            shipping_address_model.save()
            return redirect(reverse('shopping_cart:checkout'))
        else:
            messages.error(request, 'Unul dintre campuri nu este valid !')
    else:
        shipping_address_form = ShippingAddressForm()
    return render(request, 'shopping_cart/shipping_address.html', {'shipp': shipping_address_form})


def checkout(request):
    if request.method == 'GET':
        context = {
            'address': ShippingAddress.objects.filter(user_id=request.user.id)[::-1][0],
        }
        return render(request, 'shopping_cart/checkout.html', context)

    elif request.method == 'POST':
        order = get_user_pending_order(request)

        if order == False:
            messages.error(request, 'Nu exista adresa de livrare !')
            return redirect(reverse('shopping_cart:shipping_address'))

        order.shipping_address_id = request.POST.get('shipping_address')
        order.shipped = True
        order.save()

        messages.success(request, 'Felicitari! Comanda ta va ajunge la tine in cel mai scurt timp posibil.')
        return redirect(reverse('ecomm:index'))

