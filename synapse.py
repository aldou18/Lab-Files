import numpy as np
import matplotlib.pyplot as plt


gmax = 0.005        
C = 1               
Esyn = 0            
tau_r = 2           
tau_d = 8           
g_leak = 0.02       
E_leak = -60        


dt = 0.5  # ms
t_max = 100
time = np.arange(0, t_max + dt, dt)


g_syn = np.zeros_like(time)
i_syn = np.zeros_like(time)
v = np.zeros_like(time)
v[0] = E_leak


for i, t in enumerate(time):
    g_syn[i] = gmax * (-np.exp(-t / tau_r) + np.exp(-t / tau_d))
    if i > 0:
        i_syn[i] = g_syn[i] * (v[i-1] - Esyn)
        i_leak = g_leak * (v[i-1] - E_leak)
        dv = (-i_syn[i] - i_leak) / C
        v[i] = v[i-1] + dv * dt


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(time, g_syn)
plt.title("Synaptic Conductance (g_syn)")


plt.subplot(1, 2, 2)
plt.plot(time, i_syn)
plt.title("Synaptic Current (i_syn)")


plt.show()

