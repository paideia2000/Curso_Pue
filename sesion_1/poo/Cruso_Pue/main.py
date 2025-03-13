"""
Crea una clase base Empleado que tenga atributos nombre y salario, 
y un método mostrar_info que muestre esta información. 
Luego, define una clase derivada Gerente que añada el atributo departamento. 
Esta clase debe sobrescribir el método mostrar_info para mostrar 
también el departamento. 
Finalmente, crea una instancia de Gerente y muestra su información.
"""


class Employee:
    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = salary
    
    def show_info(self) -> str:
        return f"The name is: {self._name}, the salary is: {self._salary:.2f}$"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department
    
    def show_info(self) -> str:
        """ show data of the user plus, their department """
        return super().show_info() + f", the department is: {self._department}."

def see_data_manager(manager: Manager) -> str:
    """ show data of the manager """
    
    if isinstance(manager, Manager):
        return manager.show_info()
    else:
        print(f"¡ERROR! The argumet {manager} mut be instance of 'Manager'.")

def main():
    
    manager = Manager("Rene Medina", 650.04, "Depuration")
    print("\n",see_data_manager(manager),"\n")
    
if __name__=="__main__":
    main()
    
