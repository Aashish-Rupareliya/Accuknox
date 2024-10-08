import threading
from django.http import HttpResponse

def my_view(request):
    print(f"View running in thread: {threading.current_thread().name}")
    return HttpResponse("Hello, world!")
