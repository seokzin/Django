from django.shortcuts import render
from .models import Question

def new(request):
    return render(request, )


def create(request):
    pass


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'board/index.html', context)


def detail(request, pk):
    return render(request, )


def edit(request, pk):
    return render(request, )


def update(request, pk):
    pass


def delete(request, pk):
    pass