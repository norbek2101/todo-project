from functools import update_wrapper
from django.db import models

class Todo(models.Model):
    target = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    choice_color = [
        ('R', 'red'),
        ('G', 'green'),
        ('Y', 'yellow'),
        ('B', 'blue'),
        ('O', 'orange'), 
    ]
    type  = models.CharField(
        max_length=1,
        choices= choice_color,
        default='R',
    )

    def __str__(self):
        return  self.target

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'    

