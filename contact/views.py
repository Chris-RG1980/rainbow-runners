from django.conf import settings
from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse


# Create your views here.


def contact(request):
    """A view to display and process the contact page"""

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')

        if not (name and email and question):
            return HttpResponse("All fields are required.", status=400)

        db = MongoClient(settings.MONGO_URI).get_database()
        questions = db.questions
        question_document = {
            "name": name,
            "email": email,
            "question": question,
            "answered": False
        }
        entry = questions.insert_one(question_document)

        return render(request, 'contact/thanks.html', {
            "entry_id": entry.inserted_id
        })
    else:
        return render(request, 'contact/contact.html')


def view_questions(request):
    """A view to display submitted questions for admins"""
    db = MongoClient(settings.MONGO_URI).get_database()
    questions = db.questions
    all_questions = list(questions.find())

    questions_for_template = []
    for question in all_questions:
        question_data = {
            'id': str(question['_id']),
            'name': question.get('name', 'No name provided'),
            'email': question.get('email', 'No email provided'),
            'question': question.get('question', 'No question provided'),
            'answered': question.get('answered', False)
        }
        questions_for_template.append(question_data)

    return render(request, 'contact/view_questions.html', {
        'questions': questions_for_template
    })
