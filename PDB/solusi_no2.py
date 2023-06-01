import matplotlib.pyplot as plt


def forward_euler_kasus(x0,xn,v0,f,h):
    t = [x0]
    x = [x0]
    v = [v0]
    step = int((xn-x0)/h)

    for i in range(step):
        t_baru = t[i] + h
        x_baru = x[i] + h * v[i]
        v_baru = v[i] + h * f(x[i],v[i],t[i])
        t.append(t_baru)
        x.append(x_baru)
        v.append(v_baru)

    return t,x



def f(x,v,t):
    if t <=1 :
        F = 5000
    else :
        F = 0

    m = 5000
    k = 50000
    c = 5000
    return (F - c * v - k * x) / m


t0 =0
t1 =10
x0 = 0
v0 = 0
h = 0.01


t,x = forward_euler_kasus(t0,t1,x0,f,h)

plt.plot(t,x)
plt.xlabel('Waktu')
plt.ylabel('Posisi')
plt.title('Studi kasus')
plt.show()
