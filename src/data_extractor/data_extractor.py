class DataExtractor:
    def __init__(self):
        self.initialize_raw_data()
        self.extract_data()
        self.weighted_frequency()
        self.output_raw_data()

    def initialize_raw_data(self):
        self.raw_data = {'Division':{}, 'Transaction ID':{},
            'Transaction Date':{}, 'Card Posting Date':{},
            'Merchant Name':{}, 'Transaction Amount':{},
            'Transaction Currency':{}, 'Original Amount':{},
            'Original Currency':{}, 'G/L Account':{},
            'G/L Account Description':{}, 'Cost Centre':{},
            'Cost Centre Description':{}, 'Merchant Type':{},
            'Merchant Type Description':{}, 'Purpose':{},
        }

    def weighted_frequency(self):
        for key in self.raw_data:
            print(f'unique entries for {key}: {len(self.raw_data[key])}')

    def output_raw_data(self):
        print(sorted(self.raw_data['Transaction Date']))


    def extract_data(self):
        data_file = open('data.tsv', 'r')
        data_file.readline() #  Omit column names
        while data := data_file.readline().split('\t'):
            if data == ['']:
                break
            for i, key in enumerate(self.raw_data.keys()):
                if data[i] != '' and data[i] in self.raw_data[key]:
                    self.raw_data[key][data[i]] += 1
                elif data[i] != '':
                    self.raw_data[key][data[i]] = 1

        # Auxillary statistics work
        for key in self.raw_data:
            divisions = self.raw_data['Division']
            total = 0
            for division in divisions:
                if division == '':
                    continue
                total += divisions[division]
                print(f'{division}: {divisions[division]}')
            break
            '''
            for entry in self.raw_data[key]:
                print(f'{entry}: {self.raw_data[key][entry]}')
            '''
        print(f'total entries is: {total}')

    def word_to_datapoint(self, word):
        datapoint = [0] * 27
        for char in word:
            ID = ord(char.lower())
            if ID < 97 or ID > 122:
                datapoint[26] += 1
            else:
                datapoint[ID-97] += 1
        return datapoint
