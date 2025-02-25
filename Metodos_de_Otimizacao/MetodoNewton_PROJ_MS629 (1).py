#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

α = pow(10, -4) # taxa de decr ́escimo suficiente na Regra de Armijo.
β = pow(10, -3) # constante de proporcionalidade para a dire ̧c ̃ao.
γ = pow(10, -6) # constante relativa ao ˆangulo entre a dire ̧c ̃ao e o gradiente.
σ = 0.5 # fator de diminui ̧c ̃ao na busca unidimensional.
ρ = pow(10, -3) # incremento inicial na globaliza ̧c ̃ao do m ́etodo de Newton.
ε = pow(10, -7) # precis ̃ao para a norma do gradiente (crit ́erio de parada).
M = 1000 # numero maximo de iterações.

# X_ = np.array([0.23778056, 0.19917721, 0.88592654, 0.59720572, 0.03588704,
#        0.0843859 , 0.34820196, 0.42716548, 0.36100787, 0.30498218])
X_ = np.array([-1000, 1000])
n = len(X_)

def f(x):
    return np.sum([i * x ** 2 for i in range(len(x))])

def gradiente_quadratica(x):
    return (2 * np.arange(1, len(x) + 1) * x).reshape(n, 1)

def hessiana_quadratica(x):
    hessian = np.diag(np.array(2*np.arange(1, len(x) + 1)))
    return hessian.reshape(n, n)

def f_(x):
    return (x[0] + 3) ** 2 + (x[1] + 2) ** 2

def grad_F(x):
    return np.array([2 * (x[0] + 3), 2 * (2 + x[1])]).reshape(n, 1)

def hess_F(x):
    return np.array([2, 0, 0, 2]).reshape(n, n)



print(f_(X_))
print(grad_F(X_))
print(hess_F(X_))

# print(gradiente_quadratica(x))
# print(hessiana_quadratica(x))


#np.random.seed(10)
#X = np.random.randint(-5, 5, size = n)

#X = np.ones(n)*2
print(f(X_))

def metodo_newton(f, grad_f, hess_f, x0, ε, M, α, σ, β, γ, ρ):
    k = 0
    X = x0
    μ = 0.0
    grad = grad_f(X)
    hess = hess_f(X)
    g_norm = np.linalg.norm(grad)
    while g_norm >= ε and k < M:
        z = 0

        print("grad\n", grad)
        print("g_norm", g_norm)
        print("hess\n", hess)
        while z == 0:
            try:
                d = np.linalg.solve(hess + μ * np.eye(len(hess)), -grad)
                print("D resolvido:\n", d)
                prod_grad_d = float(np.dot(np.transpose(grad), d))
                print("prod_grad_d:", prod_grad_d)
                d_norm = np.linalg.norm(d)
                print("outro lado: ", -γ * g_norm * d_norm)
                if prod_grad_d > -γ * g_norm * d_norm:
                    μ = max(2 * μ, ρ)
                else:
                    z = 1
            except np.linalg.LinAlgError:
                μ = max(2 * μ, ρ)
        # print(d)
        if d_norm < β * g_norm:
            d = β * g_norm * (1 / d_norm) * d
        print(d)
        t = 1.0
        prod_grad_d = float(np.dot(np.transpose(grad), d))
        newX = X.reshape(n,1) + t * d
        print("newx:\n", newX)
        print("desvio: ", float(f(newX)))
        print("porra: ", f(X) + α * t * prod_grad_d)
        while float(f(newX)) > f(X) + α * t * prod_grad_d:
            t *= σ
            newX = X.reshape(n,1) + t * d
        print("passo com t = ", t)
        print("bef", X)
        X = newX.copy().reshape(1, n)[0]
        print("aft", X)
        k += 1
        grad = grad_f(X)
        hess = hess_f(X)
        g_norm = np.linalg.norm(grad)
        
    return X, k, f(X)

# resultado, iteracoes, f_estrela = metodo_newton(f, gradiente_quadratica, hessiana_quadratica, X_, ε, M, α, σ, β, γ, ρ)
resultado, iteracoes, f_estrela = metodo_newton(f_, grad_F, hess_F, X_, ε, M, α, σ, β, γ, ρ)
print(f"\nResultado da otimização Newton para {f.__name__}: {resultado}\nf(x*) = {f_estrela}\n Número de Iterações realizadas: {iteracoes}\n")


# In[ ]:




