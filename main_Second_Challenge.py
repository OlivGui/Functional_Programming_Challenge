from abc import ABC
from abc import abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    @abstractmethod
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        """
        Function to calculate the salary bonus
        """
        pass

    def get_hours(self):
        """
        Function to fix the work hour of each employee
        """    
        self.hours = 8
        return self.hours 
    
    def get_departament(self):
        """
        Get method to get departament
        """    
        return self._departament.name

    def set_departament(self, name, code):
        """
        Set method to set department
        """
        self._departament = Department(name, code)    


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        """
        Function to calculate the salary bonus
        """        
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self.__sales = 0

    def get_sales(self):
        """
        Get method to get amount of sales
        """
        return self.__sales

    def put_sales(self, value):
        """
        Put method to increase amount of sales
        """
        self.__sales += value

    def calc_bonus(self):
        """
        Function to calculate the salary bonus
        """            
        return self.__sales * 0.15
