import threading
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def signal_handler(sender, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")
