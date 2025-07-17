from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=300)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.text, self.published_date
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=300)
    correct = models.BooleanField()

    def __str__(self):
        return self.text, self.correct