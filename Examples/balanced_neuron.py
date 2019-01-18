from scipy.optimize import bisect
import nest
import nest.voltage_trace


# this program stimulate a neuron with exc & inh poulation of neurons
# optimazation og firing rate of inh neurons to let neuron to file with same rate as excitatory pops

# this script uses 'bisection' method from 'scipy'

nest.set_verbosity("M_WARNING")
nest.ResetKernel()

t_sim = 25000.0  # how long we simulate
n_ex = 16000     # size of the excitatory population
n_in = 4000      # size of the inhibitory population
r_ex = 5.0       # mean rate of the excitatory population
r_in = 20.5      # initial rate of the inhibitory population
epsc = 45.0      # peak amplitude of excitatory synaptic currents
ipsc = -45.0     # peak amplitude of inhibitory synaptic currents
d = 1.0          # synaptic delay
lower = 15.0     # lower bound of the search interval
upper = 25.0     # upper bound of the search interval
prec = 0.01      # how close need the excitatory rates be

neuron = nest.Create("iaf_psc_alpha")
noise = nest.Create("poisson_generator", 2)
voltmeter = nest.Create("voltmeter")
sd = nest.Create("spike_detector")

nest.SetStatus(noise, [{"rate": n_ex * r_ex}, {"rate": n_in * r_in}])
nest.SetStatus(voltmeter, {"withgid": True, "withtime": True})

nest.Connect(neuron, sd)
nest.Connect(voltmeter, neuron)
nest.Connect(noise, neuron, syn_spec={'weight': [[epsc, ipsc]], 'delay': 1.0})

def output_rate(guess):
    print("Inhibitory rate estimate: %5.2f Hz" % guess)
    rate = float(abs(n_in * guess))
    nest.SetStatus([noise[1]], "rate", rate)
    nest.SetStatus(sd, "n_events", 0)
    nest.Simulate(t_sim)
    out = nest.GetStatus(sd, "n_events")[0] * 1000.0 / t_sim
    print(" -> Neuron rate: %6.2f Hz (goal: %4.2f Hz)" % (out, r_ex))
    return out

in_rate = bisect(lambda x: output_rate(x) - r_ex, lower, upper, xtol=prec)
print("Optimal rate for the inhibitory population: %.2f Hz" % in_rate)

nest.voltage_trace.from_device(voltmeter)