
def forward_euler(x0,xn,y0,f,h):
    y = y0
    x = x0
    step = int((xn-x0)/h)

    for i in range(step):
        y = y + (h*f(x,y))
        x += h

    return x,y,step

def f(t,y) :
    return 1-(y*t)**2


x,y,step = forward_euler(0,0.1,0,f,0.01)

print(f'hasil  menggunakan euler forward di y({x}) = {y} dengan step : {step}')


def RK(x0,xn,y0,f,h):
    y = y0
    x = x0
    step = int((xn-x0)/h)

    for i in range(step):
        k1 = h * f(x, y)
        k2 = h * f(x + (1 / 2) * h, y + (1 / 2) * k1)
        k3 = h * f(x + (1 / 2) * h, y + (1 / 2) * k2)
        k4 = h * f(x + h, y + k3)
        y = y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h

    return x, y, step

    

x,y,step = RK(0,0.1,0,f,0.01)
print(f'hasil menggunakan RK di y({x}) = {y} dengan step : {step}')
