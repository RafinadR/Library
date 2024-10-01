# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from authentication.models import CustomUser
from .models import Author
from .decorators import librarian_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import AuthorCreateForm, AuthorUpdateForm

@librarian_required
def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'author/all_authors.html', {
        'authors': authors
    })
    
@librarian_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.info(request, f"Author {author.name} is created successfully")
            return redirect('author:all_authors')    
    else:
        form = AuthorCreateForm()
    return render(request, 'author/author_create.html',{
        'form': form}
    )
    
@librarian_required
def author_delete(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if author.books.all().exists():
        messages.error(request, f"Sorry, the {author.name} has books and cannot be deleted.")
        return redirect('author:all_authors')
    messages.success(request, f"{author.name} deleted successfully.")
    author.delete()
    return redirect('author:all_authors')

@librarian_required
def author_by_id(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'author/view_user.html', {
        'author': author
    })
    

@librarian_required    
def author_update(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        form = AuthorUpdateForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author:all_authors')
    else:
        form = AuthorUpdateForm(instance=author)   
    return render(request, 'author/author_update.html', {
        'form': form,
        'author': author
    })
        