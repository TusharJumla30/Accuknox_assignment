import threading
import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    print(f"Signal handler thread ID: {threading.get_ident()}")
    time.sleep(2)  # Simulate a delay
    print("Signal handler finished")

# Create an instance of MyModel
obj = MyModel.objects.create(name="Test")
print("Object created")
print(f"Main thread ID: {threading.get_ident()}")
