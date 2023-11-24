import numpy as np
import matplotlib.pyplot as plt

samples_number = 500
variance = 0.1

x = np.linspace(0, 6 * np.pi, samples_number)
u = np.sin(x)

plt.scatter(x,u,s=1)
plt.savefig('./Adaptive_control_files/{}'.format('u'))
plt.clf()

a = [1,1,1]
Φ = []
v = []
y = []

for u_k in range(2 , len(u)):
    v_k = a[0] * u[u_k] + a[1] * u[u_k-1] + a[2] * u[u_k-2]
    v.append(v_k)
    Φ_k = (np.array([u[u_k], u[u_k-1], u[u_k-2]])).reshape(1,3)
    Φ.append(Φ_k.T)

v = np.array(v)
Φ = np.array(Φ)

plt.scatter(x[2:],v,s=1)
plt.savefig('./Adaptive_control_files/{}'.format('v'))
plt.clf()

def sin_noise_generator(sin, samples_number, variance):
    noise = (np.random.rand(samples_number) - 0.5) * np.sqrt(12 * variance)
    return sin + noise

y = sin_noise_generator(v,samples_number-2,variance)
y = np.array(y)

plt.scatter(x[2:],y,s=1)
plt.savefig('./Adaptive_control_files/{}'.format('y'))
plt.clf()

def recursive_least_squares_algorithm(N):
    def recursive_P(N):
        if N == 0:
            P_0 = np.zeros((3,3))
            np.fill_diagonal(P_0,10**3)
            return P_0 
        else:
            P_prev = recursive_P(N-1) 
            P = P_prev - (P_prev @ Φ[N] @ Φ[N].T @ P_prev)/(1 + Φ[N].T @ P_prev @ Φ[N])
            return P
        
    a_list = []

    def recursive_a(N):
        if N == 0:
            a_0 = np.zeros((3,1))
            a_list.append(a_0)
            return a_0
        else:
            a_prev = recursive_a(N-1)
            a = a_prev + recursive_P(N) @ Φ[N] @ (v[N].reshape(1,1) - Φ[N].T @ a_prev)
            a_list.append(a)
            return a
    
    a = recursive_a(N)
    return a, a_list

a, a_list = recursive_least_squares_algorithm(samples_number-3)

a0_list = []
a1_list = []
a2_list = []

for n in range(0,len(a_list)):
    a0_list.append(a_list[n][0])
    a1_list.append(a_list[n][1])
    a2_list.append(a_list[n][2])

x = np.arange(samples_number-2)

plt.plot(x,a0_list,label='a0')
plt.plot(x,a1_list,label='a1')
plt.plot(x,a2_list,label='a2')
plt.savefig('./Adaptive_control_files/{}'.format("wykres"))
plt.clf()

plt.plot(x,y,label='y')
plt.savefig('./Adaptive_control_files/{}'.format("wykres2"))
plt.clf()

        



