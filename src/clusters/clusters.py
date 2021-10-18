
class Clusters:
    def __init__(self, division_profiles):
        self.apply_clustering_algorithms

    def apply_clustering_algorithms(self):
        from sklearn.datasets import load_digits
        from sklearn.decomposition import PCA
        from sklearn.cluster import KMeans
        import numpy as np
        data = load_digits().data
        pca = PCA(2)
        df = pca.fit_transform(data)
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters= 10)
        label = kmeans.fit_predict(df)
        u_labels = np.unique(label)
        for i in u_labels:
            plt.scatter(df[label == i , 0] , df[label == i , 1] , label = i)
        plt.legend()
        plt.show()
        plt.savefig('output.png')
