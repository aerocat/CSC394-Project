from django import forms
from coursesDB.models import Courses
from django.forms import ModelChoiceField



class CustomField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.course_number

# class classroom(forms.Form):
#     className = CustomField( widget= forms.TextInput(attrs={'class':'form-control'}),
#         queryset= Courses.objects.order_by('course_number')
#     )
#     online = forms.ChoiceField(choices=[("Online", 'Online'),('Not Online', 'Not Online')])

class classroom(forms.Form):
    # First = CustomField(
    #     queryset= Courses.objects.order_by('course_number')
    # )
    # Second = CustomField(
    #     queryset=Courses.objects.order_by('course_number')
    # )
    Electives = forms.ChoiceField(choices= [(1," Intro Courses"), (2,'Foundation Courses'),(3, "Software Systems "),(4," Data Science"),
                                                (5,"Database Systems"), (6,'Artificial Intelligence'), (7,"Software Engineering"),
                                                (8, 'Game and Real Time Systems'), (9, "Human Computer Interactions")])
    Classes = forms.ChoiceField(choices=[(1,"1 class a quarter"),(2,"2 classes a quarter"),(3,"3 classes a quarter"),(4,"4 classes a quarter")])
    Grad = forms.ChoiceField(choices=[(True, "CS Undergraduate completed"), (False, 'CS Undergraduate not completed')])
    Time = forms.ChoiceField(choices = [('Spring','Spring'),('Fall','Fall'),('Winter','Winter'), ('Summer','Summer')])
