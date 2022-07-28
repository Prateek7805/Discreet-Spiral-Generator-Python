#discreet spirals model #fermats spiral

from matplotlib import pyplot as plt
import math
import pandas as pd

def plot(data):
    plt.figure(figsize = (5,5))
    for i in data:
        plt.plot(i[0], i[1], marker = (4,0,i[2]), markersize=4**2)
    plt.grid()
    plt.show()

def generateModelData(n = 64, c=0.1, p = 0.414, startingPoint = 1):
    #n -> number of points
    #c -> scaling factor
    #p -> ratio to get the angle (by default the golden ratio)
    p = 1 if p>1 else 0 if p<0 else p
    startingPoint = 1 if startingPoint < 1 else startingPoint
    theta = 2*math.pi*p
    data = []
    for i in range(startingPoint, n+1):
        r = c*math.sqrt(i)
        angle = i*theta
        x = round(r*math.cos(angle), 2)
        y = round(r*math.sin(angle), 2)
        z = round((angle*180/math.pi)%360, 2)
        data.append([x,y, z])
    return data


def printModelData(data):
    for i in range(len(data)):
        print(f"#{i+1} x: {data[i][0]} , y: {data[i][1]} , angle: {data[i][2]}")

        
def outputToExcel(data, name = "spiral.xlsx"):
    index = [i+1 for i in range(len(data))]
    
    data[0].append(f"=MAX(B2:B{len(data)+1})")
    data[0].append(f"=MAX(C2:C{len(data)+1})")
    df = pd.DataFrame(data,index = index, columns = ["x","y","angle", "max X", "max Y"])
    df.to_excel(name)

    
if __name__ == "__main__":
    n = 64
    scale = 0.45
    ratio = (1 + math.sqrt(5))/2 - 1
    data = generateModelData(n, scale, ratio)
    outputToExcel(data) #output excel
    plot(data)
