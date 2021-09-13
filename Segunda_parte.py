"""En mi codigo el algoritmo astar recorre una matriz de 0s y 1s,
donde los 1 representan obstaculos y retorna un camino,
por eso antes de poner la matriz como parametro de la funcion astar 
convierto la matriz en una matriz de 0s y 1s"""


from math import sqrt
import random

#inicializamos la matriz
m = []
for i in range(32):
    m.append(["  "] * 32)

def draw_canvas_empty():
  """Inicializa los bordes de la cuadricula de 30*30 en la 
  matriz principal."""

  for j in range(32):
    m[j][0] = '| '
    m[j][31] = '| '
  for i in range(32):
    m[0][i] = '- '
    m[31][i] = '- '

def dibujar(m):
  """Sirve para imprimir una matriz de manera ordenada.
  Tiene como parametro una matriz."""

  for i in m:
    for j in i:
      print(j,end="")
    print()
  
def ok1(x,y,a,b):
  """
  Verifica si en donde queremos poner las paredes de un espacio las casillas estan vacias y 
  si los alrededores de las paredes tambien estan vacias, ya que asi cumpliria que los espacios 
  esten separados en por lo menos 1 casilla.
  Tiene como parametros la coordenada de donde empiezo a dibujar el espacio(rectangulo) y
  las dimensiones del espacio.
  Retorna False o True segun se cumpla lo anterior mencionado.
  """
  ok=True
  if x-1<2 or y-1<2 or x+a>29 or y+b>29: ok=False
  else:
    for k in range(0,b,1):
      if m[x-1][y+k]!="  " or m[x+a][y+k]!="  ": ok=False
    for k in range(-1,a+1,1):
      if m[x+k][y-1]!="  " or m[x+k][y+b]!="  ": ok=False
    
    for k in range(-1,b+1,1):
      if m[x-2][y+k]!="  " or m[x+a+2][y+k]!="  ": ok=False
    for k in range(-2,a+2,1):
      if m[x+k][y-2]!="  " or m[x+k][y+b+1]!="  ": ok=False

  return ok

espacios=[]

def init_places(espacios):
  """Iniciamos las posiciones de las entradas de los espacios al mismo 
  tiempo que generamos los espacios como rectangulos de tal manera que
  no se intersecten.
  Recibe como parametro una lista en donde guardaremos las coordenadas
  de las entradas de los espacios que utilizaremos luego."""

  j=1
  c=[]
  for i in range(6):
    uwu=True
    while uwu:
      x = random.randint(2, 28)
      y = random.randint(2, 28)
      c.append(random.randint(10,15))
      for i in range(int(sqrt(c[j-1])),c[j-1]+1):
        if c[j-1]%i==0 and ok1(x,y,i,c[j-1]//i):
          for k in range(0,c[j-1]//i,1):
            m[x-1][y+k] = '- '
            m[x+i][y+k]= '- '
          for k in range(-1,i+1,1):
            m[x+k][y-1] = '| '
            m[x+k][y+(c[j-1]//i)] = '| '
          uwu=False
          break
      if uwu: c.pop()
    m[x-1][y] = 'E'+str(j)
    espacios.append((x-1,y))
    j+=1


def init_players(tripulantes):
  """Iniciamos las posiciones de los tripulantes de manera random.
  Tiene como parametro una lista en donde guardaremos las coordenadas
  de los tripulantes que utilizaremos luego."""

  t1 = [random.randint(1, 29), random.randint(1, 29)]
  while(m[t1[0]][t1[1]]!="  "):
    t1 = [random.randint(1, 29), random.randint(1, 29)]
  m[t1[0]][t1[1]] = "t1"
  tripulantes.append((t1[0],t1[1]))
  t2 = [random.randint(1, 29), random.randint(1, 29)]
  while  m[t2[0]][t2[1]] != "  ":
    t2 = [random.randint(1, 29), random.randint(1, 29)]
  m[t2[0]][t2[1]] = "t2"
  tripulantes.append((t2[0],t2[1]))
  t3 = [random.randint(1, 29), random.randint(1, 29)]
  while m[t3[0]][t3[1]] != "  ":
    t3 = [random.randint(1, 29), random.randint(1, 29)]
  m[t3[0]][t3[1]] = "t3"
  tripulantes.append((t3[0],t3[1]))
  t4 = [random.randint(1, 29), random.randint(1, 29)]
  while  m[t4[0]][t4[1]] != "  ":
    t4 = [random.randint(1, 29), random.randint(1, 29)]
  m[t4[0]][t4[1]] = "t4"
  tripulantes.append((t4[0],t4[1]))


class Node():
    """Clase Node para encontrar un camino cuando utilizamos el algoritmo A*."""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Nos sirve para encontrar un camino desde estar hasta end, teniendo en cuenta
      los obstaculos.
      Tiene como parametros la matriz, una coodenada inicial y una coordenada final.
      Retorna una lista de tuplas(coordenadas) como una ruta desde el inicio
      hasta el final en la cuadricula."""

    #Crear nodo inicial y final
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    #Inicializar tanto la lista abierta como la cerrada
    open_list = []
    closed_list = []

    #Agregar el nodo de inicio
    open_list.append(start_node)

    #Da vueltas hasta que encuentres el final
    while len(open_list) > 0:
        #Obtener el nodo actual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        #Quitar actual de la lista abierta, agregar a la lista cerrada
        open_list.pop(current_index)
        closed_list.append(current_node)

        #Encontre la meta
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #Retorna el camino inverso

        #Generar hijos
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #Casilla adyacente

            #Obtener la posición del nodo
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if Node(current_node, node_position) in closed_list: continue
            #Asegúrese de que esté dentro del rango
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            #Asegúrese de que el terreno sea transitable
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            #Crear nuevo nodo
            new_node = Node(current_node, node_position)

            #adjuntar
            children.append(new_node)
        
        #Bucle a través de los hijos
        for child in children:

            #Su hijo está en la lista cerrada
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            #Cree los valores de f, g y h
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            #Su hijo ya está en la lista abierta
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            #Agregar hijo a la lista abierta 
            open_list.append(child)



def pinta(m,m1):
  """Convierto m1 en una matriz de 0s y 1s segun m(matriz principal), para 
  poder ponerlo en la funcion astar.
  Tiene como parametros m1 y m."""
  for i in range(32):
    for j in range(32):
      if m[i][j]!="  " and m[i][j]!="X ": 
        m1[i][j]=1


tiempo={}
def te(tiempo):
  """Inicializamos el tiempo de espera en cada espacio de manera random."""
  tiempo["E1"]=random.randint(1, 6)
  tiempo["E2"]=random.randint(1, 6)
  tiempo["E3"]=random.randint(1, 6)
  tiempo["E4"]=random.randint(1, 6)
  tiempo["E5"]=random.randint(1, 6)
  tiempo["E6"]=random.randint(1, 6)


while True:
  option=input()
  
  if option=="init":
    m = []
    for i in range(32):
      m.append(["  "] * 32)

    draw_canvas_empty()

    X = [random.randint(1, 29), random.randint(1, 29)]
    m[X[0]][X[1]] = "X "
    x=X[0]
    y=X[1]

    tripulantes=[]
    espacios=[]
    init_places(espacios)
    init_players(tripulantes)

    dibujar(m)
    """Hasta aqui solo inicializa la matriz con los espacios
    y las posiciones de los tripulantes e impostores."""
    option1=input()

    tdi=[]
    tet=[]
    trgi=[]

    if option1=="route":
      tiempo={}
      te(tiempo)

      for k in range(4):
        start=(X[0],X[1])
        end=(tripulantes[k][0],tripulantes[k][1])
        m1 = []
        for i in range(32):
          m1.append([0] * 32)
        """convierto la matriz en 0s y 1s"""
        for i in range(32):
          for j in range(32):
            if m[i][j]=="| " or m[i][j]=="- ":
              m1[i][j]=1
              if k==0 and m[i][j]=="t1": m1[i][j]=0
              elif k==1 and m[i][j]=="t2": m1[i][j]=0
              elif k==2 and m[i][j]=="t3": m1[i][j]=0
              elif k==3 and m[i][j]=="t4": m1[i][j]=0

        path=astar(m1,start,end)
        """Verifico si alguno de los 4 tripulantes esta dentro de algun espacio"""
        ok=False
        tmp=""
        if path!=None:
          for i in path:
            for j in espacios:
              if j==i:
                ok=True
                tmp1=j
                tmp=m[tmp1[0]][tmp1[1]]
                break
        """Si esta dentro de un espacio entonces hallo los tdi y tet"""
        if ok:
          tdi.append((len(path)-1)/10)
          tet.append(tiempo[tmp])
          """Si el tripulante 1 esta dentro de un espacio -> pinto con 1s
            Si el tripulante 2 esta dentro de un espacio -> pinto con 2s
            Si el tripulante 3 esta dentro de un espacio -> pinto con 3s
            Si el tripulante 4 esta dentro de un espacio -> pinto con 4s
            Si se pasa mas de 1 vez por el mismo camino  -> pinto con 0s"""
          for i in range(1,len(path)-1):
            cur=m[path[i][0]][path[i][1]]
            if cur=="  " or cur=="E1" or cur=="E2" or cur=="E3" or cur=="E4" or cur=="E5" or cur=="E6":
              m[path[i][0]][path[i][1]]=str(k+1)+" "
            else:
              m[path[i][0]][path[i][1]]="0 "
      #Hallando los trgi
      n=len(tdi)
      for l in range(n):
        trgi.append(tdi[l]-tet[l])

      dibujar(m)
      option2=input()
      if option2=="trgi":
        ans=float(-1)
        for i in trgi:
          if i<0: continue
          else: ans=max(ans,i)
        if ans==-1: print("los tripulantes siempre se escapan")
        else : print(ans)
