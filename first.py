import nest

from sklearn.svm import LinearSVC
from scipy.special import erf

print("heloooooo")

neuron=nest.Create("iaf_psc_alpha")
#neuron2=nest.Create("iaf_psc_alpha")     checking how the id numbers goes for nodes in order of creation
#voltmeter=nest.Create("voltmeter")
#neuron3=nest.Create("iaf_psc_alpha")


cu=nest.GetStatus(neuron, "I_e")
vth=nest.GetStatus(neuron, ["V_m", "V_th"])


multimeter=nest.Create("multimeter")
nest.SetStatus(multimeter, {"withtime": True, "record_from":["V_m"]})

nest.Connect(multimeter,neuron)

nest.Simulate(1000)


