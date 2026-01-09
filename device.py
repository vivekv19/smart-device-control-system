from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self._is_on = False  # internal state (protected)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def is_on(self):
        return self._is_on
