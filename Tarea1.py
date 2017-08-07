import unittest

class perceptron:
    def __init__(self, w,bias):
        self.w = w    # lista de pesos
        self.b = bias # bias
        
    def setWeights(self,w,bias):
        self.w = w
        self.b = bias
    
    def output(self,x):
        try:
            suma = self.b
            for i in range(len(x)):
                suma += x[i]*self.w[i]
            return int(suma>0)
        except IndexError:
            print "La entrada debe tener",len(self.w),"elementos"

    
class OR(perceptron):
    
    def __init__(self):
        self.w = [2,2]
        self.b = -1
        
class AND(perceptron):
    
    def __init__(self):
        self.w = [2,2]
        self.b = -3
        
class NAND(perceptron):
    
    def __init__(self):
        self.w = [-2,-2]
        self.b = 3
        
class sum_Gate:
    
    def __init__(self):
        pass
    
    def output(self,x1,x2):
        nand = NAND()
        an = AND()
        n1 = nand.output([x1,x2])
        n2 = nand.output([x1,n1])
        n3 = nand.output([n1,x2])
        suma = nand.output([n2,n3])
        carry = an.output([x1,x2])
        return (suma,carry) 
        
    
'''Comienzo del test'''

class Test(unittest.TestCase):
    
    def setUp(self):
        self.input = [(0,0), (0,1), (1,0), (1,1)]
    
    def test_OR(self):
        or_ = OR()
        correct_ans = [0,1,1,1]
        output = [or_.output(x) for x in self.input]
        self.assertEqual(output,correct_ans)
        
    def test_AND(self):
        and_ = AND()
        correct_ans = [0,0,0,1]
        output = [and_.output(x) for x in self.input]
        self.assertEqual(output,correct_ans)
        
    def test_NAND(self):
        nand_ = NAND()
        correct_ans = [1,1,1,0]
        output = [nand_.output(x) for x in self.input]
        self.assertEqual(output,correct_ans)
        
    def test_sum_Gate(self):
        sumG = sum_Gate()
        correct_ans = [(0,0), (1,0), (1,0), (0,1)]
        output = [sumG.output(x1,x2) for (x1,x2) in self.input]
        self.assertEqual(output,correct_ans)
     
    def tearDown(self):
        del self.input
        
if __name__=="__main__":
    unittest.main()
    
