import unittest

from main import Employee, Manager, see_data_manager


class Test_ClassEmployee(unittest.TestCase):
    
    def test_show_data_user(self):
        """ check that magic method returned a string with the format we want. """
        employee = Employee("Rene Medina", 650.04)
        get_output = employee.show_info()
        self.assertRegex(get_output, r'^The name is: [A-Za-z ]+, the salary is: \d{3,}+\.\d{2,}\$')

class Test_ClassManager(unittest.TestCase):
    
    def test_show_info_user(self):
        """ check that (show_info) method returned a string with the format we want. """
        manager = Manager("Rene Medina", 650.04, "Depuration")
        get_output = manager.show_info()
        self.assertIsInstance(get_output, str)

class Test_FuncSeeDataManager(unittest.TestCase):
    
    def test_func_returned_data_manager(self):
        """ check the data when the function returned the data of the manager """
        manager = Manager("Rene Medina", 650.04, "Depuration")
        output = see_data_manager(manager)
        self.assertEqual(output, r'The name is: Rene Medina, the salary is: 650.04$, the department is: Depuration.')

if __name__=="__main__":
    unittest.main()
    


