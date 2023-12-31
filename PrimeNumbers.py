import pandas as pd

class PrimeNumbers():
    
    def SubPrimes(self, data):
        self.primes = [2,3,5,7,11,13,17,19,23]
        self.prime_acc = []
        self.prime_sum = 0
        self.prime_count = 0
        
        self.prime_data = data
        
        for num in self.primes:
            if num in self.prime_data:
                self.prime_acc.append(num)
                self.prime_sum += num
                self.prime_count += 1
            else:
                self.prime_acc.append(0)
        self.prime_acc.append(self.prime_count)
        self.prime_acc.append(self.prime_sum)
        
        return self.prime_acc
    
    def GetPrimes(self, data):
        self.primes_data = data
        
        if isinstance(self.primes_data, list):
            self.prime_res = self.SubPrimes(self.primes_data)
        
        if isinstance(self.primes_data, pd.Series):
            self.primes_res = self.SubPrimes(list(self.primes_data))
        
        if isinstance(self.primes_data, pd.DataFrame):
            self.primes_acc = []
            self.prime_cols = ['PRIO2','PRI03','PRI05','PRI07','PRI11','PRI13','PRI17','PRI19','PRI23','PRIME_COUNT', 'PRIME_SUM']
            print('Buscando numeros primos')
            for row, value in self.primes_data.iterrows():
                aux = self.SubPrimes(list(value))
                self.primes_acc.append(aux)
            print('Finalizando')
            print('Creando dataframe')
            self.primes_res = pd.DataFrame(self.primes_acc)
            print('Asignando nombre de columnas al dataframe')
            print(self.primes_res.head())
            self.primes_res.columns = self.prime_cols
        
        return self.primes_res
    
    