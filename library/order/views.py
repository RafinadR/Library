from django.shortcuts import render, redirect
from .models import Order
from book.models import Book
from authentication.models import CustomUser
from datetime import datetime, timedelta
from .decorators import librarian_required
from .forms import OrderForm


def create_order(request):
    books = Book.objects.all()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.created_at = datetime.now()
            order.plated_end_at = order.created_at + timedelta(weeks=2)
            order.save()
            return redirect("order:my_orders")
    else:
        form = OrderForm()
    return render(request, "order/create.html", {"form": form, "books": books})


@librarian_required
def close_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect("order:all_orders")


@librarian_required
def all_orders(request):
    orders = Order.get_all()
    return render(request, "order/all_orders.html", {"orders": orders})


def my_orders(request):
    user_orders = Order.objects.filter(user=request.user)
    print(user_orders)
    return render(
        request,
        "order/my_orders.html",
        {"user_orders": user_orders, "user": request.user},
    )
