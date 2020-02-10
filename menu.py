from pymongodb import Mongo

class Menu():
    def __init__(self):
        self.__empleado = Mongo()
        

    def Empleados(self):
        firstname = input('First Name: ')
        lastname = input('Last Name: ')
        age = input('Age: ')
        sex = input ("Sex (M/F) :  ")
        self.__empleado.insert_one_employee(firstname,lastname,age,sex)
    
    def menuu(self):
        print("-----MAIN-----")
        print("1) Insert Employee")
        print("2) Update Employee")
        print("3) Delete Employee")
        print("4) Exit")

        option = input("Choose an option: ")

        if(option == '1'):
            self.Empleados()
            self.__empleado.cerrarConexion()
            print("Employee Added")
            self.menuu()

        if(option == '2'):
            self.__empleado.update_employee()
            self.__empleado.cerrarConexion()
            print("Employee Updated")
            self.menuu()

        if(option == '3'):
            self.__empleado.delete_employee()
            self.__empleado.cerrarConexion()
            print("Employee Deleted")
            self.menuu()

            
