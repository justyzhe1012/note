# models.py
from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Note(models.Model):
    nName = models.CharField(max_length=30, null=False)
    nDate = models.DateField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)

    def __str__(self):
        return self.nName

class NoteContent(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='contents')
    content = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=0)  # 用於排序內容段落

    class Meta:
        ordering = ['order']

class NoteImage(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class NotePDF(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='pdfs')
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']