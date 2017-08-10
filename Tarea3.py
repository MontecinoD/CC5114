import matplotlib.pyplot as plt
import random
import numpy as np

def sigmoid(x):
    return 1.0/(1+np.exp(x))

class perceptron:
    def __init__(self, w,bias, sigmo = False):
        self.w = w    # lista de pesos
        self.b = bias # bias
        self.sigmoid = sigmo
        
    def setWeights(self,w):
        self.w = w
    
    def setBias(self,bias):
        self.b = bias
    
    def output(self,x):
        try:
            suma = self.b
            for i in range(len(x)):
                suma += x[i]*self.w[i]
            if(self.sigmoid):
                return sigmoid(suma)
            else:
                return int(suma>0)
        except IndexError:
            print "La entrada debe tener",len(self.w),"elementos"
            
    def Train(self, data, target, ciclos=100, C=0.1):
        correct_ans_per_cicle =[]
        for k in range(ciclos):
            count = 0.0
            for i in range(len(data)):
                answ = self.output(data[i])
                if(self.sigmoid):
                    if(target[i]==(answ<0.5)):
                        count += 1.0
                    self.b += -C*2*(answ-target[i])*answ*(1-answ)
                    self.w += -C*2*(answ-target[i])*answ*(1-answ)*data[i]
                        
                else:
                    if(target[i]==answ):
                        count += 1.0
                        continue
                    else: 
                        self.b += C*((-1.0)**answ)
                        self.w += C*((-1.0)**answ)*data[i]
            correct_ans_per_cicle += [count]
        return np.asarray(correct_ans_per_cicle)

''' Clases OR, AND y NAND para test
import unittest

class OR(perceptron):
    
    def __init__(self):
        self.w = [2,2]
        self.b = -1
        self.sigmoid = True
        
class AND(perceptron):
    
    def __init__(self):
        self.w = [2,2]
        self.b = -3
        self.sigmoid = True
        
class NAND(perceptron):
    
    def __init__(self):
        self.w = [-2,-2]
        self.b = 3
        self.sigmoid = True
        

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
     
    def tearDown(self):
        del self.input
        
if __name__=="__main__":
    unittest.main()
'''    
    
    
    
#definicion de la funcion a estimar
def func(x):
    return 3*x-4

#Grafico del estado del perceptron
def Graficar(data,perceptron, th=0.5, titulo=""):
    up = []
    down = []
    for example in data:
        if(perceptron.output(example)>th):
            up += [example]
        else:
            down += [example]
            
    up = np.asarray(up)
    down = np.asarray(down)
    x= np.linspace(-10,10,100)
    y = func(x)
    fig, ax = plt.subplots()
    ax.scatter(up[:,0],up[:,1],marker="o",color='r')
    ax.scatter(down[:,0],down[:,1],marker="o",color='b')
    ax.plot(x,y,'k', label="f(x) = 3*x-4")
    ax.legend()
    ax.grid()
    plt.title(titulo)
    plt.show()
    

print "Estimacion mediante un perceptron sigmoide de la funcion f(x) = 3x -4"
print "."
print "Los pesos y el bias del perceptron seran iniciados al azar\n"

#Generacin de datos aleatorios y su clasificacion segun func(x)
n_ejemplos = input("Ingrese el numero de ejemplos del dataset: ")
ciclos = input("Ingrese numero de ciclos que se entrenara usando el set de ejemplos: ")
C = input("Ingrese el valor C: ")
print "\nnota: los graficos se realizaron usando un set distinto al del entrenamiento, con 500 ejemplos"
    
# inicializamos el perceptron con pesos aleatorios
w = np.random.uniform(-1,1,2)
bias = np.random.uniform(-1,1)
perc = perceptron(w,bias,sigmo=True)

data = np.random.uniform(-10,10,(n_ejemplos,2))
data_graph = np.random.uniform(-10,10,(500,2))
target = func(data[:,0])<data[:,1]

#Graficamos estado inicial
Graficar(data_graph,perc, th=0.5, titulo="Estado inicial")

# Entrenamiento del perceptron
counts = perc.Train( data, target, ciclos, C)

#Graficamos estado actual
Graficar(data_graph,perc, th=0.5, titulo = "Despues del entrenamiento")

#Graficamos la evolucion de las respuestas correctas en cada ciclo
fig, ax = plt.subplots()
ax.plot(np.linspace(1,len(counts),len(counts)),counts/n_ejemplos)
plt.xlabel("ciclos")
plt.ylabel("% de aciertos")
plt.title("Curva de aprendizaje")
plt.grid()
plt.show()
