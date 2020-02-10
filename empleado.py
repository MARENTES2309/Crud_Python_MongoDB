class Empleado():
    def __init__(self, first_name,last_name,age,sex):
        self.__first_name = first_name
        self.__last_name = last_name 
        self.__age = 0
        self.__sex = sex

    def getfirstName(self):
        return self.__first_name

    def getlastName(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age

    def getSex(self):
        return self.__sex