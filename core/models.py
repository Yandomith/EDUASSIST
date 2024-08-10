from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING')
    ]
    priority_choices = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣')
    ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=5, choices=priority_choices)
    due_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} ToDo'

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.user.username} Note'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

class StudyMaterials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='study_materials')
    subject_choices = [
        ('Compiler', 'Compiler'),
        ('MM', 'MM'),
        ('Java', 'Java'),
        ('SPM', 'SPM'),
        ('BRM', 'BRM'),
    ]
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    subject = models.CharField(max_length=50, choices=subject_choices)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.subject}'