from django.db import models

# Create your models here.
class operate_time(models.Model):

    click_time = models.DateTimeField()
    done_time = models.DateTimeField()
    time_gap = models.DurationField()
    click_command = models.CharField(max_length=20)

    def __str__(self):
        return self.click_command