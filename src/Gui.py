import abc
import tkinter as tk
import tkinter.messagebox as mb
from base64 import b85decode, b85encode
from enum import Enum
from tkinter import Tk
from tkinter.ttk import Combobox, Treeview

from Database import Kala, Resource, User, where


class Level(Enum):
    Admin = "مدیر"
    Standard = "معمولی"
    Allname = ["Admin", "Standard"]
    Allvalue = [Admin, Standard]


class Panel(Tk):
    resource = Resource()
    user = User()

    def __init__(self):
        super().__init__()
        self.top = self.winfo_toplevel()
        self.screencenter = (self.winfo_screenwidth()/2,
                             self.winfo_screenheight()/2)
        self.title("انبار دار")
        self.widget()
        self.update_idletasks()
        self.size = tuple(int(_)
                          for _ in self.geometry().split('+')[0].split('x'))
        self.geometry("+%d+%d" % (self.screencenter[0]-self.size[0]/2,
                                  self.screencenter[1]-self.size[1]/2))

    @abc.abstractmethod
    def widget(self):
        pass


class Wellcome(Panel):
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
        e_password = tk.Entry(f_data, show="*")
        e_password.grid(column=0, row=1)

        f_butt = tk.Frame(self)
        f_butt.pack()

        b_vorod = tk.Button(f_butt, text="ورود", padx=30)

        def vorod():
            try:
                q = self.user.get(e_username.get())
                password = str(b85decode(bytearray.fromhex(
                    q["password"]).decode()), encoding="utf-8")
                if password == e_password.get():
                    if q["type"] == Level.Admin.name:
                        self.destroy()
                        Main(True)
                    elif e_username.get() == "user":
                        self.destroy()
                        Main(False)
                else:
                    mb.showerror(
                        title="خطا", message="رمز عبور اشتباه است")
            except Exception:
                mb.showerror(
                    title="خطا", message="نام کاربری اشتباه است")
        b_vorod["command"] = vorod
        b_vorod.grid(column=1, row=2, sticky=tk.NSEW)
        b_khroj = tk.Button(f_butt, text="خروج", padx=30)
        b_khroj["command"] = lambda: (self.destroy(), exit())
        b_khroj.grid(column=0, row=2, sticky=tk.NSEW)


class AddUser(Panel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("افزودن کاربر")

    def widget(self):
        # username
        l_username = tk.Label(self, text="نام کاربری")
        l_username.grid(column=1, row=0)
        e_username = tk.Entry(self)
        e_username.grid(column=0, row=0)
        # password
        l_password = tk.Label(self, text="رمز عبور")
        l_password.grid(column=1, row=1)
        e_password = tk.Entry(self)
        e_password.grid(column=0, row=1)
        # level
        l_level = tk.Label(self, text="سطح کاربری")
        l_level.grid(column=1, row=2)
        lb_level = Combobox(self, values=Level.Allvalue.value)
        lb_level.set(Level.Standard.value)
        lb_level.grid(column=0, row=2)

        b_add = tk.Button(self, text="افزودن", width=20)

        def add():
            if e_username.get() != "":
                self.user.add(
                    e_username.get(),
                    b85encode(bytes(e_password.get(), encoding="utf-8")).hex(),
                    Level.Allname.value[lb_level.current()]),
                self.destroy()
            else:
                e_username.focus()
        b_add["command"] = add
        b_add.grid(column=1, row=3, sticky=tk.NSEW)
        b_laghv = tk.Button(self, text="لغو")
        b_laghv["command"] = self.destroy
        b_laghv.grid(column=0, row=3, sticky=tk.NSEW)


class RemoveUser(Panel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("حذف کاربر")

    def widget(self):
        # username
        l_username = tk.Label(self, text="نام کاربری")
        l_username.grid(column=1, row=0)
        e_username = tk.Entry(self)
        e_username.grid(column=0, row=0)

        b_remove = tk.Button(self, text="حذف", width=20)

        def remove():
            if e_username.get() != "":
                # self.user.
                self.destroy()
        b_remove["command"] = remove
        b_remove.grid(column=1, row=2, sticky=tk.NSEW)
        b_laghv = tk.Button(self, text="لغو")
        b_laghv["command"] = self.destroy
        b_laghv.grid(column=0, row=2, sticky=tk.NSEW)


class ChengeUser(Panel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("تغییر رمز")

    def widget(self):
        # oldusername
        l_olduser = tk.Label(self, text="نام کاربری قبلی")
        l_olduser.grid(column=1, row=0)
        e_olduser = tk.Entry(self)
        e_olduser.grid(column=0, row=0)
        # newusername
        l_newuser = tk.Label(self, text="نام کاربری جدید")
        l_newuser.grid(column=1, row=0)
        e_newuser = tk.Entry(self)
        e_newuser.grid(column=0, row=0)

        b_chenge = tk.Button(self, text="تغییر", width=20)
        b_chenge.grid(column=1, row=2, sticky=tk.NSEW)
        b_laghv = tk.Button(self, text="لغو")
        b_laghv["command"] = self.destroy
        b_laghv.grid(column=0, row=2, sticky=tk.NSEW)


class ChengePassword(Panel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("تغییر رمز")

    def widget(self):
        # username
        l_username = tk.Label(self, text="نام کاربری")
        l_username.grid(column=1, row=0)
        e_username = tk.Entry(self)
        e_username.grid(column=0, row=0)
        # newpassword
        l_password = tk.Label(self, text="رمز عبور جدید")
        l_password.grid(column=1, row=1)
        e_password = tk.Entry(self)
        e_password.grid(column=0, row=1)

        b_chenge = tk.Button(self, text="تغییر", width=20)

        b_chenge.grid(column=1, row=2, sticky=tk.NSEW)
        b_laghv = tk.Button(self, text="لغو")
        b_laghv["command"] = self.destroy
        b_laghv.grid(column=0, row=2, sticky=tk.NSEW)


class Main(Panel):
    kala = Kala()

    def __init__(self, isadmin):
        self.__isadmin = isadmin
        super().__init__()

    def widget(self):
        m_bar = tk.Menu(self.top)
        self.top['menu'] = m_bar

        m_file = tk.Menu(m_bar, tearoff=False)
        subbackup = tk.Menu(m_file, tearoff=False)
        subbackup.add_command(label="ذخیره")
        m_file.add_cascade(label='بکاپ', menu=subbackup)
        m_file.add_command(label="خروج", command=exit)
        m_bar.add_cascade(label='فایل', menu=m_file)
        subusers = tk.Menu(m_bar, tearoff=False)
        subusers.add_command(label="افزودن", command=AddUser)
        subusers.add_command(label="حذف", command=RemoveUser)
        subusers.add_command(label="تغییر نام کاربری", command=ChengeUser)
        subusers.add_command(label="تغییر رمز", command=ChengePassword)
        if self.__isadmin:
            m_bar.add_cascade(label='کاربری', menu=subusers)
            subbackup.add_command(label="بارگزاری")

        f_top = tk.LabelFrame(self)
        f_down = tk.LabelFrame(self)
        f_top.pack(fill=tk.BOTH)
        f_top.grid_anchor(tk.NE)
        f_down.pack(fill=tk.BOTH, expand=1)

        f_tabaghe = tk.Frame(f_top)
        f_tabaghe.grid(row=0, column=2, sticky=tk.NSEW)

        f_list_tabghe = tk.Frame(f_tabaghe)
        f_list_tabghe.pack()

        l_dasteh = tk.Label(f_list_tabghe, text="دسته بندی")
        l_dasteh.pack()
        lb_dasteh = tk.Listbox(
            f_list_tabghe, activestyle=tk.NONE, selectmode=tk.SINGLE)
        for dasteh in self.kala.get_dasteha():
            lb_dasteh.insert(tk.END, dasteh)
        lb_dasteh.pack()

        f_but_tabghe = tk.Frame(f_tabaghe)
        f_but_tabghe.pack()

        self.i_plus = tk.PhotoImage(file=self.resource["plus"])
        b_adddaste = tk.Button(f_but_tabghe, image=self.i_plus)
        e_adddaste = tk.Entry(f_but_tabghe)
        e_adddaste.pack(side=tk.TOP)

        def add_dasteh():
            if e_adddaste.get() != "":
                lb_dasteh.insert(tk.END, e_adddaste.get())
                self.kala.add_dasteh(e_adddaste.get())
                e_adddaste.delete(0, len(e_adddaste.get()))
            else:
                e_adddaste.focus()
        b_adddaste["command"] = add_dasteh
        b_adddaste.pack(side=tk.RIGHT)

        self.i_minus = tk.PhotoImage(file=self.resource["minus"])
        b_deldaste = tk.Button(f_but_tabghe, image=self.i_minus)

        def delete():
            if lb_dasteh.curselection() != ():
                self.kala.del_dasteh(lb_dasteh.get(tk.ACTIVE))
                lb_dasteh.delete(tk.ACTIVE)
            else:
                mb.showerror("خطا", "لطفا يکي از دسته ها را انتخاب کنيد")
        b_deldaste.pack()
        b_deldaste["command"] = delete

        f_kala = tk.LabelFrame(f_top, text="مشخصات کالا", labelanchor=tk.N)
        f_kala.grid(row=0, column=1, sticky=tk.NSEW)

        l_namekala = tk.Label(f_kala, text="نام کالا")
        l_namekala.grid(row=0, column=1)
        e_namekala = tk.Entry(f_kala)
        e_namekala.grid(row=0, column=0)

        l_tedadkala = tk.Label(f_kala, text="تعداد کالا")
        l_tedadkala.grid(row=1, column=1)

        s_tedadkala = tk.Spinbox(f_kala, to=100)
        s_tedadkala["from"] = 1
        s_tedadkala.grid(row=1, column=0)

        b_addkala = tk.Button(f_kala, text="اضافه کردن کالا")
        v_plan = tk.StringVar(self, "A1")

        def add_kala():
            if(e_namekala.get() == ""):
                mb.showerror("خطا", "نام کالا را وارد کنيد")
            elif(lb_dasteh.curselection() == ()):
                mb.showerror("خطا", "لطفا يکي از دسته ها را انتخاب کنيد")
            else:
                self.kala.kalaha.insert(
                    {"mahal": v_plan.get(),
                     "num": s_tedadkala.get(),
                     "name": e_namekala.get(),
                     "dasteh": lb_dasteh.get(tk.ACTIVE)})
        b_addkala["command"] = add_kala
        b_addkala.grid(row=3)

        f_plan = tk.LabelFrame(f_top)
        f_plan.grid(row=0, column=0, sticky=tk.NSEW)
        self.i_plan = tk.PhotoImage(file=self.resource["plan"])
        l_plan = tk.Label(f_plan, image=self.i_plan)
        l_plan.pack()
        radif = ['A', 'B', 'C', 'D']
        for x in range(4):
            l = tk.Label(f_plan, text=radif[x])
            l.place(x=(x*92)+50, y=10)
            for y in range(8):
                rb = tk.Radiobutton(f_plan, variable=v_plan,
                                    value=str(radif[x])+str(y+1),
                                    background="red")
                rb.place(x=(x*92)+40, y=(y*36)+35)

        t_infokala = Treeview(f_down, show="headings")
        t_infokala["columns"] = ["mahal", "num", "name"]
        t_infokala.heading("name", text="نام")
        t_infokala.heading("num", text="تعداد")
        t_infokala.heading("mahal", text="محل کالا")

        def datagrid(event):
            try:
                t_infokala.delete(*t_infokala.get_children())
                for kala in self.kala.kalaha.search(
                        where("dasteh") == lb_dasteh.selection_get()):
                    t_infokala.insert("", tk.END, values=list(kala.values()))
            except Exception:
                pass
        lb_dasteh.bind('<ButtonRelease>', datagrid)
        t_infokala.grid(row=0, column=0, sticky=tk.NSEW)
        f_down.grid_columnconfigure(0, weight=1)
        f_down.grid_rowconfigure(0, weight=1)
        sb_infokala = tk.Scrollbar(f_down)
        sb_infokala["command"] = t_infokala.yview
        sb_infokala.grid(row=0, column=0, sticky=tk.E)
