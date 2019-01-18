import nest
import nest.raster_plot

# repeat a stimulation protocol using the 'origin' property of devices
# actually 'poisson generator' generates a spike train which is recorded by 'spike detector'
# within each trial the poisson generator is active from 100ms to 500ms

rate = 1000.0    # generator rate in spikes/s
start = 100.0    # start of simulation relative to trial start, in ms
stop = 500.0     # end of simulation relative to trial start, in ms

trial_duration = 1000.0 # trial duration, in ms
num_trials = 5          # number of trials to perform


nest.ResetKernel()
pg = nest.Create('poisson_generator',
                 params={'rate': rate,
                         'start': start,
                         'stop': stop})

sd = nest.Create('spike_detector')
nest.Connect(pg, sd)

# 'origin' property of devices
for n in range(num_trials):
    nest.SetStatus(pg, {'origin': nest.GetKernelStatus()['time']})
    nest.Simulate(trial_duration)


nest.raster_plot.from_device(sd, hist=True, hist_binwidth=50.0,
                             title='Repeated stimulation by Poisson generator')