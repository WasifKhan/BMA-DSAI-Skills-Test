class DataExtractor:
    def __init__(self):
        self.initialize_dataset()
        self.extract_data()

    def initialize_dataset(self):
        self.dataset = {'Division':{}, 'Transaction ID':{},
            'Transaction Date':{}, 'Card Posting Date':{},
            'Merchant Name':{}, 'Transaction Amount':{},
            'Transaction Currency':{}, 'Original Amount':{},
            'Original Currency':{}, 'G/L Account':{},
            'G/L Account Description':{}, 'Cost Centre':{},
            'Cost Centre Description':{}, 'Merchant Type':{},
            'Merchant Type Description':{}, 'Purpose':{},
        }


    def extract_data(self):
        data_file = open('data.tsv', 'r')
        while data := data_file.readline().split('\t'):
            if data == ['']:
                break
            for i, key in enumerate(self.dataset.keys()):
                if data[i] in self.dataset[key]:
                    self.dataset[key][data[i]] += 1
                else:
                    self.dataset[key][data[i]] = 1
        '''
        for key in self.dataset:
            print(f'{key}: {self.dataset[key]}')
        '''


    def word_to_datapoint(self, word):
        datapoint = [0] * 27
        for char in word:
            ID = ord(char.lower())
            if ID < 97 or ID > 122:
                datapoint[26] += 1
            else:
                datapoint[ID-97] += 1
        return datapoint
