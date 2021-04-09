from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from .forms import QuestboardForm, QuestcardForm, QuestcardForm_


class main(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questboards'] = Questboard.objects.all()
        return context


class questboard(TemplateView):
    template_name = 'questboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['questboard_id']
        context['questboard'] = Questboard.objects.get(
            id=pk).questcard_set.all()
        context['qbid'] = pk
        return context


def addPerson(request, questcard_id, questboard_id):
    questcard = Questcard.objects.get(id=questcard_id)
    if questcard.person1 is None:
        questcard.person1 = request.GET['person']
        questcard.save()
        return redirect('/questboard/' + str(questboard_id))
    elif questcard.person2 is None:
        questcard.person2 = request.GET['person']
        questcard.save()
        return redirect('/questboard/' + str(questboard_id))
    elif questcard.person3 is None:
        questcard.person3 = request.GET['person']
        questcard.save()
        return redirect('/questboard/' + str(questboard_id))


def addQB(request):
    context = {}
    form = QuestboardForm()
    f = QuestboardForm(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            f.save()
            return redirect('home')
    context['form'] = form
    return render(request, 'addQB.html', context)


def addQC(request, questboard_id):
    context = {}
    data = {'questboard': Questboard.objects.filter(id=questboard_id)}
    form = QuestcardForm(initial={'questboard':Questboard.objects.get(id=questboard_id)})
    f = QuestcardForm(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            f.save()
            return redirect('/questboard/' + str(questboard_id))
    form.fields['questboard'].queryset = form.fields['questboard'].queryset.filter(id=questboard_id)
    context['form'] = form
    return render(request, 'addQC.html', context)
