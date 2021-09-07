from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Question
from .forms import QuestionForm

@require_http_methods(['GET', 'POST'])
def create(request):
    # 5. 사용자가 데이터를 입력 & POST /board/create/ => invalid data
    # 10. 사용자가 데이터를 입력 & POST /board/create/ => valid data
    if request.method == 'POST':
        # 6. 데이터를 검증할 QuestionForm 인스턴스 초기화 => 내용 있음
        # 11. 데이터를 검증할 QuestionForm 인스턴스 초기화 => 내용 있음
        form = QuestionForm(request.POST)
        # 7. 검증 => 실패
        # 12. 검증 => 성공
        if form.is_valid():
            # 13. form 을 통해 데이터 저장
            question = form.save()  
            # 14. /board/<pk>/ 로 redirect 하도록 응답
            return redirect('questions:detail', question.pk)
    # 1. GET /board/create/ => 빈 form 요청
    else:
        # 2. 비어있는 QuestionForm 인스턴스를 초기화 => 빈 form 생성
        form = QuestionForm()

    # 3. 빈 form 을 context에 담음
    # 8. 에러 메시지를 담은 form을 context에 담음
    context = {'form': form}

    # 4. 사용자에게 빈 form 제공
    # 9. 에러 미시지를 포함한 form 제공
    return render(request, 'board/form.html', context)


@require_http_methods(['GET', 'SAFE'])
def index(request):
    # pk 내림차순 정렬
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
            return redirect('questions:detail', question.pk)
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
    return redirect('questions:index')
