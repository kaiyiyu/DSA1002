
# Towers of Hanoi

class Hanoi:
    
    count = 1       # used a global and could refactor more but it works! lol
    
    def __init__(self):
        pass
    
    def moveTower(self, disks, src, dest, aux):

        if disks == 1:
            self.moveDisk(src,dest)
        elif disks >= 1:
            self.moveTower(disks - 1, src, aux, dest)
            self.moveDisk(src, dest)
            self.moveTower(disks - 1, aux, dest, src)

    def moveDisk(self, src, dest):
        space = '  ' * (self.count - 1)     # (self.count - 1) just for better numbering and space for first level 
        print('[%s] %sMoved top disk from %s to %s.' % (self.count, space, src, dest))
        
        self.count += 1

first_test = Hanoi()
first_test.moveTower(4,"A","B","C")
