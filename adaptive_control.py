import numpy as np
import matplotlib.pyplot as plt

samples_number = 1000
variance = 0.1
lambd = 1

x = np.linspace(0, 6 * np.pi, samples_number)
u = np.random.rand(samples_number)*2
a_sin = np.sin(x)/2

Φ = []
Φ.append(np.array([u[0], 0, 0]))
Φ.append(np.array([u[1], u[0], 0]))
for u_k in range(2, len(u)):
    Φ.append(np.array([u[u_k], u[u_k - 1], u[u_k - 2]]))

a = [1, 5, 3]
v = []
v.append(a[0] * u[0] + 0 + 0)
v.append(a[0] * u[1] + a[1] * u[0] + 0)
for u_k in range(2, len(u)):
    v.append((a_sin[u_k]+a[0]) * u[u_k] + a[1] * u[u_k - 1] + a[2] * u[u_k - 2])

def noise_generator(v, samples_number, variance):
    noise = (np.random.rand(samples_number) - 0.5) * np.sqrt(12 * variance)
    return v + noise

y = noise_generator(v,samples_number,variance)

def recursive_least_squares_algorithm(N):
    a = np.zeros((3, 1))
    P = np.zeros((3, 3))
    np.fill_diagonal(P, 10**3)
    a_list = []

    for k in range(N):
        Φ_k = Φ[k].reshape(-1, 1)
        P = 1/lambd * (P - (P @ Φ_k @ Φ_k.T @ P) / (lambd + Φ_k.T @ P @ Φ_k))
        a = a + P @ Φ_k @ (y[k] - Φ_k.T @ a)
        a_list.append(a)
    
    return a, a_list

a, a_list = recursive_least_squares_algorithm(samples_number)
a0_list, a1_list, a2_list = [], [], []
x = np.arange(samples_number)

for n in range(0,len(a_list)):
    a0_list.append(a_list[n][0])
    a1_list.append(a_list[n][1])
    a2_list.append(a_list[n][2])

plt.plot(x,a0_list,label='a0')
plt.plot(x,a1_list,label='a1')
plt.plot(x,a2_list,label='a2')
plt.legend()
plt.savefig('./Adaptive_control_files/{}'.format("wykres"))
plt.clf()
