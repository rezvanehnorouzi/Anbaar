import os
from Panel import *
 
class Wellcome(Panel):
    size = ()
    i_user = tk.PhotoImage
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.__widget()

    def __widget(self):
        self.i_user = tk.PhotoImage(file=self.resource["User_icon_2"])
        l_user = tk.Label(self, image=self.i_user)
        l_user.pack()

        f_data = tk.LabelFrame(self)
        f_data.pack()
        # username
        l_username = tk.Label(f_data, text="نام کاربری")
        l_username.grid(column=1, row=0)
        e_username = tk.Entry(f_data)
        e_username.grid(column=0, row=0)
        # password
        l_password = tk.Label(f_data, text="رمز عبور")
        l_password.grid(column=1, row=1)
        e_password = tk.Entry(f_data)
        e_password.grid(column=0, row=1)

        f_butt = tk.Frame(self)
        f_butt.pack()

        b_vorod = tk.Button(f_butt, text="ورود", padx=30)
        b_vorod["command"] = lambda: (self.destroy(), Panel())
        b_vorod.grid(column=1, row=2, sticky=tk.NSEW)
        b_khroj = tk.Button(f_butt, text="خروج", padx=30)
        b_khroj["command"] = lambda: (self.destroy(), exit())
        b_khroj.grid(column=0, row=2, sticky=tk.NSEW)
