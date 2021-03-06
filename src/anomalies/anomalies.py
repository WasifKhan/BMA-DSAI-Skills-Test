class Anomalies:
    def __init__(self, division_profiles):
        return None

    def generate_statistics(self):
        import numpy as np
        np.random.seed(123)
        all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
        bplot1 = axes[0].boxplot(all_data,
                                 vert=True,   
                                 patch_artist=True)   
        bplot2 = axes[1].boxplot(all_data,
                                 notch=True,  
                                 vert=True,   
                                 patch_artist=True)  
        colors = ['pink', 'lightblue', 'lightgreen']
        for bplot in (bplot1, bplot2):
            for patch, color in zip(bplot['boxes'], colors):
                patch.set_facecolor(color)
        for ax in axes:
            ax.yaxis.grid(True)
            ax.set_xticks([y+1 for y in range(len(all_data))], )
            ax.set_xlabel('xlabel')
            ax.set_ylabel('ylabel')
        plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
                 xticklabels=['x1', 'x2', 'x3', 'x4'])
        plt.show()
        plt.savefig('stats.png')
