class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())  # PythonPython


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append(1)  # Append called
