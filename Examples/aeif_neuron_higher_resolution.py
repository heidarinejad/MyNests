import nest
import nest.voltage_trace
import pylab

nest.ResetKernel()

# First we make sure that the resolution of the simulation is 0.1 ms.
# This is important, since the slop of the action potential is very steep.
res = 0.1     # lower resolution
nest.SetKernelStatus({"resolution": res})

neuron1 = nest.Create("aeif_cond_exp")
neuron2 = nest.Create("aeif_cond_exp")

#Set the parameters of the neuron according to the paper.
nest.SetStatus(neuron1, {"V_peak": 20., "E_L": -60.0, "a": 80.0, "b": 80.5, "tau_w": 720.0})  # according the paper fig. 3D
nest.SetStatus(neuron2, {"a": 4.0, "b": 80.5})  # according the paper fig. 2C

# Create and configure the stimulus which is a step current.
dc1 = nest.Create("dc_generator")      # current DC generator
dc2 = nest.Create("dc_generator",2)
nest.SetStatus(dc1, [{"amplitude": -800.0, "start": 0.0, "stop": 400.0}])
nest.SetStatus(dc2, [{"amplitude": 500.0, "start": 0.0, "stop": 200.0},
                     {"amplitude": 800.0, "start": 500.0, "stop": 1000.0}])

# We connect the DC generator.
nest.Connect(dc1, neuron1, 'all_to_all')
nest.Connect(dc2, neuron2, 'all_to_all')# 'all_to_all' is not the necessary phrase here

# And add a voltmeter to record the membrane potentials.
voltmeter = nest.Create("voltmeter")

# We set the voltmeter to record in small intervals of 0.1 ms and connect
# the voltmeter to the neuron.
nest.SetStatus(voltmeter, {"withgid": True, "withtime": True, 'interval': 0.1})    # set lower recording resolution
nest.Connect(voltmeter, neuron1)
nest.Connect(voltmeter, neuron2)

# Finally, we simulate for 1000 ms and plot a voltage trace
# to produce the figure.
nest.Simulate(1000.0)
nest.voltage_trace.from_device(voltmeter)
pylab.axis([0, 1000, -85, 0])
pylab.show()