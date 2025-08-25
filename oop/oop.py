from abc import ABC, abstractmethod

class Human:
    def __init__(self, name):
        pass
    def jump(self):
        raise NotImplementedError("Not implemented yet")


class Person(Human):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    def jump(self):
        print(f"{self.name} is jumping")

alex = Person("Alex")
alex.jump()


class Storage(ABC):
    @abstractmethod
    def save(self, data: str) -> None:
        pass

    @abstractmethod
    def load(self) -> str:
        pass

# ❌ Will raise an error if you try to instantiate directly
# storage = Storage()
# TypeError: Can't instantiate abstract class Storage with abstract methods load, save

class FileStorage(Storage):
    def save(self, data: str) -> None:
        with open("data.txt", "w") as f:
            f.write(data)

    def load(self) -> str:
        with open("data.txt", "r") as f:
            return f.read()

storage = FileStorage()  # ✅ Works fine