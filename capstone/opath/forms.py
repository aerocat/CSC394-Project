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
    First = CustomField(
        queryset= Courses.objects.order_by('course_number')
    )
    Second = CustomField(
        queryset=Courses.objects.order_by('course_number')
    )
    Schedule = forms.ChoiceField(choices=[(1,"1 class a quarter"),(2,"2 classes a quarter"),(3,"3 classes a quarter"),(4,"4 classes a quarter"),(5,"5 classes a quarter")])
    Online = forms.ChoiceField(choices=[(True, "Online"), (False, 'Not Online')])
    Credits = forms.ChoiceField(choices=[(2, "2 Quarter Class"), (4," 4 Quarter Class")])
    Quarter = forms.ChoiceField(choices = [('Spring','Spring'),('Fall','Fall'),('Winter','Winter'), ('Summer','Summer')])
