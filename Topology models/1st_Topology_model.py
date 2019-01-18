import nest

# four step to define a topology model
# 1- define layers
# 2- define connection profiles
# 3- connection layers
# 4- auxillary    (for visualization)

import nest.topology as topp

# for defining the layer dic the parameters are:
# elements         (one of the nest.Models())
# extent           (size of the model im mm)   (2D)
# rows
# columns
# center           (the center of grid or free layer to arravnge the frids independently)    (2D list)
# positions
# edge_wrap


# in elements any number of models could be positioned as a "composite layer"
"""
nest.CopyModel("iaf_psc_alpha","pyr")
nest.CopyModel("iaf_psc_alpha","inh", {"V_th": -52.0})
# co_layer = topp.CreateLayer({"rows":5,"columns":5,
            "elements": ["pyr",4,"inh",2,"poisson_generator","noise_generator"]   # 8 elements in same position
"""


# for define connection profile we need connection dictionary
# including 'connection_type' and 'mask'
"""
# Circular mask, gaussian kernel.
conn1 = { "connection_type":"divergent", 
          "mask": {"circular":{"radius":0.75}}, 
          "kernel": {"gaussian":{"p_center":1.0,"sigma":0.2}}, 
          "allow_autapses":False }
          
# Rectangular mask, constant kernel, non-centered anchor
conn2 = { "connection_type":"divergent", 
        "mask": {"rectangular":{"lower_left":[-0.5,-0.5],"upper_right":[0.5,0.5]}, "anchor": [0.5,0.5]},
        "kernel": 0.75, 
        "allow_autapses":False }
        
# Donut mask, linear kernel that decreases with distance # Commented out line would allow connection to target the pyr neurons (useful for ˓→
composite layers)
conn3 = { "connection_type": "divergent", 
        "mask": {"doughnut":{"inner_radius":0.1,"outer_radius":0.95}}, 
        "kernel": {"linear": {"c":1.,"a":-0.8}}, 
        "targets":"pyr"} 
        
# Rectangular mask, fixed number of connections, gaussian weights, linear delays
conn4 = { "connection_type":"divergent", 
        "mask": {"rectangular":{"lower_left":[-0.5,-0.5],"upper_right":[0.5,0.5]}},
        "number_of_connections": 40, 
        "weights": {"gaussian":{"p_center":J,"sigma":0.25}}, 
        "delays" : {"linear" :{"c":0.1,"a":0.2}}, 
        "allow_autapses":False }
"""

# all parameters are:

# connection_type                      (divergent,convergent)
# mask                                 (circular,rectangular,doughnut,grid)
# kernel                               (constant,uniform,linear,gaussian,exponential,guassian2D)
# weights                              (constant,uniform,linear,gaussian,exponential)
# delays                               (constant,uniform,linear,gaussian,exponential)
# synapse_model                        (any synapse model)
# sources
# targets
# number_of_connections                (integer)
# allow_multapses                      (True or False)
# allow_autapases




# and finally connections
"""
ex_layer = topp.CreateLayer({"rows":5,"columns":5,"elements":"iaf_psc_alpha"}) 
in_layer = topp.CreateLayer({"rows":4,"columns":4,"elements":"iaf_psc_alpha"}) 
conn_dict_ex = {"connection_type":"divergent",
                "mask":{"circular":{"radius":0.5}}} 
# And now we connect E->I 
topp.ConnectLayers(ex_layer,in_layer,conn_dict_ex)

# and with same info
conn_dict_in = {"connection_type":"divergent", 
                "mask":{"circular":{"radius":0.75}},"weights":-4.}
# And finish connecting the rest of the layers: Connect E->E
topp.ConnectLayers(ex_layer,ex_layer,conn_dict_ex) 
"""

