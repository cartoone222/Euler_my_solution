_1 = 1
_2 = 2

t = 0

out = 2

while t < 4000000:
    t = _1 + _2
    
    if t%2 == 0:
        out += t
    
    _1 = _2
    _2 = t

print(out)
