from itertools import combinations
from random import randint
import pandas as pd

class Combinations():
    def __init__(self):
        self.cols = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07',
                     'B08', 'B09', 'B10', 'B11', 'B12', 'B13', 'B14']
        
    def RandomCombination(self):
        self.comb_acc = []
        
        while len(self.comb_acc) < 14:
            self.num = randint(1,26)
            if self.num not in self.comb_acc:
                self.comb_acc.append(self.num)
        
        return sorted(self.comb_acc)
        
    
    def AllCombinations(self):
        pass