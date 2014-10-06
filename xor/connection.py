import random
class Connection:
    def __init__(self, a, b,w=0):
        self.from_n = a
        self.to_n = b
        if w == 0:
            self.weight_range = self.prange(-1,1,0.001)
            self.weight = self.weight_gen(1)*2 - 1
        else:
            self.weight = w

    def getFrom():
        return self.from_n

    def getTo():
        return self.to_n
    
    def getWeight():
        return self.weight

    def adjustWeight(self,deltaWeight):
        self.weight += deltaWeight

    def weight_gen(self,n):
        return self.weight_range[random.randint(0,len(self.weight_range)-1)]
        

    def prange(self,start,stop,step):
        vals = []
        r = start
        while r < stop:
            r = round(r,5)
            vals.append(r)
            r += step
        return vals
