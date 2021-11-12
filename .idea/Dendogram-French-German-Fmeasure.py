import plotly.figure_factory as ff
import numpy as np

fr_de_fmeasure = np.array([[0.60,0.60,0.55,0.42,0.31],
                           [0.60,0.60,0.38,0.28,0.22],
                           [0.60,0.60,0.60,0.60,0.60],
                           [0.60,0.60,0.60,0.60,0.60],
                           [0.60,0.60,0.60,0.56,0.51],
                           [0.24,0.24,0.24,0.23,0.31],
                           [0.24,0.24,0.24,0.24,0.19],
                           [0.60,0.60,0.60,0.56,0.51],
                           [0.60,0.60,0.34,0.14,0.07],
                           [0.60,0.60,0.60,0.55,0.37],
                           [0.60,0.60,0.60,0.60,0.60],
                           [0.05,0.04,0.04,0.02,0.01],
                           [0.60,0.60,0.60,0.60,0.58]])


names = ['Jaro', 'JaroWinkler', 'Levenshtein', 'Hamming', 'Ratio', 'PartialRatio', 'PartialTokenSort', 'TokenSort', 'Cosine', 'Dice', 'Jaccard', 'Overlap', 'Tversky']
fig = ff.create_dendrogram(fr_de_fmeasure, labels=names)
fig.update_layout(width=800, height=500)
fig.show()

import matplotlib.pyplot as plt

f = plt.figure()

plt.plot(range(10), range(10), "o")
plt.show()

