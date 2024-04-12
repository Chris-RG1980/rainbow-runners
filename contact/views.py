from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pymongo import MongoClient

from .forms import ContactForm


# Create your views here.

def is_in_group(user, group_name):
    """Check if the user is in the given group."""
    return user.groups.filter(name=group_name).exists()


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


@login_required
def view_questions(request):
    """A view to display submitted questions for admins"""

    is_admin = is_in_group(request.user, 'admin')

    if is_admin:
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
    else:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('contact_us')
