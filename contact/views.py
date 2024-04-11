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
        question = {"name": name, "email": email, "question": question}
        entry = questions.insert_one(question)

        return render(request, 'contact/thanks.html', {
            "entry_id": entry.inserted_id
        })
    else:
        return render(request, 'contact/contact.html')
