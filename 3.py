def invers(t):
  out = []
  for i in range(len(t)):
    out += t[-(i+1)]
  return out

for j in range(998001,0,-1):
  if list(str(j)[:3]) == invers(list(str(j)[3:6]):
    x = j
    for i in range(999,0,-1):
      if x % i == 0:
        if len(str(i))<=3 and len(str(int(x/i)))<=3:
           print(j)
