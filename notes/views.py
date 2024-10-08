from django.shortcuts import render, redirect

from notes.forms import AddNoteForm
from notes.forms import RegisterForm
from notes.models import Note


def index(request):
    notes = Note.objects.all()
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                author=request.user, title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
            return redirect("index")
    else:
        form = AddNoteForm()
    return render(request, "index.html", {"notes": notes, "form": form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            # Например, создание пользователя
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


def home(request):
    return render(request, 'account/home.html')


def login_view(request):
    return render(request, 'account/login.html')
