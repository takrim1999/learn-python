import time

class StopWatch:
    def __init__(self):
        self.value = 0
        self.started = False
        self.startTime = time.time()
        self.stopTime = time.time()

    def start(self):
        if self.started:
            print("Already running!")
        else:
            self.startTime = time.time()
            self.started = True

    def stop(self):
        if not self.started:
            print("Not started yet!")
        else:
            self.stopTime = time.time()
            self.started = False

    def show(self):
        self.value += (self.stopTime - self.startTime)
        print(self.value)