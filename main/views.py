from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from .forms import *


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
        context['qb'] = Questboard.objects.get(id=pk)
        return context


class studentQuestboard(TemplateView):
    template_name = 'studentQuestboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['questboard_id']
        context['questboard'] = Questboard.objects.get(
            id=pk).questcard_set.all()
        context['qbid'] = pk
        context['qb'] = Questboard.objects.get(id=pk)
        return context


# def addPerson(request, questcard_id, questboard_id):
#     questcard = Questcard.objects.get(id=questcard_id)
#     context = {}
#     if questcard.person1 is not None and questcard.person2 is None and questcard.person3 is None:
#         form = addPerson1Form()
#     elif questcard.person1 is not None and questcard.person2 is not None and questcard.person3 is None:
#         form = addPersonThreeForm()
#     elif questcard.person1 is None and questcard.person2 is None and questcard.person3 is None:
#         form = addPersonForm()

#     if request.method == 'POST':
#         print(request.POST['slot'])
#         a = request.POST['slot']
#         if a == "Slot 1":
#             questcard.person1 = request.POST['name']
#             questcard.save()
#             return redirect('/questboard/' + str(questboard_id))
#         elif a == "Slot 2":
#             questcard.person2 = request.POST['name']
#             questcard.save()
#             return redirect('/questboard/' + str(questboard_id))
#         elif a == "Slot 3":
#             print("QWEQWEQWEQWEWQE")
#             questcard.person3 = request.POST['name']
#             questcard.save()
#             return redirect('/questboard/' + str(questboard_id))
#     context['form'] = form
#     return render(request, 'addPerson.html',context)

def addPerson(request, questcard_id, questboard_id):
    questcard = Questcard.objects.get(id=questcard_id)
    context = {}
    if questcard.person1 is not None and questcard.person2 is None and questcard.person3 is None:
        form = addPerson1Form()
    elif questcard.person1 is not None and questcard.person2 is not None and questcard.person3 is None:
        form = addPersonThreeForm()
    elif questcard.person1 is None and questcard.person2 is None and questcard.person3 is None:
        form = addPersonForm()
    elif questcard.person1 is None and questcard.person2 is not None and questcard.person3 is None:
        form = addPerson2Form()
    elif questcard.person1 is None and questcard.person2 is None and questcard.person3 is not None:
        form = addPerson3Form()
    elif questcard.person1 is None and questcard.person2 is not None and questcard.person3 is not None:
        form = addPersonOneForm()
    elif questcard.person1 is not None and questcard.person2 is None and questcard.person3 is not None:
        form = addPersonTwoForm()
    if request.method == 'POST':
        a = request.POST['slot']
        b = request.POST['name']
        if a == "Slot 1":
            context = {'questcard_id': questcard_id,
                       'questboard_id': questboard_id, 'a': a, 'b': b}
            return render(request, 'confirmation.html', context)
            # return redirect('/confirm/' + str(questcard_id) +'/' + str(questboard_id))
        elif a == "Slot 2":
            context = {'questcard_id': questcard_id,
                       'questboard_id': questboard_id, 'a': a, 'b': b}
            return render(request, 'confirmation.html', context)
            print("QWEQWEQWEQWEWQE")
            context = {'questcard_id': questcard_id,
                       'questboard_id': questboard_id, 'a': a, 'b': b}
            return render(request, 'confirmation.html', context)
        elif a == "Slot 3":
            context = {'questcard_id': questcard_id,
                       'questboard_id': questboard_id, 'a': a, 'b': b}
            return render(request, 'confirmation.html', context)
            print("QWEQWEQWEQWEWQE")
            context = {'questcard_id': questcard_id,
                       'questboard_id': questboard_id, 'a': a, 'b': b}
            return render(request, 'confirmation.html', context)
    context['form'] = form
    return render(request, 'addPerson.html', context)


def confirm(request):
    if request.method == 'POST':
        questcard_id = int(request.POST['questcard_id'])
        questboard_id = int(request.POST['questboard_id'])
        questcard = Questcard.objects.get(id=questcard_id)
        a = request.POST['a']
        if a == "Slot 1":
            questcard.person1 = request.POST['name']
            questcard.save()
            return redirect('/studentQuestboard/' + str(questboard_id))
        elif a == "Slot 2":
            questcard.person2 = request.POST['name']
            questcard.save()
            return redirect('/studentQuestboard/' + str(questboard_id))
        elif a == "Slot 3":
            print("QWEQWEQWEQWEWQE")
            questcard.person3 = request.POST['name']
            questcard.save()
            return redirect('/studentQuestboard/' + str(questboard_id))
    return redirect('/studentQuestboard' + str(questboard_id))


def addQB(request):
    context = {}
    form = QuestboardForm()
    f = QuestboardForm(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            f.save()
            latest = Questboard.objects.latest('id')
            return redirect('questboard/' + str(latest.id))
    context['form'] = form
    return render(request, 'addQB.html', context)


def addQC(request, questboard_id):
    context = {}
    data = {'questboard': Questboard.objects.filter(id=questboard_id)}
    form = QuestcardForm(
        initial={'questboard': Questboard.objects.get(id=questboard_id)})
    f = QuestcardForm(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            f.save()
            return redirect('/questboard/' + str(questboard_id))
    form.fields['questboard'].queryset = form.fields['questboard'].queryset.filter(
        id=questboard_id)
    context['form'] = form
    return render(request, 'addQC.html', context)


def editName(request, questboard_id):

    if request.method == 'POST':
        questboard = Questboard.objects.get(id=questboard_id)
        questboard.name = request.POST['name']
        questboard.save()
        return redirect('/questboard/' + str(questboard_id))
    return render(request, 'edit.html', {'questboard_id': questboard_id})


def editDescription(request, questboard_id):

    if request.method == 'POST':
        questboard = Questboard.objects.get(id=questboard_id)
        questboard.description = request.POST['name']
        questboard.save()
        return redirect('/questboard/' + str(questboard_id))
    return render(request, 'editDescription.html', {'questboard_id': questboard_id})


def editStars(request, questboard_id):

    if request.method == 'POST':
        questboard = Questboard.objects.get(id=questboard_id)
        questboard.stars = int(request.POST['number'])
        questboard.save()
        return redirect('/questboard/' + str(questboard_id))
    return render(request, 'editStars.html', {'questboard_id': questboard_id})


def editQC(request, questboard_id, questcard_id):
    questcard = Questcard.objects.get(id=questcard_id)
    context = {}
    data = {'questboard': Questboard.objects.filter(id=questboard_id)}
    form = QuestcardForm(initial={'questboard': Questboard.objects.get(
        id=questboard_id)}, instance=questcard)
    f = QuestcardForm(request.POST, instance=questcard)
    if request.method == 'POST':
        if f.is_valid():
            f.save()
            return redirect('/questboard/' + str(questboard_id))
    form.fields['questboard'].queryset = form.fields['questboard'].queryset.filter(
        id=questboard_id)
    context['form'] = form
    return render(request, 'addQC.html', context)
