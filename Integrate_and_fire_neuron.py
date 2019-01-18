# iaf (integrate_and_fire) neuron example

import nest
import pylab    # for plotting

# in this program a DC current is injected to neuron using a current generator device and V_m is recorded by 'spike_detector'


# to do so the best way is define a function so called ' build_network'
# this function take the resoultion as a input

def build_network(dt):

    nest.ResetKernel()
    nest.SetKernelStatus({"local_num_threads":1, "resolution": dt})    # number of threads is set to zero


    neuron=nest.Create("iaf_psc_alpha")
    nest.SetStatus(neuron, "I_e",376.0)   # neuron is recieved an external current

    Vm=nest.Create('voltmeter')
    nest.SetStatus(Vm, 'withtime', True)  #times are given in the times vector in events

    sd=nest.Create('spike_detector')

    nest.Connect(Vm,neuron)
    nest.Connect(neuron, sd)

    # The Voltmeter is connected to the neuron and the neuron to the spikedetector
    # because the neuron sends spikes to the detector and the voltmeter 'observes' the neuron

    return Vm,sd


# the neuron is stimulated with 3 different dt and voltage is plotted
for dt in [0.1,0.5,1.0]:
    print("Running simulation with dt=%.2f" %dt)
    Vm,sd=build_network(dt)


    nest.Simulate(100.0)   # ms

    # spike detector counts the spike numbers during simulation time
    potentials=nest.GetStatus(Vm,"events")[0]["V_m"]
    times=nest.GetStatus(Vm, "events")[0]["times"]

    # The values of the voltage recorded by the voltmeter are read out and the values for the membrane potential
    # are stored in potential and the corresponding times in the times array


    # To print out the results (voltage trace over time)
    pylab.plot(times,potentials, label="dt=%.2f" %dt)
    print("Number of spikes: {0}".format(nest.GetStatus(sd, "n_events")[0]))


    pylab.legend(loc=5)       # this is for defining the position of label box   0=<loc=<10
    pylab.xlabel("Time (ms)")
    pylab.ylabel("V_m (mV)")
    #pylab.plt(times,potentials)
