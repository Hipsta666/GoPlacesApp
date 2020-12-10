from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import *


class QuizView(View):
    def get(self, request):
        questions = Question.objects.all()
        poll = dict()

        for question in questions:
            answers = [answer.answer_text for answer in Answer.objects.filter(questions=question.id)]
            poll[question.question_text] = answers

        return render(request, 'goplaces/quiz-form.html', {'questions': poll})


class OffersView(View):
    def post(self, request):
        result = request.POST.dict()
        result.pop('csrfmiddlewaretoken')

        request.session['addrFrom'] = result.get('addrFrom')
        request.session['method'] = result.get('method')

        r = list(result.values())
        places = Place.objects.filter(tags__title__in=r)

        return render(request, 'goplaces/offers.html', {'places': places})


class OfferDetailView(View):
    def post(self, request, slug):
        address_from = request.session['addrFrom']
        method = request.session['method']
        place = Place.objects.get(url=slug)
        print(address_from)

        return render(request, 'goplaces/view.html', {'place': place,
                                                      'address_from': address_from,
                                                      'method': method})

