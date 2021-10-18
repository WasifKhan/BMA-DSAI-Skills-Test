'''
Author: Wasif Khan
Purpose: Bermuda Monetary Authority DSAI Skills Test
Date: 17/10/2021
'''


from data_extractor.data_extractor import DataExtractor
from division_profiles.division_profiles import DivisionProfiles
from clusters.clusters import Clusters
from anomalies.anomalies import Anomalies

from time import time

start = time()
if __name__ == '__main__':
    data = DataExtractor()
    division_profiles = DivisionProfiles(data.dataset)
    clusters = Clusters(division_profiles)
    anomalies = Anomalies(division_profiles)
end = time()

print(f'Program took {str(end-start)[0:6]}s to execute')
