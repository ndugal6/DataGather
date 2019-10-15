import math
import numpy as np

class FiveBox:
    def __init__(self, list):
        list.sort()
        self.data = np.array(list)
        self.min = self.max = self.med = self.q1 = self.q3 = 0
        self.computeValues()

    def computeValues(self):
        self.min = self.data[0]
        self.max = self.data[-1]
        self.med = self.data[math.floor(len(self.data) / 2)]
        self.q1 = self.data[math.floor(len(self.data) / 4)]
        self.q3 = self.data[math.floor(len(self.data) * .75)]

    def hasOutLiers(self):
        iqr = (self.q3 - self.q1) * 1.5
        uppers = self.data[self.data > (self.q3 + iqr)]
        lowers = self.data[self.data < (self.q3 - iqr)]
        return len(uppers) + len(lowers) > 0

def main():
    a = [1,2,3,4,5,6,7,8,9,10,11]
    box = FiveBox(a)
    # print(box.med)
    # print(box.q1)
    # print(box.q3)
    print(box.hasOutLiers())

if __name__ == '__main__': main()