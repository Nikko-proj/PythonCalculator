import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Basic Calculator")
        #setting window size
        width=410
        height=240
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_221=tk.Button(root)
        GButton_221["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_221["font"] = ft
        GButton_221["fg"] = "#000000"
        GButton_221["justify"] = "center"
        GButton_221["text"] = "1"
        GButton_221.place(x=50,y=70,width=70,height=25)
        GButton_221["command"] = self.GButton_221_command

        GButton_778=tk.Button(root)
        GButton_778["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_778["font"] = ft
        GButton_778["fg"] = "#000000"
        GButton_778["justify"] = "center"
        GButton_778["text"] = "4"
        GButton_778.place(x=50,y=100,width=70,height=25)
        GButton_778["command"] = self.GButton_778_command

        GButton_357=tk.Button(root)
        GButton_357["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_357["font"] = ft
        GButton_357["fg"] = "#000000"
        GButton_357["justify"] = "center"
        GButton_357["text"] = "7"
        GButton_357.place(x=50,y=130,width=70,height=25)
        GButton_357["command"] = self.GButton_357_command

        GButton_848=tk.Button(root)
        GButton_848["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_848["font"] = ft
        GButton_848["fg"] = "#000000"
        GButton_848["justify"] = "center"
        GButton_848["text"] = "2"
        GButton_848.place(x=130,y=70,width=70,height=25)
        GButton_848["command"] = self.GButton_848_command

        GButton_390=tk.Button(root)
        GButton_390["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_390["font"] = ft
        GButton_390["fg"] = "#000000"
        GButton_390["justify"] = "center"
        GButton_390["text"] = "5"
        GButton_390.place(x=130,y=100,width=70,height=25)
        GButton_390["command"] = self.GButton_390_command

        GButton_56=tk.Button(root)
        GButton_56["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_56["font"] = ft
        GButton_56["fg"] = "#000000"
        GButton_56["justify"] = "center"
        GButton_56["text"] = "8"
        GButton_56.place(x=130,y=130,width=70,height=25)
        GButton_56["command"] = self.GButton_56_command

        GButton_809=tk.Button(root)
        GButton_809["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_809["font"] = ft
        GButton_809["fg"] = "#000000"
        GButton_809["justify"] = "center"
        GButton_809["text"] = "3"
        GButton_809.place(x=210,y=70,width=70,height=25)
        GButton_809["command"] = self.GButton_809_command

        GButton_803=tk.Button(root)
        GButton_803["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_803["font"] = ft
        GButton_803["fg"] = "#000000"
        GButton_803["justify"] = "center"
        GButton_803["text"] = "6"
        GButton_803.place(x=210,y=100,width=70,height=25)
        GButton_803["command"] = self.GButton_803_command

        GButton_585=tk.Button(root)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "9"
        GButton_585.place(x=210,y=130,width=70,height=25)
        GButton_585["command"] = self.GButton_585_command

        GButton_450=tk.Button(root)
        GButton_450["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_450["font"] = ft
        GButton_450["fg"] = "#000000"
        GButton_450["justify"] = "center"
        GButton_450["text"] = "0"
        GButton_450.place(x=130,y=160,width=70,height=25)
        GButton_450["command"] = self.GButton_450_command

        GButton_51=tk.Button(root)
        GButton_51["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_51["font"] = ft
        GButton_51["fg"] = "#000000"
        GButton_51["justify"] = "center"
        GButton_51["text"] = "+"
        GButton_51.place(x=290,y=70,width=70,height=25)
        GButton_51["command"] = self.GButton_51_command

        GButton_486=tk.Button(root)
        GButton_486["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_486["font"] = ft
        GButton_486["fg"] = "#000000"
        GButton_486["justify"] = "center"
        GButton_486["text"] = "-"
        GButton_486.place(x=290,y=100,width=70,height=25)
        GButton_486["command"] = self.GButton_486_command

        GButton_875=tk.Button(root)
        GButton_875["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_875["font"] = ft
        GButton_875["fg"] = "#000000"
        GButton_875["justify"] = "center"
        GButton_875["text"] = "*"
        GButton_875.place(x=290,y=130,width=70,height=25)
        GButton_875["command"] = self.GButton_875_command

        GButton_958=tk.Button(root)
        GButton_958["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_958["font"] = ft
        GButton_958["fg"] = "#000000"
        GButton_958["justify"] = "center"
        GButton_958["text"] = "/"
        GButton_958.place(x=290,y=160,width=70,height=25)
        GButton_958["command"] = self.GButton_958_command

        GButton_882=tk.Button(root)
        GButton_882["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_882["font"] = ft
        GButton_882["fg"] = "#000000"
        GButton_882["justify"] = "center"
        GButton_882["text"] = "="
        GButton_882.place(x=210,y=160,width=70,height=25)
        GButton_882["command"] = self.GButton_882_command

        GButton_558=tk.Button(root)
        GButton_558["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_558["font"] = ft
        GButton_558["fg"] = "#000000"
        GButton_558["justify"] = "center"
        GButton_558["text"] = "Clear"
        GButton_558.place(x=50,y=160,width=70,height=25)
        GButton_558["command"] = self.GButton_558_command

        GMessage_55=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_55["font"] = ft
        GMessage_55["fg"] = "#333333"
        GMessage_55["justify"] = "right"
        GMessage_55["text"] = "Message"
        GMessage_55["relief"] = "ridge"
        GMessage_55.place(x=50,y=10,width=310,height=55)

    def GButton_221_command(self):
        print("command")


    def GButton_778_command(self):
        print("command")


    def GButton_357_command(self):
        print("command")


    def GButton_848_command(self):
        print("command")


    def GButton_390_command(self):
        print("command")


    def GButton_56_command(self):
        print("command")


    def GButton_809_command(self):
        print("command")


    def GButton_803_command(self):
        print("command")


    def GButton_585_command(self):
        print("command")


    def GButton_450_command(self):
        print("command")


    def GButton_51_command(self):
        print("command")


    def GButton_486_command(self):
        print("command")


    def GButton_875_command(self):
        print("command")


    def GButton_958_command(self):
        print("command")


    def GButton_882_command(self):
        print("command")


    def GButton_558_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
