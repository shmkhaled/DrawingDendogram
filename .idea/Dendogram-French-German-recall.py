import plotly.figure_factory as ff
import numpy as np

fr_de_recall = np.array([[0.56,0.56,0.56,0.56,0.56],
                         [0.56,0.56,0.56,0.56,0.56],
                         [0.56,0.56,0.56,0.56,0.56],
                         [0.56,0.56,0.56,0.56,0.56],
                         [0.56,0.56,0.56,0.56,0.56],
                         [0.73,0.73,0.73,0.73,0.73],
                         [0.73,0.73,0.73,0.73,0.73],
                         [0.56,0.56,0.56,0.56,0.56],
                         [0.56,0.56,0.56,0.67,0.78],
                         [0.56,0.56,0.56,0.56,0.56],
                         [0.56,0.56,0.56,0.56,0.56],
                         [0.73,0.73,0.73,0.73,0.78],
                         [0.56,0.56,0.56,0.56,0.56]])

names = ['Jaro', 'JaroWinkler', 'Levenshtein', 'Hamming', 'Ratio', 'PartialRatio', 'PartialTokenSort', 'TokenSort', 'Cosine', 'Dice', 'Jaccard', 'Overlap', 'Tversky']
fig = ff.create_dendrogram(fr_de_recall, labels=names)
fig.update_layout(width=800, height=500)
fig.show()

import matplotlib.pyplot as plt

f = plt.figure()

plt.plot(range(10), range(10), "o")
plt.show()

