from math import sqrt 
import random

m = []
for i in range(32):
    m.append(["  "] * 32)

def draw_canvas_empty():
  for j in range(32):
    m[j][0] = '| '
    m[j][31] = '| '
  for i in range(32):
    m[0][i] = '- '
    m[31][i] = '- '

def dibujar(m):
  for i in m:
    for j in i:
      print(j,end="")
    print()
  
def ok1(x,y,a,b):
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

def init_places():
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
    j+=1


def init_players():
  t1 = [random.randint(1, 29), random.randint(1, 29)]
  while(m[t1[0]][t1[1]]!="  "):
    t1 = [random.randint(1, 29), random.randint(1, 29)]
  m[t1[0]][t1[1]] = "t1"
  t2 = [random.randint(1, 29), random.randint(1, 29)]
  while  m[t2[0]][t2[1]] != "  ":
    t2 = [random.randint(1, 29), random.randint(1, 29)]
  m[t2[0]][t2[1]] = "t2"
  t3 = [random.randint(1, 29), random.randint(1, 29)]
  while m[t3[0]][t3[1]] != "  ":
    t3 = [random.randint(1, 29), random.randint(1, 29)]
  m[t3[0]][t3[1]] = "t3"
  t4 = [random.randint(1, 29), random.randint(1, 29)]
  while  m[t4[0]][t4[1]] != "  ":
    t4 = [random.randint(1, 29), random.randint(1, 29)]
  m[t4[0]][t4[1]] = "t4"

print("Para mover el impostor, escriba:")
print("up -> Arriba")
print('down -> Abajo')
print('left -> Izquierda')
print('right -> Derecha')

X = [random.randint(1, 29), random.randint(1, 29)]
m[X[0]][X[1]] = "X "
x=X[0]
y=X[1]
t=["  "]

def move_impostor(option,x,y,t):
  if option=="down" and m[x+1][y]!="| " and m[x+1][y]!="- " and x+1<=29:
    if m[x][y-1]!="  " and m[x][y+1]!="  ": 
      m[x][y]=t[-1]
      if t[-1]!="  ":t.pop()
    else: m[x][y]="  "
    if m[x+1][y]!="  ": 
      t.append(m[x+1][y])
    m[x+1][y]="X "
  elif option=="left" and m[x][y-1]!="| " and m[x][y-1]!="- " and y-1>=0:
    if m[x][y-1]!="  " and m[x][y+1]!="  ":
      m[x][y]=t[-1]
      if t[-1]!="  ":t.pop()
    else: m[x][y]="  "
    if m[x][y-1]!="  ": 
      t.append(m[x][y-1])
    m[x][y-1]="X "
  elif option=="up" and m[x-1][y]!="| " and m[x-1][y]!="- " and x-1>=0:
    if m[x][y-1]!="  "and m[x][y+1]!="  ": 
      m[x][y]=t[-1]
      if t[-1]!="  ":t.pop()
    else: m[x][y]="  "
    if m[x-1][y]!="  ": 
      t.append(m[x-1][y])
    m[x-1][y]="X "
  elif option=="right" and m[x][y+1]!="| " and m[x][y+1]!="- " and y+1<=29:
    if m[x][y-1]!="  " and m[x][y+1]!="  ": 
      m[x][y]=t[-1]
      if t[-1]!="  ":t.pop()
    else: m[x][y]="  "
    if m[x][y+1]!="  ": 
      t.append(m[x][y+1])
    m[x][y+1]="X "
  else:
    print("No se puede realizar el movimiento")
    return False
  return True

draw_canvas_empty()
init_places()
init_players()

dibujar(m)

while True:
  option=input("Mover X: ")
  if option!="init":
    if move_impostor(option,x,y,t):
      if option=="down": x+=1
      elif option=="left": y-=1
      elif option=="up": x-=1
      elif option=="right": y+=1
    dibujar(m)
  else: 
    m = []
    for i in range(32):
      m.append(["  "] * 32)
    draw_canvas_empty()
    X = [random.randint(1, 29), random.randint(1, 29)]
    m[X[0]][X[1]] = "X "
    x=X[0]
    y=X[1]
    init_places()
    init_players()
    dibujar(m)

