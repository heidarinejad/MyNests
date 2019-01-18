import nest
import pylab
import nest.voltage_trace
nest.set_verbosity("M_WARNING")
nest.ResetKernel()

neuron=nest.Create("iaf_psc_alpha")
voltmeter=nest.Create("voltmeter")

nest.SetStatus(neuron, "I_e",376.0)    # this is the minimum current for iaf neuron to start to fire
nest.SetStatus(voltmeter, [{"withgid":True}])

nest.Connect(voltmeter, neuron)        # seems multimeter and voltmeter works in same way

nest.Simulate(1000.0)   # ms

# first way to represent the graph
nest.voltage_trace.from_device(voltmeter)

nest.voltage_trace.show()

#second way to represent the result
dmm=nest.GetStatus(voltmeter)[0]
Vms=dmm["events"]["V_m"]
ts=dmm["events"]["times"]

pylab.figure(2)
pylab.plot(ts,Vms)
pylab.show()

# actually two graph is overlapping here and (1st black and 2nd blue graph make orange output)
# in case we give the number 2 to figure they will be separated

# another way to extract the data
dnn=nest.GetStatus(voltmeter,keys="events")[0]
evs=dnn["senders"]
#ts=dnn["times"]      # same as 'ts' above

pylab.figure(3)
pylab.plot(ts,evs, ".")
pylab.show()