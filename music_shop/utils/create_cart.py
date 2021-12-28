def create_cart(request):
    from musicshop.models import Cart, Customer

    customer = Customer.objects.get(user=request.user)
    customer_cart = customer.cart_set.filter(in_order=False).first()
    if customer_cart:
        customer_cart.delete()
    cart = Cart.objects.get(id=request.session['cart_id'])
    cart.session_key = None
    cart.owner = customer
    cart.products.update(user=cart.owner, session_key=None)
    cart.save()
    del request.session['cart_id']
