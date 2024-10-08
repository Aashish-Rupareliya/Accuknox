from django.db import transaction
from django.http import HttpResponse
from .models import MyModel

def my_view(request):
    try:
        with transaction.atomic():
            instance = MyModel.objects.create(name="Test")
            print("Model saved")
            raise Exception("Rolling back transaction")
    except Exception as e:
        print(f"Exception occurred: {e}")
    return HttpResponse("Transaction rolled back")
