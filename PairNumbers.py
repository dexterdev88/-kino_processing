import pandas as pd

class PairNumbers():
    
    def SubPairs(self, data):
        self.pair_data = data
        self.pairs = [2,4,6,8,10,12,14,16,18,20,22,24]
        self.pair_acc = []
        self.pair_sum = 0
        self.pair_count = 0
        
        for num in self.pairs:
            if num in data:
                self.pair_acc.append(num)
                self.pair_sum += num
                self.pair_count += 1
            else:
                self.pair_acc.append(0)
        self.pair_acc.append(self.pair_count)
        self.pair_acc.append(self.pair_sum)
        
        return self.pair_acc
    
    def GetPairs(self, data):
        self.pairs_data = data
        
        if isinstance(self.pairs_data, list):
            self.pairs_res = self.SubPairs(self.pairs_data)
        
        if isinstance(self.pairs_data, pd.Series):
            self.pairs_res = self.SubPairs(list(self.pairs_data))
        
        if isinstance(self.pairs_data, pd.DataFrame):
            self.pairs_acc = []
            self.pairs_cols = ['PARO2','PAR04','PAR06','PAR08','PAR10','PAR12','PAR14','PAR16','PAR18','PAR20','PAR22','PAR24','PAR_COUNT', 'PAR_SUM']
            for row, value in data.iterrows():
                aux = self.SubPairs(list(value))
                self.pairs_acc.append(aux)
            self.pairs_res = pd.DataFrame(self.pairs_acc)
            self.pairs_res.columns = self.pairs_cols
        
        return self.pairs_res