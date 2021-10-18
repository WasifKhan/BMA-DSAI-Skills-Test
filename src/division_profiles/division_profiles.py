import matplotlib.pyplot as plt
import pandas as pd


class DivisionProfile:
    def __init__(self, name):
        self.name = name

    @property
    def batch_trans_ID(self):
        count = self.ds[self.ds['Division'] == self.name].value_counts()
        x = division_count.index
        y = division_count.values
        self.graph_aggregate_stats(x[0:10], y[0:10], 'Division Statistics',
                'Number of Transactions',
                f'Number Of Transactions for {self.name}')
        return x, y

    @property
    def trans_date(self):
        count = self.ds[self.ds['Division'] == self.name].value_counts()
        x = division_count.index
        y = division_count.values
        self.graph_aggregate_stats(x[0:10], y[0:10], 'Division Statistics',
                'Number of Transactions',
                f'Number Of Transactions for {self.name}')
        return x, y

    @property
    def card_posting_date(self):
        count = self.ds[self.ds['Division'] == self.name].value_counts()
        x = division_count.index
        y = division_count.values
        self.graph_aggregate_stats(x[0:10], y[0:10], 'Division Statistics',
                'Number of Transactions',
                f'Number Of Transactions for {self.name}')
        return x, y


    @property
    def merchant_name(self):
        count = self.ds[self.ds['Division'] == self.name].value_counts()
        x = division_count.index
        y = division_count.values
        self.graph_aggregate_stats(x[0:10], y[0:10], 'Merchant Name Statistics',
                'Number of Transactions',
                f'Number Of Transactions for {self.name}')
        return x, y

    @property
    def g_l_account(self):
        count = self.ds[self.ds['Division'] == self.name].value_counts()
        x = division_count.index
        y = division_count.values
        self.graph_aggregate_stats(x[0:10], y[0:10], 'GL account Statistics',
                'Number of Transactions',
                f'Number Of Transactions for {self.name}')
        return x, y

    @property
    def g_l_account_description(self):
        count = self.ds[self.ds['Division'] == self.name].value_counts()
        x = division_count.index
        y = division_count.values
        self.graph_aggregate_stats(x[0:10], y[0:10], 'GL Account Description',
                'Number of Transactions',
                f'Number Of Transactions for {self.name}')
        return x, y

class DivisionProfiles:
    def __init__(self, dataset):
        self.ds = dataset
        self.graph_complex_statistics()


    def aggregate_statistics_bar(self):
        division_count = self.ds['Division'].value_counts()
        x = division_count.index
        y = division_count.values
        self.graph_aggregate_stats(x[0:10], y[0:10], 'Divisions',
                'Number of Transactions',
                'Number Of Transactions By Division (Top 10)')
        self.graph_aggregate_stats(x[20:], y[20:], 'Divisions',
                'Number of Transactions',
                'Number Of Transactions By Division (Bottom 50%)')


        division_transactions = self.ds.groupby(
                ['Division'])['Transaction Amount'].sum().sort_values(ascending=False)
        x = division_transactions.index[:10]
        y = division_transactions.values[:10]
        self.graph_aggregate_stats(x, y, 'Divisions',
                'Transaction Amount (CAD $)',
                'Transaction Amount By Division (Top 10)')

        normal_div_trans = (division_transactions /
                division_count).sort_values(ascending=False)
        x = normal_div_trans.index[0:10]
        y = normal_div_trans.values[0:10]
        self.graph_aggregate_stats(x, y, 'Divisions',
                'Transaction Amount (CAD $)',
                'Normalized Transaction Amount By Division (Top 10)')

    def graph_scatter(self, x, y, x_label, y_label, title):
        import numpy as np
        fig, ax = plt.subplots()
        colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(x))))
        for i, color in enumerate(colors):
            n=50
            x, y = np.random.rand(2, n)
            scale = 200.0 * np.random.rand(n)
            ax.scatter(x, y, c=color, s=scale, label=color,
                                   alpha=0.3, edgecolors='none')
        ax.legend()
        ax.grid(True)
        ax.set_xlabel(y_label, fontsize=25)
        ax.set_ylabel(x_label, fontsize=25)
        ax.set_title(title, fontsize=50)
        plt.show()
        plt.savefig(f'{title}.png')

    def graph_complex_statistics(self):
        data = {}
        self.divisions = list(self.ds['Division'].unique())
        self.ds['Year'] = self.ds['Transaction Date'].apply(lambda x:
                x.strftime('%Y'))
        for date_val in list(self.ds['Year'].unique()):
            summ = self.ds[self.ds['Year'] == date_val]
            summ = summ.groupby('Division').agg(
                {'Transaction Amount': 'sum'}).reset_index()
            to_map = []
            for division in self.divisions:
                try:
                    to_map.append(summ[summ['Division'] ==
                            division]['Transaction Amount'].iloc[0])
                except IndexError:
                    to_map.append(0)

            data[date_val] = to_map
        self.graph_aggregate_stats(data.keys(), data, 'Year',
                'Transaction Amounts', 'Aggregate Transaction Amounts',
                'sbar')
        division_GL = self.ds.groupby(
                ['Division', 'G/L Account'])['Transaction Amount'].sum().sort_values(ascending=False)
        print(division_GL)
        x = division_GL.index
        y = division_GL.values



    def graph_aggregate_stats(self, x, y, x_label, y_label,
            title, plot_type='barh'):
        print('got here')
        fig, ax = plt.subplots(figsize=(40,20))
        if plot_type == 'barh':
            ax.barh(x, y)
            ax.invert_yaxis()
        elif plot_type == 'line':
            ax.plot(x, y)
        elif plot_type == 'sbar':
            ax.invert_yaxis()
            division_count = len(self.divisions)
            for div_id in range(division_count):
                val = []
                for date in x:
                    val.append(y[date][div_id])
                ax.bar(x, val, width=0.35, label=self.divisions[div_id])

        ax.xaxis.set_tick_params(labelsize=14, pad=0)
        ax.yaxis.set_tick_params(labelsize=14, pad=0, rotation=30)
        ax.grid(b=True, color='black', linestyle='-.',
                linewidth=0.5, alpha=0.2)
        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.3,
                    str(round((i.get_width()), 2)),
                    fontsize=18, fontweight='bold',
                    color='black')
        ax.set_xlabel(y_label, fontsize=25)
        ax.set_ylabel(x_label, fontsize=25)
        ax.set_title(title, fontsize=50)
        ax.legend()
        plt.show()
        plt.savefig(f'{title}.png')


#def graph_time_series_stats(self, x, y, x_label, y_label, title):

