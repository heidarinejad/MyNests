import nest
import numpy as np
import pylab as pl

# In this program 2 neuron connected by gap junction. they are synchronized based of same level of currnet input

nest.ResetKernel()

# First we set the resolution of the simulation, create two neurons and
# create a `voltmeter` for recording.
nest.SetKernelStatus({'resolution': 0.05})
neuron = nest.Create('hh_psc_alpha_gap', 2)
vm = nest.Create('voltmeter', params={'to_file': False,'withgid': True,'withtime': True,'interval': 0.1})

# Then we set the constant current input, modify the initial membrane
# potential of one of the neurons and connect the neurons to the `voltmeter`.
nest.SetStatus(neuron, {'I_e': 100.0})
nest.SetStatus([neuron[0]], {'V_m': -10.0})
nest.Connect(vm, neuron, 'all_to_all')

# In order to create the `gap_junction` connection we employ the `all_to_all`
# connection rule: Gap junctions are bidirectional connections, therefore we
# need to connect `neuron[0]` to `neuron[1]` and `neuron[1]` to `neuron[0]`:
nest.Connect(neuron, neuron, {'rule': 'all_to_all', 'autapses': False}, {'model': 'gap_junction', 'weight': 0.5})

# Finally we start the simulation and plot the membrane potentials of
# both neurons.

nest.Simulate(351.0)
senders = nest.GetStatus(vm, 'events')[0]['senders']
times = nest.GetStatus(vm, 'events')[0]['times']
V = nest.GetStatus(vm, 'events')[0]['V_m']
pl.figure(1)
pl.plot(times[np.where(senders == 1)],
V[np.where(senders == 1)], 'r-')
pl.plot(times[np.where(senders == 2)],
V[np.where(senders == 2)], 'g-')
pl.xlabel('time (ms)')
pl.ylabel('membrane potential (mV)')
pl.show()