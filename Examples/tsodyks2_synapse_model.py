import nest
import nest.voltage_trace
nest.ResetKernel()

# Parameter set for depression
dep_params = {"U": 0.67, "u": 0.67, 'x': 1.0, "tau_rec": 450.0, "tau_fac": 0.0, "weight": 250.}

# Parameter set for facilitation
fac_params = {"U": 0.1, "u": 0.1, 'x': 1.0, "tau_fac": 1000.0, "tau_rec": 100., "weight": 250.}

# Now we assign the parameter set to the synapse models.
t1_params = fac_params

# for tsodyks_synapse
t2_params = t1_params.copy() # for tsodyks2_synapse
nest.SetDefaults("tsodyks2_synapse", t1_params)
nest.SetDefaults("tsodyks_synapse", t2_params)
nest.SetDefaults("iaf_psc_exp", {"tau_syn_ex": 3.0})

# Create three neurons.
neuron = nest.Create("iaf_psc_exp", 3)

# Neuron one produces spikes. Neurons 2 and 3 receive the spikes via
# the two synapse models.
nest.Connect([neuron[0]], [neuron[1]], syn_spec="tsodyks_synapse")
nest.Connect([neuron[0]], [neuron[2]], syn_spec="tsodyks2_synapse")

# Now create two voltmeters to record the responses.
voltmeter = nest.Create("voltmeter", 2)
nest.SetStatus(voltmeter, {"withgid": True, "withtime": True})

# Connect the voltmeters to the neurons.
nest.Connect([voltmeter[0]], [neuron[1]])
nest.Connect([voltmeter[1]], [neuron[2]])

# Now simulate the standard STP protocol: a burst of spikes,
# followed by a pause and a recovery response.
nest.SetStatus([neuron[0]], "I_e", 376.0)
nest.Simulate(500.0)
nest.SetStatus([neuron[0]], "I_e", 0.0)
nest.Simulate(500.0)
nest.SetStatus([neuron[0]], "I_e", 376.0)
nest.Simulate(500.0)

# Finally, generate voltage traces. Both are shown in the same plot
# and should be almost completely overlapping.
nest.voltage_trace.from_device([voltmeter[0]])
# nest.voltage_trace.from_device([voltmeter[1]])