from django.urls import path
from main.views import main, questboard, addPerson, addQB, addQC

urlpatterns = [
    path('home/', main.as_view(), name='home'),
    path('questboard/<questboard_id>/', questboard.as_view() , name='questboard'),
    path('addPerson/<int:questcard_id>/<int:questboard_id>', addPerson, name='addPerson'),
    path('addQB', addQB, name="addQB"),
    path('addQC/<questboard_id>', addQC, name="addQC")
]

