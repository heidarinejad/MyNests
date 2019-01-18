import pylab
import nest
import numpy

# To create we need nodes, number and param
# first define the param and then create the desired note

#better to define the param before then definition of nodes
# method 1
"""
ndic={"I_e":200.0, "tau_m": 20.0}
popneuron=nest.Create("iaf_psc_alpha", 100, params=ndic)
"""
# another way to do same thing as above
# method 2
"""
ndic={"I_e":200.0, "tau_m": 20.0}
nest.SetDefaults("iaf_psc_alpha", ndic)
popneuron1=nest.Create("iaf_psc_alpha", 100)
# and even more
popneuron2=nest.Create("iaf_psc_alpha", 100)
"""

# in case of batches of neurons with same model and different parameters
# better to use CopyModel
# it means copy new model based on existing model
# method 3
"""
nest.CopyModel("iaf_psc_alpha", "exc_iaf_psc_alpha")
# then
edic={"I_e":200.0, "tau_m": 20.0}
nest.SetDefaults("exc_iaf_psc_alpha", edic)
# or in one step
idic={"I_e":300.0}
nest.CopyModel("iaf_psc_alpha", "inh_iaf_psc_alpha", params=idic)
"""

# no need to always define all same
# also possible to specify params of some neurons together
# here 2 neuorns with different parameters
# method 4
"""
param_list=[{"I_e":200.0, "tau_m": 20.0}, {"I_e":150.0, "tau_m": 30.0}]
mixpop=nest.Create("exc_iaf_psc_alpha",2, param_list)
"""

# what if we want to parametrize the neurons one by one
# method 5-1 (using random distribution)
"""
Vth=-55
Vrest=-70
for neuron in mixpop:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})
"""

# above method in one by one, but we know that SetStatus could handle list of nodes simultaneously, so:
# method 5-2 (using list)
"""
dVms= [{"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()} for x in mixpop)
nest.SetStatus(mixpop, dVms)
"""
# and in case of changing only one parameter among the population it is easier to write:
"""
Vms= Vrest+(Vth-Vrest)*numpy.random.rand(len(mixpop))
nest.SetStatus(mixpop, "V_m", Vms)
"""

