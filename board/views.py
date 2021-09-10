from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Question
from .forms import QuestionForm

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()  
            return redirect('board:detail', question.pk)
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'board/form.html', context)


@require_http_methods(['GET', 'SAFE'])
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {'questions': questions,}
    return render(request, 'board/index.html', context)


@require_safe
def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    context = {'question': question,}
    return render(request, 'board/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()              
            return redirect('board:detail', question.pk)
    else:
        form = QuestionForm(instance=question)
    
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'board/form.html', context)


@require_POST
def delete(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    question.delete()
    return redirect('board:index')
