import os
from Panel import *


class Wellcome(Panel):
    size = ()
    i_user = tk.PhotoImage

    def __init__(self):
        super().__init__()
        self.resizable(False, False)

    def widget(self):
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
        b_vorod["command"] = lambda: (self.destroy(), Main())
        b_vorod.grid(column=1, row=2, sticky=tk.NSEW)
        b_khroj = tk.Button(f_butt, text="خروج", padx=30)
        b_khroj["command"] = lambda: (self.destroy(), exit())
        b_khroj.grid(column=0, row=2, sticky=tk.NSEW)


class Main(Panel):
    i_plus = tk.PhotoImage
    i_minus = tk.PhotoImage

    def widget(self):
        f_tabaghe = tk.Frame(self)
        f_tabaghe.pack(side=tk.RIGHT, fill=tk.BOTH)

        f_tree_tabghe = tk.Frame(f_tabaghe)
        f_tree_tabghe.pack()

        l_dasteh = tk.Label(f_tree_tabghe, text="دسته بندی")
        l_dasteh.pack()
        t_dasteh = Treeview(f_tree_tabghe, show="tree")
        t_dasteh.insert("", 'end', iid="خوراکی", text="خوراکی")
        t_dasteh.insert("", 'end', iid="اسيدی", text="اسيدی")
        t_dasteh.pack()

        f_but_tabghe = tk.Frame(f_tabaghe)
        f_but_tabghe.pack()

        self.i_plus = tk.PhotoImage(file=self.resource["plus"])
        b_adddaste = tk.Button(f_but_tabghe, image=self.i_plus)
        e_adddaste = tk.Entry(f_but_tabghe)
        e_adddaste.pack(side=tk.TOP)

        def add():
            try:
                t_dasteh.insert("", 'end', iid=e_adddaste.get(),
                                text=e_adddaste.get())
            except Exception as identifier:
                e_adddaste.focus()
        b_adddaste["command"] = add
        b_adddaste.pack(side=tk.RIGHT)

        self.i_minus = tk.PhotoImage(file=self.resource["minus"])
        b_deldaste = tk.Button(f_but_tabghe, image=self.i_minus)
        def delete():
            try:
                t_dasteh.delete(
                    t_dasteh.selection())
            except Exception as identifier:
                mb.showerror("خطا","لطفا يکي از دسته ها را انتخاب کنيد")
        b_deldaste.pack()
        b_deldaste["command"] = delete 
        
        f_Kala = tk.LabelFrame(self, text="مشخصات کالا")
        f_Kala.pack(side = tk.RIGHT,fill=tk.BOTH)
        l_namekala = tk.Label(f_Kala,text="نام کالا")
        l_namekala.grid(row = 0 , column = 1)
        e_namekala = tk.Entry(f_Kala)
        e_namekala.grid(row = 0 , column = 0)
       
        l_tedadkala = tk.Label(f_Kala,text="تعداد کالا")
        l_tedadkala.grid(row = 1 , column = 1)
        
        s_tedadkala = tk.Spinbox(f_Kala,to = 100)
        s_tedadkala["from"]=1
        s_tedadkala.grid(row = 1 , column = 0)
        
        b_addkala = tk.Button(f_Kala,text = "اضافه کردن کالا")
        def addkala():
            if(e_namekala.get() == ""):
                mb.showerror("خطا","نام کالا را وارد کنيد")
            elif(t_dasteh.selection() == ()):
                mb.showerror("خطا","لطفا يکي از دسته ها را انتخاب کنيد")
            else:
                t_dasteh.insert(t_dasteh.selection(), 'end',text=e_namekala.get())
        b_addkala["command"] = addkala
        b_addkala.grid(row = 2)
        
        tk.Frame(self,widt=400).pack(side = tk.r,fill=tk.BOTH)

        