from django.shortcuts import render, redirect

from .forms import BookCreateForm, BookUpdateForm
from .models import Book

# Create your views here.


def book_create(request):
    form = BookCreateForm()
    books = Book.objects.all()

    context = {
        "form":form,
        "books":books,
    }

    template_name = "book/create.html"

    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            context = {
                "form":form,
            }
            return render(request, template_name, context)
    return render(request, template_name, context)


def view_book(request, id):
    book = Book.objects.get(id=id)
    context = {
        "book": book,
    }
    return render(request, 'book/view.html', context)


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookUpdateForm(instance=book)
    context = {
        "form": form
    }
    if request.method == 'POST':
        form = BookUpdateForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            form = BookUpdateForm(request.POST, instance=book)
            context = {
                "form": form,
            }
            return render(request, 'book/edit.html', context)

    return render(request, 'book/edit.html', context)

def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect("create")