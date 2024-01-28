from django import forms 
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    class Meta:
        model = Project
        fields = ('name', 'description', 'members')

        def save(self, commit=True, user=None):
            instance = super().save(commit=False)
            if user:
                instance.created_by = user 
            if commit:
                instance.save()
            
            return instance

class TaskForm(forms.ModelForm):
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    class Meta:
        model = Task 
        fields = ['name', 'description', 'deadline_time', 'assignee', 'project']

        # def save(self, commit=True, user=None):
        #     instance = super().save(commit=False)
        #     if user:
        #         instance.created_by = user 
        #     if commit:
        #         instance.save()
            
        #     return instance