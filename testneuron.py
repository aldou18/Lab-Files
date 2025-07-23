import neuron
from neuron import h
from neuron.units import ms, mV
import textwrap
import matplotlib.pyplot as plt

print(neuron.__version__)
soma = h.Section(name='soma')

h.topology()
print(soma.psection())

print(soma.psection()['morphology']['L'])
print(soma.L) # easier version of ^^^^^


soma.L = 20
soma.diam = 20

print(textwrap.fill(', '.join(dir(h))))

soma.insert('hh')

print("type(soma) = {}".format(type(soma)))
print("type(soma(0.5)) = {}".format(type(soma(0.5))))

mech = soma(0.5).hh
print(dir(mech))
print(mech.gkbar)
print(soma(0.5).hh.gkbar)

iclamp = h.IClamp(soma(0.5))

print([item for item in dir(iclamp) if not item.startswith('__')])
iclamp.delay = 2
iclamp.dur = 0.1
iclamp.amp = 0.9

print(soma.psection())

v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector
t = h.Vector().record(h._ref_t) 


h.load_file('stdrun.hoc')
h.finitialize(-65 * mV)
h.continuerun(40 * ms)

plt.figure()
plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()
