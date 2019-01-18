import nest
import nest.topology as tp

# for layer connections some terminologies are important should be taken to consider:
# Connection dictionary, Source, Target, Connection type, Convergent connection, Divergent connection
# Driver, Pool, Displacement, Distance, Mask, Kernel, Autapase and Multapse

# Connection type                    Driver                      Pool
#  Convergent                     Target Layer                Source Layer
#  Divergent                      Source Layer                Target Layer

# A mask describes which area of the pool layer shall be searched for nodes to connect for any given node in the driver layer.

# Any connection between layers through "ConnectLayers"  (Connection dictionary should at least provide the
# "connection_type" information

l= tp.CreateLayer({"rows":11,"columns":11, "extent": [11.0,11.0],
                "elements": "iaf_neuron"})
conn_dic={"connection_type": "divergent",
          "mask": {"rectangular": {"lower_left": [-2.0,-1.0],
                                   "upper_right": [2.0,1.0]}}}
tp.ConnectLayers(l,l,conn_dic)

# the above layer connection model is divergent, so it takes all nodes of Layer 'l' and connects it to all neighbor nodes inside the rectangular
# where the selected node is in center. (one by one)
# for the boundry nodes the number of connection decrease unless the periodic boundry condition is used