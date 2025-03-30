from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# TypeError: Can't instantiate abstract class Stream with abstract methods read
# Because it requires concreate implementation of read method
# class MemmoryStream(Stream):
#     pass


# TypeError: Can't instantiate abstract class Stream with abstract methods read
# stream = Stream()
