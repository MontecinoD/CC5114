import matplotlib.pyplot as plt
import random
import numpy as np

class perceptron:
    def __init__(self, w,bias):
        self.w = w    # lista de pesos
        self.b = bias # bias
        
    def setWeights(self,w):
        self.w = w
    
    def setBias(self,bias):
        self.b = bias
    
    def output(self,x):
        try:
            suma = self.b
            for i in range(len(x)):
                suma += x[i]*self.w[i]
            return int(suma>0)
        except IndexError:
            print "La entrada debe tener",len(self.w),"elementos"
            
    def Train(self, data, target, ciclos=100, C=0.1):
        correct_ans_per_cicle =[]
        for k in range(ciclos):
            count = 0.0
            for i in range(len(data)):
                answ = self.output(data[i])
                if(target[i]==answ):
                    count += 1.0
                    continue
                else: 
                    self.b += C*((-1.0)**answ)
                    self.w = self.w + C*((-1.0)**answ)*data[i]
            correct_ans_per_cicle += [count]
        return np.asarray(correct_ans_per_cicle)

    
    
print "Estimacion mediante un perceptron de la funcion f(x) = 3x -4"
print "."
print "Los pesos y el bias del perceptron seran iniciados al azar\n"

    
#definicion de la funcion a estimar
def func(x):
    return 3*x-4

#Generacin de datos aleatorios y su clasificacion segun func(x)
n_ejemplos = input("Ingrese el numero de ejemplos del dataset: ")
ciclos = input("Ingrese numero de ciclos que se entrenara usando el set de ejemplos: ")
C = input("Ingrese el valor C: ")
print "\nnota: los graficos se realizaron usando un set distinto al del entrenamiento, con 500 ejemplos"

data = np.random.uniform(-10,10,(n_ejemplos,2))
data_graph = np.random.uniform(-10,10,(500,2))
target = func(data[:,0])<data[:,1]

#Grafico del estado del perceptron
def Graficar(data,perceptron,titulo=""):
    up = []
    down = []
    for example in data:
        if(perceptron.output(example)):
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

# inicializamos el perceptron con pesos aleatorios
w = np.random.random(2)
bias = np.random.random()
perc = perceptron(w,bias)

#Graficamos estado inicial
Graficar(data_graph,perc,titulo="Estado inicial")

# Entrenamiento del perceptron
counts = perc.Train( data, target, ciclos, C)

#Graficamos estado actual
Graficar(data_graph,perc, titulo = "Despues del entrenamiento")

#Graficamos la evolucion de las respuestas correctas en cada ciclo
fig, ax = plt.subplots()
ax.plot(np.linspace(1,len(counts),len(counts)),counts/n_ejemplos)
plt.xlabel("ciclos")
plt.ylabel("% de aciertos")
plt.title("Curva de aprendizaje")
plt.grid()
plt.show()
print "nota2: la curva de apendizaje es con respecto al set de entrenamiento"
print "nota3: un 100% de acierto en el set de entrenamiento no implica una correcta estimacin de f, ya que los ejemplos pueden no ser suficientes" 