import nest

# access to all type of synaptic models
"""
nest.Models()
"""

# access to synaptic parameters any adjustment
"""
nest.GetDefaults("Model_name")
nest.SetDefaults("Model_name", {"param_name": value})
"""

# define customised synaptic model
"""
nest.CopyModel("stdp_synapse", "my_synapse_model", {"Wmax":90.0})
"""
# all synapses could be parametrized by 'SetDefaults' except STDP synapses which are control by
# pre & post synapses...for example the spike timing of post-synaptic could be set"
"""
nest.Create("iaf_psc_alpha", params={"tau_minus": 30.0})
"""

# most of the synaptic parameters are distribution. to handle
"""
alpha_min=0.1
alpha_max=2.0
w_min=0.5
w_max=5.0

syn_dict= {"model": "stdp_synapse",
            "alpha": {"distribution": "uniform", "low": alpha_min, "high": alpha_max}
            "weight": {"distribution": "uniform", "low": w_min, "high": w_max}
            "delay":1.0}
            
nest.Connect(pop1, pop2, "all_to_all", syn_dict)
"""
# all distribution models
# normal        (mu,sigma)
# lognormal     (mu,sigma)
# uniform       (low,high)
# uniform_int   (low,high)
# binomial      (n,p)
# exponential   (lambda)
# gamma         (order,scale)
# poisson       (lambda)

# all information of any connection could be extracted
# source, target or synapse model could be omitted to generalize
"""
conns=nest.GetConnections(epop1, epop2, synapse_model="stdp_synapse")
conn_vals = nest.GetStatus(conns, ["target","weight"])
"""
