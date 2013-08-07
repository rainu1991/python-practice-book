class Reversed:
    def __init__(self, seq):
        self.seq = seq
	self.i = -1
	self.n = len(self.seq)
    def __len__(self):
        return len(self.seq)
    def next(self):
	 if self.i < self.n:
            i = self.i
            self.i += -1        
	    return self.seq[i]
	 else:
            raise StopIteration()


