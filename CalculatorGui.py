import tkinter as tk
import tkinter.font as tkFont
import CalcConstants as CTS
import QuickCalculator as QC # for calculator button logic


class App:
    def __init__(self, root):
        # setting title
        #root.title("Calculator {}".format)
        # setting window size
        width = CTS.WINDOW_WIDTH
        height = CTS.WINDOW_HEIGHT
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.title("Calculator {}".format(alignstr))

        # Button 1
        button_1 = tk.Button(root)
        button_1["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_1["font"] = ft
        button_1["fg"] = CTS.BUTTON_TEXT_COLOR
        button_1["highlightcolor"] = CTS.BUTTON_HIGHTLIGHTCOLOR
        button_1["justify"] = CTS.BUTTON_JUSTIFY
        button_1["text"] = "1"
        button_1.place(x=50, y=70, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_1["command"] = self.button_1_command

        # Button 4
        button_4 = tk.Button(root)
        button_4["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_4["font"] = ft
        button_4["fg"] = CTS.BUTTON_TEXT_COLOR
        button_4["justify"] = CTS.BUTTON_JUSTIFY
        button_4["text"] = "4"
        button_4.place(x=50, y=100, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_4["command"] = self.button_4_command

        # Button 7
        button_7 = tk.Button(root)
        button_7["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_7["font"] = ft
        button_7["fg"] = CTS.BUTTON_TEXT_COLOR
        button_7["justify"] = CTS.BUTTON_JUSTIFY
        button_7["text"] = "7"
        button_7.place(x=50, y=130, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_7["command"] = self.button_7_command

        # Button 2
        button_2 = tk.Button(root)
        button_2["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_2["font"] = ft
        button_2["fg"] = CTS.BUTTON_TEXT_COLOR
        button_2["justify"] = CTS.BUTTON_JUSTIFY
        button_2["text"] = "2"
        button_2.place(x=130, y=70, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_2["command"] = self.button_2_command

        # Button 5
        button_5 = tk.Button(root)
        button_5["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_5["font"] = ft
        button_5["fg"] = CTS.BUTTON_TEXT_COLOR
        button_5["justify"] = CTS.BUTTON_JUSTIFY
        button_5["text"] = "5"
        button_5.place(x=130, y=100, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_5["command"] = self.button_5_command

        # Button 8
        button_8 = tk.Button(root)
        button_8["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_8["font"] = ft
        button_8["fg"] = CTS.BUTTON_TEXT_COLOR
        button_8["justify"] = CTS.BUTTON_JUSTIFY
        button_8["text"] = "8"
        button_8.place(x=130, y=130, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_8["command"] = self.button_8_command

        # Button 3
        button_3 = tk.Button(root)
        button_3["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_3["font"] = ft
        button_3["fg"] = CTS.BUTTON_TEXT_COLOR
        button_3["justify"] = CTS.BUTTON_JUSTIFY
        button_3["text"] = "3"
        button_3.place(x=210, y=70, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_3["command"] = self.button_3_command

        # Button 6
        button_6 = tk.Button(root)
        button_6["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_6["font"] = ft
        button_6["fg"] = CTS.BUTTON_TEXT_COLOR
        button_6["justify"] = CTS.BUTTON_JUSTIFY
        button_6["text"] = "6"
        button_6.place(x=210, y=100, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_6["command"] = self.button_6_command

        # Button 9
        button_9 = tk.Button(root)
        button_9["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_9["font"] = ft
        button_9["fg"] = CTS.BUTTON_TEXT_COLOR
        button_9["justify"] = CTS.BUTTON_JUSTIFY
        button_9["text"] = "9"
        button_9.place(x=210, y=130, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_9["command"] = self.button_9_command

        # Button 0
        button_0 = tk.Button(root)
        button_0["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_0["font"] = ft
        button_0["fg"] = CTS.BUTTON_TEXT_COLOR
        button_0["justify"] = CTS.BUTTON_JUSTIFY
        button_0["text"] = "0"
        button_0.place(x=130, y=160, width=CTS.BUTTON_WIDTH,
                       height=CTS.BUTTON_HEIGHT)
        button_0["command"] = self.button_0_command

        # Button plus (+)
        button_plus = tk.Button(root)
        button_plus["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_plus["font"] = ft
        button_plus["fg"] = CTS.BUTTON_TEXT_COLOR
        button_plus["justify"] = CTS.BUTTON_JUSTIFY
        button_plus["text"] = "+"
        button_plus.place(x=290, y=70, width=CTS.BUTTON_WIDTH,
                          height=CTS.BUTTON_HEIGHT)
        button_plus["command"] = self.button_plus_command

        # Button minus (-)
        button_minus = tk.Button(root)
        button_minus["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_minus["font"] = ft
        button_minus["fg"] = CTS.BUTTON_TEXT_COLOR
        button_minus["justify"] = CTS.BUTTON_JUSTIFY
        button_minus["text"] = "-"
        button_minus.place(
            x=290, y=100, width=CTS.BUTTON_WIDTH, height=CTS.BUTTON_HEIGHT)
        button_minus["command"] = self.button_minus_command

        # Button mult (*)
        button_mult = tk.Button(root)
        button_mult["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_mult["font"] = ft
        button_mult["fg"] = CTS.BUTTON_TEXT_COLOR
        button_mult["justify"] = CTS.BUTTON_JUSTIFY
        button_mult["text"] = "*"
        button_mult.place(x=290, y=130, width=CTS.BUTTON_WIDTH,
                          height=CTS.BUTTON_HEIGHT)
        button_mult["command"] = self.button_mult_command

        # Button div (/)
        button_div = tk.Button(root)
        button_div["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_div["font"] = ft
        button_div["fg"] = CTS.BUTTON_TEXT_COLOR
        button_div["justify"] = CTS.BUTTON_JUSTIFY
        button_div["text"] = "/"
        button_div.place(x=290, y=160, width=CTS.BUTTON_WIDTH,
                         height=CTS.BUTTON_HEIGHT)
        button_div["command"] = self.button_div_command

        # Button equal (=)
        button_dot = tk.Button(root)
        button_dot["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_dot["font"] = ft
        button_dot["fg"] = CTS.BUTTON_TEXT_COLOR
        button_dot["justify"] = CTS.BUTTON_JUSTIFY
        button_dot["text"] = "."
        button_dot.place(
            x=210, y=160, width=CTS.BUTTON_WIDTH, height=CTS.BUTTON_HEIGHT)
        button_dot["command"] = self.button_dot_command

        # Button clr (clear)
        button_clr = tk.Button(root)
        button_clr["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_clr["font"] = ft
        button_clr["fg"] = CTS.BUTTON_TEXT_COLOR
        button_clr["justify"] = CTS.BUTTON_JUSTIFY
        button_clr["text"] = "Clear"
        button_clr.place(x=50, y=160, width=CTS.BUTTON_WIDTH,
                         height=CTS.BUTTON_HEIGHT)
        button_clr["command"] = self.button_clr_command

        # Button equal (=)
        button_eql = tk.Button(root)
        button_eql["bg"] = CTS.BUTTON_TEXT_COLOR_ONCLICK
        ft = tkFont.Font(family=CTS.BUTTON_FONT, size=CTS.BUTTON_FONT_SIZE)
        button_eql["font"] = ft
        button_eql["fg"] = CTS.BUTTON_TEXT_COLOR
        button_eql["justify"] = CTS.BUTTON_JUSTIFY
        button_eql["text"] = "="
        button_eql.place(x=50,y=190,
                    width=CTS.BIG_BUTTON_WIDTH, height=CTS.BUTTON_HEIGHT)
        button_eql["command"] = self.button_eql_command

        # Message window
        # message_window = tk.Message(root)
        # ft = tkFont.Font(family=CTS.WINDOW_WIDGET_FONT,
        #                  size=CTS.WINDOW_WIDGET_FONT_SIZE)
        # message_window["font"] = ft
        # message_window["fg"] = "#333333"
        # message_window["justify"] = CTS.WINDOW_WIDGET_JUSTIFY
        # message_window["text"] = "Numbers go here"
        # message_window["relief"] = "ridge"
        # message_window.place(
        #     x=50, y=10, width=CTS.WINDOW_WIDGET_WIDTH, height=CTS.WINDOW_WIDGET_HEIGHT)

        # Textbox creation
        text_input = tk.Text(root)
        ft = tkFont.Font(family=CTS.WINDOW_TEXT_INPUT_FONT,
                         size=CTS.WINDOW_TEXT_INPUT_FONT_SIZE)
        text_input["font"] = ft
        text_input["fg"] = "#333333"
        text_input["relief"] = CTS.WINDOW_TEXT_INPUT_RELIEF
        text_input["state"] = 'disabled'
        text_input.place(x=50,y=10,
        width=CTS.WINDOW_TEXT_INPUT_WIDTH,height=CTS.WINDOW_TEXT_INPUT_HEIGHT)
        


    def button_1_command(self):
        print("Button 1")
        

    def button_4_command(self):
        print("Button 4")

    def button_7_command(self):
        print("Button 7")

    def button_2_command(self):
        print("Button 2")

    def button_5_command(self):
        print("Button 5")

    def button_8_command(self):
        print("Button 8")

    def button_3_command(self):
        print("Button 3")

    def button_6_command(self):
        print("Button 6")

    def button_9_command(self):
        print("Button 9")

    def button_0_command(self):
        print("Button 0")

    def button_plus_command(self):
        print("Button +")

    def button_minus_command(self):
        print("Button -")

    def button_mult_command(self):
        print("Button *")

    def button_div_command(self):
        print("Button /")

    def button_dot_command(self):
        print("Button .")

    def button_clr_command(self):
        print("Button clr")

    def button_eql_command(self):
        print("Button eql")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
