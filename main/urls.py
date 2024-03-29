from django.urls import path
from main.views import main, questboard, addPerson, addQB, addQC, editName, editDescription, editStars, confirm, studentQuestboard, editQC
urlpatterns = [
    path('home/', main.as_view(), name='home'),
    path('questboard/<questboard_id>/', questboard.as_view() , name='questboard'),
    path('addPerson/<int:questcard_id>/<int:questboard_id>', addPerson, name='addPerson'),
    path('addQB', addQB, name="addQB"),
    path('addQC/<questboard_id>', addQC, name="addQC"),
    path('editName/<questboard_id>', editName, name="editname" ),
    path('editDescription/<questboard_id>', editDescription, name="editDescription" ),
    path('editStars/<questboard_id>', editStars, name="editStars" ),
    path('studentQuestboard/<questboard_id>', studentQuestboard.as_view(), name="studentQuestboard" ),
    path('confirm', confirm, name='confirm'),
    path('editQC/<questboard_id>/<questcard_id>', editQC, name="editQC")
]

