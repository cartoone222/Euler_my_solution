out = 100
for i in range(99,0,-1):
    out*=i
out = str(out)
out_ = 0
for i in out:
    out_+=int(i)
print(out_)
