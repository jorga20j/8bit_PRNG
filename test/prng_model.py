#PRNG model: 8 bit Xorshift
class Xorshift8bit:
    def __init__(self, seed):
        self.state = seed & 0xFF  #init state
    
    def next(self):
        x = self.state
        x ^= (x << 3) & 0xFF    #compute xorshift
        x ^= (x >> 5) & 0xFF    #compute xorshift
        x ^= (x << 4) & 0xFF    #compute xorshift
        self.state = x & 0xFF   #compute xorshift
        return self.state


