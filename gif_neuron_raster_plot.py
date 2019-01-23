import nest
import nest.raster_plot
import matplotlib.pyplot as plt

nest.ResetKernel()


dt = 0.1
simul_time = 2000.0

neuron_params = {"C_m": 83.1,
                 "g_L": 3.7,
                 "E_L": -67.0,
                 "Delta_V": 1.4,
                 "V_T_star": -39.6,
                 "t_ref": 4.0,
                 "V_reset": -36.7,
                 "lambda_0": 1.0,
                 "q_stc": [56.7, -6.9],
                 "tau_stc": [57.8, 218.2],
                 "q_sfa": [11.7, 1.8],
                 "tau_sfa": [53.8, 640.0],
                 "tau_syn_ex": 10.0,
                 }

N_ex = 100
P_ex = 0.3
W_ex = 30.0

N_noise = 50
rate_noise = 10.0
W_noise = 20.0

nest.SetKernelStatus({"resolution": dt})


population = nest.Create("gif_psc_exp", N_ex, params=neuron_params)
noise = nest.Create("poisson_generator", N_noise, params={'rate': rate_noise})
spike_det = nest.Create("spike_detector")


nest.Connect(population, population, {'rule': 'pairwise_bernoulli', 'p': P_ex}, syn_spec={"weight": W_ex})
nest.Connect(noise, population, 'all_to_all', syn_spec={"weight": W_noise})
nest.Connect(population, spike_det)

nest.Simulate(simul_time)


nest.raster_plot.from_device(spike_det, hist=True)
plt.title('Population dynamics')
plt.show()