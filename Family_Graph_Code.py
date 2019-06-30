# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


df = pd.DataFrame({ 'from':[1,1,3,3,2,3,2,3,2,3,2,5,5,4,9,9,6,9,6,9,6,9,6,19,19,8,10,10,21,10,21,23,12,23,23,23,14,16,16,16,16,25,25,25,17,17,27], 'to':[3,5,2,4,4,9,9,11,11,13,13,15,17,7,6,19,19,10,10,23,23,16,16,8,18,18,21,31,31,20,20,12,22,22,14,33,33,25,35,24,26,35,24,26,27,29,29]})


carac = pd.DataFrame({ 'ID':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,31,33,35], 'myvalue':['group5','group5','group5','group8','group8','group5','group5','group5','group5','group5','group5','group8','group5','group8','group5','group8','group8','group8','group5','group5','group8','group8','group8','group8','group5','group5','group5','group8','group8','group5','group5'] })


G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph() )


G.nodes()
carac['myvalue']=pd.Categorical(carac['myvalue'])
carac['myvalue'].cat.codes
fig = plt.figure()


nx.draw(G, with_labels=True, node_color=carac['myvalue'].cat.codes, cmap=plt.cm.Set1, node_size=500)
fig.set_facecolor("#87CEEB")


