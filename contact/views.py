from django.conf import settings
from django.shortcuts import render
from pymongo import MongoClient

from .forms import ContactForm


# Create your views here.


def contact(request):
    """A view to display and process the contact page"""

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            db = MongoClient(settings.MONGO_URI).get_database()
            questions = db.questions
            question = form.cleaned_data
            entry = questions.insert_one(question)

            return render(request, 'contact/thanks.html', {
                "entry_id": entry.inserted_id
            })
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {"form": form})


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
