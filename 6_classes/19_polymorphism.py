from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):  # Draw methods implements polymorphism
    for control in controls:
        control.draw()


ddl = DropDownList()
text_box = TextBox()
draw([ddl, text_box])  # DropDownList, TextBox
