import math
pi = 3.14


def distance(x, y, z, sx, sy, sz):
    total_distance = 0.0
    if(z == sz and (x == sx or y == sy) and sz != 0):
        if(x != sx):
            total_distance = (2*pi*abs(x-sx))/6.0
        else:
            total_distance = (2*pi*abs(y-sy))/6.0
    else:
        total_distance = int((math.sqrt(pow(x-sx, 2)+pow(y-sy, 2))+abs(z-sz)))

    sx=x
    sy=y
    sz=z
    return total_distance


N=int(input())
Visite=[]

for i in range(0, 3*N, 1):
    Visite.append(int(input()))

sx=Visite[0]
sy=Visite[1]
sz=Visite[2]
sum=0.0

for i in range(3, 3*N, 3):
    sum=sum+distance(Visite[i], Visite[i+1], Visite[i+2], sx, sy, sz)

print(round(sum, 2))
