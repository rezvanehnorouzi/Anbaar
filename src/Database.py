from tinydb import TinyDB, where
import os


class Database:
    _db = TinyDB('res/db.json')
class Resource(Database):
    # name,path
    def __init__(self):
        self.__resource = super()._db.table("Resource")
        self.update_resource()

    def update_resource(self):
        for d in os.listdir('res'):
            ds = d.split('.')
            name = ds[0]
            if (self.__resource.get(where("name") == name) == None) & (name != 'db'):
                self.__resource.insert({"name": name, "path": 'res/'+d})

    def __getitem__(self, name):
        return self.__resource.get(where("name") == name)['path']


class User(Database):
    def __init__(self):
        self.__users = super()._db.table("Users")
    def get(self,name):
        return self.__users.get(where("name") == name)
    def add(self, name, password, type):
        self.__users.insert({"name": name, "password": password, "type": type})
    def remove(self,name):
        self.__users.remove(where("name") == name)

class Kala(Database):
    def __init__(self):
        self.__prop = super()._db.table("Prop")
        self.kalaha = super()._db.table("Kalaha")

    def get_dasteha(self):
        dasteha = []
        for dic in self.__prop.all():
            dasteha.append(dic["dasteh"])
        return dasteha

    def add_dasteh(self, name):
        self.__prop.insert({"dasteh": name})

    def del_dasteh(self, name):
        self.__prop.remove(where("dasteh") == name)
        self.kalaha.remove(where("dasteh") == name)
