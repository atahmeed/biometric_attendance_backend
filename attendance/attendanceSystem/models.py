from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique = True,primary_key = True)
    present = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.roll)

class Attendance(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    roll = models.ForeignKey(Student , on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        if not self.pk:
            Student.objects.filter(pk = self.roll_id).update(present = models.F('present')+1)
        super().save(*args,**kwargs)    

    class Meta:
        unique_together = (('date','roll'),)

    def __str__(self):
        return str(self.roll)