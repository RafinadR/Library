from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from author.models import Author
from .decorators import librarian_required
from order.models import Order
from authentication.models import CustomUser


def all_books(request):
    books = Book.objects.all()

    author_name = request.GET.get("author")
    title = request.GET.get("title")
    user_id = request.GET.get("user_id")
    if user_id:
        return redirect("book:user_books", user_id=user_id)
    if author_name:
        books = books.filter(authors__name__icontains=author_name)

    if title:
        books = books.filter(name__icontains=title)

    return render(request, "book/all_books.html", {"books": books})


def add(request):
    authors = Author.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            selected_authors = request.POST.getlist("authors")
            for author_id in selected_authors:
                author = Author.objects.get(pk=author_id)
                book.authors.add(author)

            new_author_name = request.POST.get("new_author")
            if new_author_name:
                name, patronymic, surname = new_author_name.split(" ")
                new_author = Author.create(
                    name=name, patronymic=patronymic, surname=surname
                )
                new_author.save()
                book.authors.add(new_author)
            book.save()
            return redirect("book:all_books")
    else:
        form = BookForm()

    return render(request, "book/add.html", {"form": form, "authors": authors})


def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "book/view_book.html", {"book": book})


@librarian_required
def user_books(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    orders = Order.objects.filter(user_id=user_id)

    book_ids = [order.book_id for order in orders]
    books = Book.objects.filter(id__in=book_ids)

    return render(request, "book/user_books.html", {"user": user, "books": books})


@librarian_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book:all_books")

    return render(request, "book/delete_book.html", {"book": book})