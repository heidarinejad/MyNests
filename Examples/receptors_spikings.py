import nest
import numpy as np
import matplotlib.pyplot as plt

# The neuron is bombarded with spike trains from four Poisson generators, which are connected to the AMPA, NMDA,
# GABA_A, and GABA_B receptors, respectively

nest.set_verbosity("M_WARNING")
nest.ResetKernel()

rate_in = 100.0
w_recep = {'AMPA': 30.0, 'NMDA': 30.0, 'GABA_A': 5.0, 'GABA_B': 10.0}
t_sim = 250.0
num_recep = len(w_recep)


nrn = nest.Create('ht_neuron')
p_gens = nest.Create('poisson_generator', 4, params={'rate': rate_in})
mm = nest.Create('multimeter',
params={'interval': 0.1,
        'record_from': ['V_m', 'theta', 'g_AMPA', 'g_NMDA', 'g_GABA_A', 'g_GABA_B',
                        'I_NaP', 'I_KNa', 'I_T', 'I_h']})


receptors = nest.GetDefaults('ht_neuron')['receptor_types']
for pg, (rec_name, rec_wgt) in zip(p_gens, w_recep.items()):
    nest.Connect([pg], nrn, syn_spec={'receptor_type': receptors[rec_name], 'weight': rec_wgt})

nest.Connect(mm, nrn)
nest.Simulate(t_sim)

data = nest.GetStatus(mm)[0]['events']
t = data['times']

def texify_name(name):
    return r'${}_{{\mathrm{{{}}}}}$'.format(*name.split('_'))

fig = plt.figure()
Vax = fig.add_subplot(311)
Vax.plot(t, data['V_m'], 'b', lw=2, label=r'$V_m$')
Vax.plot(t, data['theta'], 'g', lw=2, label=r'$\Theta$')
Vax.set_ylabel('Potential [mV]')