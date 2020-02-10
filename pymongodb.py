from pymongo import MongoClient

class Mongo():
    def __init__(self):
        self.__MONGO_URI = 'mongodb://uttics.com:27027'
        self.__client = MongoClient(self.__MONGO_URI)
        self.db = self.__client['Marentes']
        self.collection_employees = self.db['employees']

    def insert_one_employee(self,first_name,last_name,age,sex):
        self.collection_employees.insert_one({
            "_id":self.collection_employees.count()+1,
            "first_name": first_name,
            "last_name": last_name,
            "age": age, 
            "sex": sex
        })

    def update_employee(self):
        _id = input('ID to Update: ')
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        age = input('Age: ')
        self.collection_employees.update_one({"_id" :int(_id) },{"$set" : {"first_name" : first_name,"last_name" : last_name,"age" : age}})
    
    def delete_employee(self):
        _id = input('ID to Delete: ')
        self.collection_employees.remove({"_id": int(_id)})


    def cerrarConexion(self):
        self.__client.close()