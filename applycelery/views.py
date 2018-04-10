from django.shortcuts import render
from .models import operate_time
from .tasks import celery, celery_delay
from django.utils import timezone
import time

# Create your views here.

def app_core(request):
    operate_list = operate_time.objects.order_by('-id').all()
    if (request.GET.get('operate')):
        click_command = "operate"
        click_time = timezone.now()
        done_time = timezone.now()
        time_gap = done_time-click_time
        form_new = operate_time(click_time=click_time, done_time=done_time, time_gap=time_gap, click_command=click_command)
        form_new.save()

    if (request.GET.get('operate_delay')):
        click_time = timezone.now()
        time.sleep(10)
        done_time = timezone.now()
        time_gap = done_time-click_time
        click_command = "operate"
        form_new = operate_time(click_time=click_time, done_time=done_time, time_gap=time_gap, click_command=click_command)
        form_new.save()

    if (request.GET.get('celery')):
        celery.delay()

    if (request.GET.get('celery_delay')):
        celery_delay.delay()

    return render(request, 'django_celery_main.html', {'operate_list': operate_list})