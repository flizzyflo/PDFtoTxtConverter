
from tkinter import Button

class OwnButton(Button):
    """OwnButton Class inheriting from tkinter button class"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"'{self.cget('text')}' - Button"

    def __str__(self) -> str:
        return f"'{self.cget('text')}' - Button"