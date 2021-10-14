'''
from data_extractor.data_extractor import DataExtractor
from division_profiles.division_profiles import DivisionProfiles
from clusters.clusters import Clusters
from anomalies.anomalies import Anomalies

if __name__ == '__main__':
    data = DataExtractor()
    division_profiles = DivisionProfiles(data)
    clusters = Clusters(division_profiles)
    anomalies = Anomalies(division_profiles)

    data.visualize()
    division_profiles.visualize()
    clusters.visualize()
    anomalies.visualize()

'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

from os import walk


from os import listdir
counter = 0
columns = [None]*16
for filename in listdir('./data/'):
    counter += 1
    print(f'on file: {filename}')
    data = pd.read_excel(f'./data/{filename}')
    for i, col in enumerate(data.columns):
        if i < 16 and not columns[i]:
            columns[i] = [col]
        elif i < 16:
            columns[i].append(col)
for col in columns:
    print(col)

'''
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)

plt.title('About as simple as it gets, folks')
plt.plot(t, s)
plt.savefig('bla.png')
'''
