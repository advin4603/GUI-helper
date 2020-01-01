from GuiResources import GuiMaker
from math import *

"""Using GUI HELPER TO MAKE SIMPLE CALCULATOR"""

with GuiMaker(font_style='Century gothic',padx=15,pady=20,bg='Black',Title='Calculator',fg='Light Blue') as gui:
    gui.Header('Calculator')
    gui.Input(prompt='Enter:')

    @gui.onInput
    def process(inp):
        try:
            gui.Output(eval(inp))
        except:
            gui.Output('ERROR')
