from data_extractor.data_extractor import DataExtractor
from division_profiles.division_profiles import DivisionProfiles
from clusters.clusters import Clusters
from anomalies.anomalies import Anomalies

if __name__ == '__main__':
    data = DataExtractor()
'''
    division_profiles = DivisionProfiles(data)
    clusters = Clusters(division_profiles)
    anomalies = Anomalies(division_profiles)

    data.visualize()
    division_profiles.visualize()
    clusters.visualize()
    anomalies.visualize()
'''
