from tinydb import TinyDB, Query
import os


class Resource:
    __db = TinyDB('res/db.json')
    # name,path
    __resource = __db.table("Resource")
    def __init__(self):
        self.update_resource()
    def update_resource(self):
        for d in os.listdir('res'):
            ds = d.split('.')
            name = ds[0]
            ext = ds[1]
            if (self.__resource.get(Query().name == name ) == None) & (name != 'db' ):
                self.__resource.insert({"name": name, "path": 'res/'+d})
    def __getitem__(self, name):
        return self.__resource.get(Query().name == name)['path']
