from django.db import models
from django import forms

# Create your models here.

CATEGORY_CHOICES = [
    ('work', 'Work'),
    ('studies', 'Studies'),
    ('personal', 'Personal'),
    ('shopping', 'Shopping'),
    ('other', 'Other'),
]

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('due_date',)

    def __str__(self):
        return self.title