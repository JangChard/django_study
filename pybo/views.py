from django.shortcuts import render, get_object_or_404
from .models import Question
#from pybo.models import Question, Answer

# # Create your views here.
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")


def index(request):
    '''
    pybo  목록 출력
    '''
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}    
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """    
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)