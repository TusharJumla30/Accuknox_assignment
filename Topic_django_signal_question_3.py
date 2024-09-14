from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction


class MyModel(models.Model):
    name = models.CharField(max_length=100)

class Log(models.Model):
    message = models.CharField(max_length=255)

# Signal handler
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler called. Inserting a log entry...")
    Log.objects.create(message=f"Log entry for: {instance.name}")

def create_model_instance():
    try:
        with transaction.atomic():
            print("Creating model instance...")
            # This will trigger the signal
            MyModel.objects.create(name="Test Instance")
            
            # Checking log entries created by the signal handler
            print(f"Log count inside transaction: {Log.objects.count()}")

            # Intentionally raise an error to roll back the transaction
            raise Exception("Simulated error to roll back transaction")

    except Exception as e:
        print(f"Transaction failed: {e}")
    
    # After rollback, check log entries again
    print(f"Log count after transaction rollback: {Log.objects.count()}")


create_model_instance()