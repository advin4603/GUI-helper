from tkinter import *


class Gui:
    """Simple Gui creator.
    Returned by Gui maker"""

    def __init__(self, Bg, Fg, title, Font, Icon, padx, pady):

        self.inputs = tuple()
        self.font = Font
        self.background = Bg
        self.foreground = Fg
        self.Window = Tk()
        self.Window.config(background=Bg)
        self.Window.title(title)
        self.Window.resizable(False, False)
        self.HeaderLabel = Label(self.Window, text=None, fg=self.foreground, bg=self.background, font=self.font,
                                 padx=padx, pady=pady)
        self.OutputLabel = Label(self.Window, text=None, fg=self.foreground, bg=self.background, font=self.font,
                                 padx=padx, pady=pady)
        self.PromptLabel = Label(self.Window, text=None, fg=self.foreground, bg=self.background, font=self.font,
                                 padx=padx, pady=pady)
        self.InputField = Entry(self.Window, fg=self.foreground, bg=self.background, font=self.font, relief=FLAT)
        self.InputButton = Button(self.Window, command=self.Input_enter, fg=self.foreground, bg=self.background,
                                  text='Submit', font=self.font, relief=FLAT, padx=padx, pady=pady, overrelief=RIDGE)
        self.InputField.config(insertbackground=Fg)
        self.OutputSideText = Label(self.Window, text=None, fg=self.foreground, bg=self.background, font=self.font,
                                    padx=padx, pady=pady)
        if Icon is not None:
            self.Window.iconbitmap(Icon)

    def Input_enter(self):
        """Defines course on Hitting submit"""
        text = self.InputField.get()
        self.inputs += (text,)

    def Header(self, *args, sep=' '):
        """Creates Header Label"""
        text = sep.join([str(item) for item in args])
        self.HeaderLabel.config(text=text)
        self.HeaderLabel.grid(row=0, column=0, columnspan=2)

    def Output(self, *args, sep=' ', label=None):
        """Creates Output Label"""
        text = sep.join([str(item) for item in args])
        self.OutputLabel.config(text=text)
        self.OutputSideText.config(text=label)
        if label is None:
            self.OutputLabel.grid(row=3, column=0, columnspan=2)
        else:
            self.OutputLabel.grid(row=3, column=1)
            self.OutputSideText.grid(row=3, column=0)

    def Input(self, prompt=''):
        """"Creates Input Label"""
        self.PromptLabel.config(text=prompt)
        self.PromptLabel.grid(row=1, column=0)
        self.InputField.grid(row=1, column=1)
        self.InputButton.grid(row=2, column=0, columnspan=2)

    def onInput(self, func):
        """Decorator to be used For evaluating input use decorator on a function requiring one argument that
        is given by User"""

        def new_func():
            text = self.InputField.get()
            self.inputs += (text,)
            func(text)

        # noinspection PyAttributeOutsideInit
        self.Input_enter = new_func
        self.InputButton.config(command=self.Input_enter)
        return func


class GuiMaker:
    """To be used as context Manager. Returns GUI object"""

    def __init__(self, font_style='Times', font_size=70, fg='Green', bg='Black', Title='My Program', IconPath=None,
                 padx=5, pady=10):
        self.fg = fg
        self.bg = bg
        self.title = Title
        self.font = (font_style, font_size)
        self.Icon = IconPath
        self.padx = padx
        self.pady = pady

    def __enter__(self):
        self.gui_obj = Gui(self.bg, self.fg, self.title, self.font, self.Icon,self.padx,self.pady)
        return self.gui_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.gui_obj.Window.mainloop()


def main():
    """Example:-"""
    with GuiMaker(font_style='Century gothic',padx=15,pady=20) as gui:
        gui.Header('Test Window')
        gui.Input(prompt='Enter:')

        @gui.onInput
        def program(inp):
            if len(gui.inputs) < 4:
                gui.Output('\n'.join(gui.inputs))
            else:
                gui.Output(inp, label='Output:')


if __name__ == '__main__':
    main()
