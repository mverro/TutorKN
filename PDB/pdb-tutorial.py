import matplotlib.pyplot as plt


##########################
# Definisiin fungsinya
def f(t,y) :
    return 1-(y*t)**2
##########################


###############################
# Dengan forward euler , x0(x init), xn (x target), y0 (y init), f (fungsi), h(jarak step)
def forward_euler(x0,xn,y0,f,h):
    y = [y0]
    x = [x0]
    step = int((xn-x0)/h)

    for i in range(step):
        y_baru = y[i] + (h*f(x[i],y[i]))
        x_baru = x[i] + h
        y.append(y_baru)
        x.append(x_baru)

    return x,y,step


x,y,step = forward_euler(0,0.1,0,f,0.01)

print(f'hasil  menggunakan euler forward di y({x[-1]}) = {y[-1]} dengan step : {step}')
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metode Euler')
plt.show()



##############################
# Dengan RK
# Dengan forward euler , x0(x init), xn (x target), y0 (y init), f (fungsi), h(jarak step)
def RK(x0,xn,y0,f,h):
    y = [y0]
    x = [x0]
    step = int((xn-x0)/h)

    for i in range(step):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + (1 / 2) * h, y[i] + (1 / 2) * k1)
        k3 = h * f(x[i] + (1 / 2) * h, y[i] + (1 / 2) * k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y_baru = y[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x_baru = x[i] + h
        x.append(x_baru)
        y.append(y_baru)

    return x, y, step

    
x,y,step = RK(0,0.1,0,f,0.01)
print(f'hasil menggunakan RK di y({x}) = {y} dengan step : {step}')
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metode Euler')
plt.show()
