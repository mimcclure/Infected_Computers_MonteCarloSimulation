import numpy as np

#N = input('Number of computers: ')
N = 20
#p = input('Probability of spreading the infection: ')
p = 0.1
infect_comps = 1   #computers infected
fix_comps = 5      #computers fixed
#BERNOULLI
def Bernoulli(p):
    U = np.random.random()
    if (U < p):
        X = 1
    else:
        X = 0
    return X

comps = [0] * N
comps[0] = 1

i = 1
days = np.zeros((len(comps)-1,1),dtype=np.int16)
total_inf = comps
while (comps[i] == 1):
  total_inf =+ 1
  
while(comps[i] != 0):
  days += 1

for i in range(1): #change for how many times to loop the simulation
#MORNING
  if i in range(1, N):
      comps[i] = 0
  print(comps)
  x = 0
  i = 0
  for i in range(0, N):
      for j in range(0, N):
          if (comps[i] == 1) and (comps[j] == 0):
              x = Bernoulli(p)
              if (x == 1):
                  comps[j] = 2

  for i in range(0, N):
      if (comps[i] == 2):
          comps[i] = 1
  print(comps)   

  #AFTERNOON
  if (comps[i] <= fix_comps):
    comps[i] = 0
    if (comps[i] > fix_comps):
        if (comps.random.random(comps[i]) == 1): #choose 5 from the infected computers
          comps[i] = 0
    print('Infected computers left after the technician finishes cleaning them: '+str(comps[i]))

daysstr = ', '.join(str(e) for e in days)
print('Total days to clean all computers: ',len(daysstr))
print('Total number of computers affected per simulation: ',sum(total_inf))