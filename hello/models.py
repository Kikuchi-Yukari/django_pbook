from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator

class Friend(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    icon = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '<User:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'

class Pbook(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE) 
    item = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    collection_date = models.DateField()
    pbook_image = models.ImageField(upload_to='image/')     

    def __str__(self):
        return '<Pbook:id=' + str(self.id) + ', ' + \
            str(self.friend) + '(' + str(self.collection_date) + ')>'
    
    class Meta:
        ordering = ('collection_date',)
