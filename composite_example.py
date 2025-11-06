from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(FileSystemComponent):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name} ({self.size} KB)")

    def get_size(self):
        return self.size


class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        if component not in self.children:
            self.children.append(component)
            print(f"Added '{component.name}' to '{self.name}'.")
        else:
            print(f"'{component.name}' already exists in '{self.name}'.")

    def remove(self, component):
        if component in self.children:
            self.children.remove(component)
            print(f"Removed '{component.name}' from '{self.name}'.")
        else:
            print(f"'{component.name}' not found in '{self.name}'.")

    def display(self, indent=0):
        print(" " * indent + f"[Directory] {self.name}")
        for child in self.children:
            child.display(indent + 4)

    def get_size(self):
        total = sum(child.get_size() for child in self.children)
        return total


if __name__ == "__main__":
    file1 = File("movie.mp4", 1200)
    file2 = File("song.mp3", 5)
    file3 = File("game.exe", 500)
    file4 = File("photo.png", 2)

    root = Directory("Root")
    media = Directory("Media")
    games = Directory("Games")
    pictures = Directory("Pictures")

    media.add(file1)
    media.add(file2)
    games.add(file3)
    pictures.add(file4)

    root.add(media)
    root.add(games)
    root.add(pictures)

    print("\n--- File System Structure ---")
    root.display()

    print(f"\nTotal size of Root directory: {root.get_size()} KB")
