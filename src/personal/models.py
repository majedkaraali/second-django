from django.db import models


PRIORITY=[
("H","Heigh"),
("M","Medium"),
("L","LoW")
]
# Create your models here.
class Question(models.Model):
    title= models.CharField(max_length=60)
    question= models.TextField(max_length=60)
    priority=models.CharField(max_length=1,choices=PRIORITY)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="The Question"
        verbose_name_plural="pepole Questions"