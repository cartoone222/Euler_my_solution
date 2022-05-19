index = 0

while True:
    index += 10
    for i in range(20):
        if index%(i+1)==0:
            pass
        else:
            break
    else:
        print(index)
        break
