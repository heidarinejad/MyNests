
import nest
import pylab
import nest.voltage_trace

weight=50.0
delay=1.0
stim=1000.0

neuron1=nest.Create("iaf_psc_alpha")
neuron2=nest.Create("iaf_psc_alpha")
neuron3=nest.Create("iaf_psc_alpha")
neuron4=nest.Create("iaf_psc_alpha")
voltmeter=nest.Create("voltmeter")

nest.SetStatus(neuron3, {"I_e":380.0})
nest.SetStatus(neuron4, {"I_e":400.0})
nest.SetStatus(neuron1, {"I_e":stim})
nest.Connect(neuron1,neuron2, syn_spec={'weight':weight,'delay':delay})
nest.Connect(voltmeter, neuron1)
nest.Connect(voltmeter, neuron2)
nest.Connect(voltmeter, neuron3)
nest.Connect(voltmeter, neuron4)

nest.Simulate(100.0)   #ms

nest.voltage_trace.from_device(voltmeter)
nest.voltage_trace.show()



# to retrive the information of neurons seperately
dmm=nest.GetStatus(voltmeter, "events")[0]
dmm1=dmm["V_m"]
vs1=dmm["V_m"][::4]     # start at index 0:till the end: each second entry (all odd outputs)
ts1=dmm["times"][::4]
vs2=dmm["V_m"][1::4]    # start at index 1:till the end: each second entry (all even outputs)
vs3=dmm["V_m"][2::4]
vs4=dmm["V_m"][3::4]
ts2=dmm["times"][1::4]
ts3=dmm["times"][2::4]
ts4=dmm["times"][3::4]


pylab.figure(2)
pylab.plot(ts1,vs1)
pylab.show()

pylab.figure(3)
pylab.plot(ts2,vs2)
pylab.show()

pylab.figure(4)
pylab.plot(ts3,vs3)
pylab.show()

pylab.figure(5)
pylab.plot(ts4,vs4)
pylab.show()
