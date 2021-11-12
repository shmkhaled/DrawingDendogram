import plotly.figure_factory as ff
import numpy as np

fr_de_precision = np.array([[0.64, 0.64, 0.53, 0.33, 0.22],
                            [0.64, 0.64, 0.29, 0.19, 0.14],
                            [0.64, 0.64, 0.64, 0.64, 0.64],
                            [0.64, 0.64, 0.64, 0.64, 0.64],
                            [0.64, 0.64, 0.64, 0.57, 0.46],
                            [0.15, 0.15, 0.14, 0.14, 0.2],
                            [0.15, 0.15, 0.15, 0.14, 0.11],
                            [0.64, 0.64, 0.64, 0.57, 0.46],
                            [0.64, 0.64, 0.25, 0.08, 0.04],
                            [0.64, 0.64, 0.64, 0.53, 0.28],
                            [0.64, 0.64, 0.64, 0.64, 0.64],
                            [0.02, 0.02, 0.02, 0.01, 0.01],
                            [0.64, 0.64, 0.64, 0.64, 0.6]])

names = ['Jaro', 'JaroWinkler', 'Levenshtein', 'Hamming', 'Ratio', 'PartialRatio', 'PartialTokenSort', 'TokenSort', 'Cosine', 'Dice', 'Jaccard', 'Overlap', 'Tversky']
fig = ff.create_dendrogram(fr_de_precision, labels=names)
fig.update_layout(width=800, height=500)
fig.show()

import matplotlib.pyplot as plt

f = plt.figure()

plt.plot(range(10), range(10), "o")
plt.show()

# f.savefig("foo3.pdf", bbox_inches='tight')