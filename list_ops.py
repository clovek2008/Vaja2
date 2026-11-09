sez = [12, 5, 8, 21, 3, 16, 9, 14] 

def vsota(sez):
    return sum(sez)
print(vsota(sez))

def povprecna(sez):
    return sum(sez)/len(sez)
print(povprecna(sez))

def najvecja(sez):
    return max(sez)
print(najvecja(sez))

def najmanjse(sez):
    return min(sez)
print(najmanjse(sez))

def sodi(sez):
    int i = 0
    for i in sez:
        if i%2==0:
            i+=1
    return i
print(sodi(sez))
