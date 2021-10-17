import pandas as pd

class DataExtractor:
    def __init__(self):
        self.initialize_dataset()
        self.load_data()
        self.extract_data()
        '''
        Do not need to clean data more than once
        Uncomment the line below if you need to generate the "data.xlsx" file
        '''
        self.clean_data()
        self.save_data()



    def initialize_dataset(self):
        self.features = ['Division', 'Transaction ID', 'Transaction Date', 'Card Posting Date',
            'Merchant Name', 'Transaction Amount', 'Transaction Currency', 'Original Amount',
            'Original Currency', 'G/L Account', 'G/L Account Description', 'Cost Centre',
            'Cost Centre Description', 'Merchant Type', 'Merchant Type Description', 'Purpose',
        ]
        self.words = ['Division', 'Merchant Name', 'G/L Account Description', 'Cost Centre Description', 'Merchant Type Description']


    def clean_data(self):
        for column in self.words:
            print(f'on feature: {column}')
            agg_data = self.dataset[column].value_counts()
            print(agg_data)
            print(f'len: {len(agg_data)}')
            same_candidates = agg_data.index[len(agg_data) -int(len(agg_data)*0.1):]
            real_values = agg_data.index[0:int(len(agg_data)*0.9)]
            for entry1 in same_candidates:
                best_candidate = None
                best_val = None
                for entry2 in real_values:
                    total_diff = self.is_same_entry(
                            self.word_to_datapoint(entry1),
                            self.word_to_datapoint(entry2))
                    if total_diff <= 0.2 and (not best_candidate or total_diff
                            < best_val):
                        best_candidate, best_val = entry2, total_diff
                if best_candidate:
                    print(f'replaced {entry1} with {best_candidate}')
                    self.dataset.replace(entry1, best_candidate, inplace=True)
            agg_data = self.dataset[column].value_counts()
            print(agg_data)
            print(f'len: {len(agg_data)}')

    def save_data(self):
        self.dataset.to_excel('data.xlsx')


    def is_same_entry(self, wc1, wc2):
        smaller, larger = (wc1, wc2) if sum(wc1) <= sum(wc2) else (wc2, wc1)
        total = sum(larger)
        if total == 0:
            return False
        total_diff = 0
        for i in range(26):
            total_diff += abs(smaller[i] - larger[i])
        print(f'total dif: {total_diff}/{total}')

        return total_diff/total


    def extract_data(self):
        from os import listdir
        dataset = None
        for filename in listdir('./data/'):
            datapoint = pd.read_excel(f'./data/{filename}')
            datapoint.set_axis(self.features, axis='columns', inplace=True)
            datapoint.dropna(inplace=True)
            if dataset is None:
                dataset = datapoint
            else:
                dataset = pd.concat([dataset, datapoint])
        self.dataset = dataset


    def load_data(self):
        self.dataset = pd.read_excel('data.xlsx')


    def analyze_features(self):
        features = [None]*16
        for dp in self.dataset.rows:
            if len(dp) != 16:
                print(f'bad DP: {dp}')
                break
            for i, feature in enumerate(dp):
                if not features[i]:
                    features[i] = {dp[i]: 1}
                elif dp[i] in features[i]:
                    features[i][dp[i]] += 1
                else:
                    features[i][dp[i]] = 1
        return features


    def word_to_datapoint(self, word):
        datapoint = [0] * 26
        for char in word:
            ID = ord(char.lower())
            if ID >= 97 and ID <= 122:
                datapoint[ID-97] += 1
        return datapoint


    def graph_sanitization_statistics(self):
        width = 0.8
        labels = ['Division', 'Merchant Name', 'G/L Account Description',
            'Cost Centre Description', 'Others']
        after_cleaning = [93, 85, 99, 94, 100]
        indicies = [0, 1, 2, 3, 4]
        fig, ax = plt.subplots()
        p1 = ax.bar(indicies, after_cleaning, width=0.5*width, color='b', alpha=0.5, label='Features')
        ax.bar_label(p1, label_type='center')
        ax.set_xticks(indicies)
        ax.set_xticklabels(labels)
        ax.set_ylabel('Precent Clean')
        ax.set_title('Cleanliness of Data Entries')
        ax.legend()
        fig.set_size_inches(14.5, 8.5)
        plt.show()
        plt.savefig('Cleaning Statistics.png')
