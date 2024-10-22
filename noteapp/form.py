from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['nName', 'nDate', 'nDescription', 'image', 'pdf', 'folder']
        widgets = {
            'nDescription': forms.Textarea(attrs={'cols': 80, 'rows': 20}),  # 使用文本區域
            'nDate': forms.TextInput(attrs={'type': 'date'}),  # 使用日期選擇器
        }
