from django.db import models

# Create your models here.
class Student_table(models.Model):
    reg_no=models.IntegerField(primary_key=True)
    name=models.CharField()
    email=models.EmailField(default='example@gmail.com')
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    dob=models.DateField()
def __str__(self):
    return self.name