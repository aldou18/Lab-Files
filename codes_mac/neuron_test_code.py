# if these three lines work, then neuron is correctly installed
from neuron import h
soma = h.Section(name='soma')
from neuron.units import ms, mV
import matplotlib.pyplot as plt

# if these two lines work then the text outputs show up corrcetly on the terminal 
# it should look like a block of text and some dashes
#|-|       soma(0-1)
# 1.0
# {'point_processes': {}, 'density_mechs': {}, 'ions': {}, 'morphology: {'L': 100.0, 'diam': [500.0], 'pts3d': [], 'parent': None, 'trueparent': None}, 'nseg': 1, 'Ra': 35.4, 'cm': [1.0], 'regions': set(), 'species': set(), 'name': 'soma', 'hoc_internal_name': '__nrnsec_0x7f8ee98b8000', 'cell': None}
h.topology()
print(soma.psection())

# this next segment should output a graph in another window using matplotlib library 
# setting segment length and diameter and inserting Hodgkin-Huxley channel mechanics 
soma.L = 20
soma.diam = 201
soma.insert('hh')
iclamp = h.IClamp(soma(0.5))
iclamp.delay = 2
iclamp.dur = 0.1
iclamp.amp = 0.9
v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector
t = h.Vector().record(h._ref_t)                     # Time stamp vector
h.load_file('stdrun.hoc')
h.finitialize(-65 * mV)
h.continuerun(40 * ms)
plt.plot(t,v)
plt.show()