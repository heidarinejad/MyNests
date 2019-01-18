import nest

ndic={"I_e":376.0, "tau_m": 20.0}
nest.CopyModel("iaf_psc_alpha","iaf_psc_alpha_fire")
nest.SetDefaults("iaf_psc_alpha_fire",ndic)
pop1=nest.Create("iaf_psc_alpha_fire", 10)

pop2 =nest.Create("iaf_psc_alpha",10)

syn_spec={"model": "stdp_synapse","weight":20.0, "delay":1.2}
conn_dict={"rule":"one_to_one"}


nest.Connect(pop1,pop2, conn_dict, syn_spec)


# above is the simple connecrtion of two population
# to access to synaptic information

conns1=nest.GetConnections(pop1)
conns2=nest.GetConnections(target=pop2)
conns3=nest.GetConnections(synapse_model="stdp_synapse")

# and values
con_val1=nest.GetStatus(conns1)
con_val2=nest.GetStatus(conns1,"weight")