import nest
import nest.topology as tp


# for 2D layers
L1=tp.CreateLayer({"rows":5, "columns": 5,
                   "extent": [2.0,0.5],
                   "elements": "iaf_psc_alpha"})

# how to determine the center of layer with size of (ncd,nrd)
"""
nc, nr =5,3 
d = 0.1
l = tp.CreateLayer({"columns":nc, "rows": nr, "elements":"iaf_neuron",
                    "extent": [nc*d,nr*d], "center": [nc*d/2,0.0]})
                    
                    
# or we can make grid free structure
import numpy as np
pos = [[np.random.uniform(-0.5,0.5),np.random.uniform(-0.5,0.5)] for j in range(5)]
l=nest.CreateLayer({"positions": pos, "elements": "iaf_psc_alpha"})
"""



# for 3D layers
# for the NEST, layer is a special type of subnet
# NEST model type for grid base layers is : "topology_layer_grid"
#                 for grid free layers is : "topology_layer_free"

# to understand that printing the Network shows the info in desired depth
nest.PrintNetwork(depth=3)
# depth 1 is root dimension
# depth 2 is showing the model of layer
# depth 3 is showing the type of elements used inside the layer (it is also showing range of ID of elements)
# to understand run the below code
"""
L1=tp.CreateLayer({"rows":1, "columns": 2,
                   "elements": ["iaf_psc_alpha", 10, "poisson_generator",2, "noise_generator"]})
nest.PrintNetwork(depth=3)
"""


# to know status of the layer
print(nest.GetStatus(L1)[0]["topology"])




# how to create the layers with composite elements
"""
L1=tp.CreateLayer({"rows":5, "columns": 5,
                   "extent": [2.0,0.5],
                   "elements": ["iaf_psc_alpha", "poisson_generator"]})
"""