def nhap(): 
    return input().split()
def xuat(value):
    if isinstance(value, list): 
        print('->'.join(value))
        return
    return print(value)
    
def demsochan(value): 
    dem = 0 
    for i in value: 
        if int(i) % 2 == 0: 
            dem += 1
    return dem 
def songuyento(value): 
    dem = 0 
    for i in range(len(value)): 
        if int(value[i]) > 1: 
            for j in range(2, int(value[i])): 
                if int(value[i]) % j == 0:
                    break
            else: dem += 1
    return dem     
def sapxeptangdan(value):
    for i in range(len(value) - 1): 
        for j in range(i + 1, len(value)): 
            if value[i] > value[j]: 
                value[i], value[j] = value[j], value[i]
    return value
                

value = nhap()
xuat(value)
sapxeptangdan(value)
xuat(demsochan(value))
xuat(value)
xuat(songuyento(value))