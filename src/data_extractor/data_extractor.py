import pandas as pd

class DataExtractor:
    def __init__(self):
        self.initialize_dataset()
        self.extract_data()


    def initialize_dataset(self):
        self.features = ['Division', 'Transaction ID', 'Transaction Date', 'Card Posting Date',
            'Merchant Name', 'Transaction Amount', 'Transaction Currency', 'Original Amount',
            'Original Currency', 'G/L Account', 'G/L Account Description', 'Cost Centre',
            'Cost Centre Description', 'Merchant Type', 'Merchant Type Description', 'Purpose',
        ]


    def extract_data(self):
        from os import listdir
        dataset = None
        for filename in listdir('./data/'):
            datapoint = pd.read_excel(f'./data/{filename}')
            self.analyze_feature_names(datapoint, filename)
            datapoint.set_axis(self.features, axis='columns', inplace=True)
            datapoint.dropna(inplace=True)
            if dataset is None:
                dataset = datapoint
            else:
                dataset = pd.concat([dataset, datapoint])
        self.dataset = dataset


    def analyze_feature_names(self, data, filename):
        columns = [None]*16
        for i, col in enumerate(data.columns):
            if not columns[i]:
                columns[i] = {col: [1, [filename]]}
            elif col in columns[i]:
                columns[i][col][0] += 1
                columns[i][col][1].append(filename)
            else:
                columns[i][col] = [1, [filename]]


    def word_to_datapoint(self, word):
        datapoint = [0] * 27
        for char in word:
            ID = ord(char.lower())
            if ID < 97 or ID > 122:
                datapoint[26] += 1
            else:
                datapoint[ID-97] += 1
        return datapoint
