from django.shortcuts import render,  get_object_or_404,redirect
from .models import Question, Choice
# Create your views here.
def home(request):
    
    first_question = Question.objects.order_by('id').first()
    return render(request, 'quiz/index.html', {
        'first_question': first_question
    })


def question_page(request, id):
    question = get_object_or_404(Question, id=id)

    next_question = Question.objects.filter(id__gt=id).order_by('id').first()

    # Initialize session ONCE
    if 'answers' not in request.session:
        request.session['answers'] = {}

    # 🔥 POST should be OUTSIDE
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')

        if not selected_choice_id:
            return render(request, 'quiz/question_base.html', {
                'question': question,
                'next_question': next_question,
                'error': 'Please select an option'
            })

        request.session['answers'][str(id)] = selected_choice_id
        request.session.modified = True

        if next_question:
            return redirect('question', id=next_question.id)
        else:
            return redirect('results')

    return render(request, 'quiz/question_base.html', {
        'question': question,
        'next_question': next_question
    })
def result_view(request):
    answers = request.session.get('answers', {})
    score = 0
    total = len(answers)

    for q_id, choice_id in answers.items():
        choice = Choice.objects.get(id=int(choice_id))
        if choice.is_correct:
            score += 1

    return render(request, 'quiz/results.html', {
        'score': score,
        'total': total
    })