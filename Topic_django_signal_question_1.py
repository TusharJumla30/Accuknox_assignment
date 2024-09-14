from django.dispatch import Signal
import time

# Define the custom signal
my_signal = Signal()

# Receiver functions
def receiver1(sender, **kwargs):
    print("Receiver 1 started")
    time.sleep(2)  # Simulating work
    print("Receiver 1 finished")

def receiver2(sender, **kwargs):
    print("Receiver 2 started")
    time.sleep(2)  # Simulating work
    print("Receiver 2 finished")

# Connect the receivers to the signal
my_signal.connect(receiver1)
my_signal.connect(receiver2)

# Send the signal
print("Send signal...")
my_signal.send(sender="sender", message="Hello, world!")
print("Signal sent...")
