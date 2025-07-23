import numpy as np
import matplotlib.pyplot as plt

class LIF:
    def __init__(self, tmax=0.5, dt=0.0001, tau=0.010, E_L=-0.070, Vth=-0.050, Vreset=-0.080, Cm=100e-12, Iapp=210e-12, ton=0.15, toff=0.35):
        self.tmax = tmax
        self.dt = dt
        self.tau = tau
        self.E_L = E_L
        self.Vth = Vth
        self.Vreset = Vreset
        self.Cm = Cm
        self.G_L = Cm / tau
        self.Iapp = Iapp
        self.ton = ton
        self.toff = toff
        self.t_vector = np.arange(0, tmax, dt)
        self.I = np.zeros(len(self.t_vector))
        self.I[round(ton/dt):round(toff/dt)] = Iapp
        self.V = E_L * np.ones(len(self.t_vector))
        self.spikes = np.zeros(len(self.t_vector))

    def simulate(self):
        for i in range(1, len(self.t_vector)):
            self.V[i] = self.V[i-1] + (self.dt/self.Cm) * (-self.G_L * (self.V[i-1] - self.E_L) + self.I[i-1])
            if self.V[i] >= self.Vth:
                self.spikes[i] = 1
                self.V[i] = self.Vreset

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.t_vector, self.V*1000, label=f'{self.Iapp*1e12:.0f} pA')
        plt.show()
    

cell = LIF()
cell.simulate()
cell.plot()