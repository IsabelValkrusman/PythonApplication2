import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x1 = np.arange(0, 9, 1) 
x2 = np.arange(-10, 0, 1)
x3 = np.arange(-9, -3, 1)
x4 = np.arange(-3, 9, 1)
x5 = np.arange(5, 8.3, 1)
x6 = np.arange(5, 8.5, 1)
x7 = np.arange(-13, -9, 1)
x8 = np.arange(-15, -13, 1)
x9 = np.arange(-15, -10, 1)
x10 = np.arange(3, 4, 1)


y1 = ((2/27)*(x1**2)-3)
y2 = (0.04*x2**2-3)
y3 = ((2/9)*(x3+6)**2+1)
y4 = abs(-1/12*(x4-3)**2+6)
y5 = abs(1/9*(x5-5)**2+2)
y6 = abs(1/8*(x6-7)**2+1.5)
y7 = (-0.75*(x7+11)**2+6)
y8 = (-0.5*(x8+13)**2+3)
y9 = [1] * len(x9)
y10 = [3] * len(x10)



plt.plot(x1,y1 ,'-b',linewidth=5)
plt.plot(x2,y2 ,'-r',linewidth=5)
plt.plot(x3,y3 ,'-r',linewidth=5)
plt.plot(x4,y4 ,'-',color="pink",linewidth=5)
plt.plot(x5,y5 ,'-b',linewidth=5,label="кит")
plt.plot(x6,y6 ,'-r',linewidth=5)
plt.plot(x7,y7 ,'-b',linewidth=5)
plt.plot(x8,y8 ,'-b',linewidth=5)
plt.plot(x9,y9,'-r')
plt.plot(x10,y10,'-.g',marker="o",label="глаз")

plt.legend()
plt.text(-7, 24.5, "На диаграмме 2 графика:\nпарабола и линия экстремума")

plt.annotate(r"Экстремум функции = $\frac{-b}{2a} = \frac{-4}{2} = -2$",
xy=(-2, 9), xytext=(-5, 15),
arrowprops=dict(facecolor="red", shrink=0.05))

plt.savefig("my_image.png")
plt.show() 

fail=open("tex.num.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(float(line[n+1:len(line)].strip()))
fail.close()

title = "Данные о ИТ безопасности"
plt.grid(True)

color_rectangle = np.random.rand(7, 3)
plt.pie(mas2, labels=mas1)

plt.show()

