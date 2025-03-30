from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):  # Draw methods implements polymorphism
    for control in controls:
        # Python is dynamic language and it does not matter what type of object. But it should have draw function in this case.
        control.draw()


ddl = DropDownList()
text_box = TextBox()
draw([ddl, text_box])  # DropDownList, TextBox
