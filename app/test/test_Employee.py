import unittest
from E import E


class TestEmployee(unittest.TestCase):

    # When a setUp() method is defined, 
    # the test runner will run that method prior to each test. 
    # Likewise, if a tearDown() method is defined,
    #  the test runner will invoke that method after each test.

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_email(self):
        emp_1 = E('Tanveer','Ansari', 50000)
        emp_2 = E('Dilnawaz','Haider',60000)

        self.assertEqual(emp_1.email, 'Tanveer.Ansari@email.com')
        self.assertEqual(emp_2.email, 'Dilnawaz.Haider@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jahn'


        self.assertEqual(emp_1.email,'John.Ansari@email.com')
        self.assertEqual(emp_2.email,'Jahn.Haider@email.com')

    def test_fullname(self):
        emp_1 = E('Tanveer','Ansari', 50000)
        emp_2 = E('Dilnawaz', 'Haider', 60000)

        self.assertEqual(emp_1.fullname, 'Tanveer Ansari')
        self.assertEqual(emp_2.fullname, 'Dilnawaz Haider')

        emp_1.last = 'Kumar'
        emp_2.last = 'Shah'

        self.assertEqual(emp_1.fullname, 'Tanveer Kumar')
        self.assertEqual(emp_2.fullname,'Dilnawaz Shah')

    def test_apply_raise(self):
        emp_1 = E('Tanveer','Ansari',50000)
        emp_2 = E('Dilnawaz', 'Haider',60000)


        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay,52500)
        self.assertEqual(emp_2.pay,63000)

if __name__ == '__main__':
    unittest.main()




