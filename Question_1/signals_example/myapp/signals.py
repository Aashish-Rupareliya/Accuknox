import time
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def signal_handler(sender, **kwargs):
    print("Signal handler started")
    time.sleep(5) 
    print("Signal handler finished")
