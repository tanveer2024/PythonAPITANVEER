import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):        # def is a method definition
       # result = calc.add(10,5)
        self.assertEqual( calc.add(10,5),15) # correct
        self.assertEqual( calc.add(2,2),4)  # correct
        self.assertEqual( calc.add(4,2),6) # wrong
        self.assertEqual( calc.add(5,5),10) # correct
        
    def test_subtract(self):        # def is a method definition subtract
       # result = calc.add(10,5)
        self.assertEqual( calc.subtract(10,5),5) # correct
        self.assertEqual( calc.subtract(2,2),0) # correct
        self.assertEqual( calc.subtract(2,2),0) # correct
        self.assertEqual( calc.subtract(4,2),2) # correct
        self.assertEqual( calc.subtract(5,5),0) # correct

    def test_multiply(self):        # def is a method definition
       # result = calc.add(10,5)
        self.assertEqual( calc.multiply(10,5),50) #correct
        self.assertEqual( calc.multiply(2,2),4) # correct
        self.assertEqual( calc.multiply(4,2),8) # correct
        self.assertEqual( calc.multiply(5,5),25) # correct

    def test_divide(self):        # def is a method definition
       # result = calc.add(10,5)
        self.assertEqual( calc.divide(10,5),2) # correct
        self.assertEqual( calc.divide(10,2),5) # error
        self.assertEqual( calc.divide(4,2),2) # correct
        self.assertEqual( calc.divide(2, 2),1) # wrong           


        # self.assertRaises(ValueError, calc.divide,10,2)
################################################################################
    # self represents the instance of the class.
    # By using the “self” keyword we can access the attributes and methods of the class in python.
    # It binds the attributes with the given arguments. 
    # The reason you need to use self. is because Python does 
    # not use the @ syntax to refer to instance attributes   
###################################################################################
#  A context manager usually takes care of setting up some resource, 
#  e.g. opening a connection, and
#  automatically handles the clean up when we are done with it.
###########################################################################
# Python programming provides us with a built-in @property 
# decorator which makes usage of getter and setters much easier 
# in Object-Oriented Programming.




################################################################################

        with self.assertRaises(ValueError):  # context manager
           calc.divide(10,0)

if  __name__ == '__main__':
    unittest.main() 
      