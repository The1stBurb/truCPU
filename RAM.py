from register import REG
from allVars import ramSize
class RAM:
    def __init__(self):
        self.mem=[REG() for i in range(ramSize)]
    def build(self,mem):
        ad=0
        for i in mem:
            self.mem[ad].s=1
            self.mem[ad].st(i)
            self.mem[ad].s=0
            ad+=1
        return self
    def cur(self,addr):
        return self.mem[addr]
    def __repr__(self):
        return str([str(i.val)for i in self.mem])