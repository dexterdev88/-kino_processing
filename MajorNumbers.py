import pandas as pd

class MajorNumbers():
    
    def SubMajors(self, data):
        self.majors = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        self.major_acc = []
        self.major_sum = 0
        self.major_count = 0
        
        self.major_data = data
        
        for num in self.majors:
            if num in self.major_data:
                self.major_acc.append(num)
                self.major_sum += num
                self.major_count += 1
            else:
                self.major_acc.append(0)
        self.major_acc.append(self.major_count)
        self.major_acc.append(self.major_sum)
        
        return self.major_acc
    
    def GetMajors(self, data):
        self.majors_data = data
        
        if isinstance(self.majors_data, list):
            self.majors_res = self.SubMajors(self.majors_data)
        
        if isinstance(self.majors_data, pd.Series):
            self.majors_res = self.SubMajors(list(self.majors_data))
        
        if isinstance(self.majors_data, pd.DataFrame):
            self.majors_acc = []
            self.majors_cols = ['MAJ10','MAJ11','MAJ12','MAJ13','MAJ14','MAJ15','MAJ16','MAJ17','MAJ18','MAJ19','MAJ20','MAJ21','MAJ22','MAJ23','MAJ24','MAJ25','MAJOR_COUNT', 'MAJOR_SUM']
            for row, value in self.majors_data.iterrows():
                aux = self.SubMajors(list(value))
                self.majors_acc.append(aux)
            self.majors_res = pd.DataFrame(self.majors_acc)
            self.majors_res.columns = self.majors_cols
        
        return self.majors_res

'''
class MajorNumbers():
    def __init__(self):
        self.major_acc = []
        self.major_sum = 0
        self.major_count = 0
    
    def MajorNumber(self, data):
        self.major_data = data
        self.major_numbers = list(range(10,26))
        
        for num in self.major_numbers:
            if num in self.major_data:
                self.major_acc.append(num)
                self.major_sum += num
                self.major_count += 1
            else:
                self.major_acc.append(0)
        self.major_acc.append(self.major_count)
        self.major_acc.append(self.major_sum)
        return self.major_acc
    
    def GetMajorNumbers(self, data):
        self.majors_data = data
                
        if isinstance(self.majors_data, list):
            self.majors_res = self.MajorNumber(self.majors_data)
            
        if isinstance(self.majors_data, pd.Series):
            self.majors_res = self.MajorNumber(list(self.majors_data))
            
        if isinstance(self.majors_data, pd.DataFrame):
            self.majors_acc = []
            self.majors_cols = ['MAJ10', 'MAJ11', 'MAJ12', 'MAJ13', 'MAJ14', 'MAJ15', 'MAJ16', 'MAJ17', 'MAJ18', 'MAJ19', 'MAJ20', 'MAJ21', 'MAJ22', 'MAJ23', 'MAJ24', 'MAJ25', 'MAJ_COUNT', 'MAJ_SUM']
            for row, value in self.majors_data.iterrows():
                aux = self.MajorNumber(list(value))
                self.majors_acc.append(aux)
            self.majors_res = pd.DataFrame(self.majors_acc)
            self.majors_res.columns = self.majors_cols
        
        return self.majors_res
'''