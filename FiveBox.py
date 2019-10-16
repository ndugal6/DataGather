import math
import numpy as np


class FiveBox:
    def __init__(self, list_):
        self.min = self.max = self.med = self.q1 = self.q3 = self.iqr = 0
        self.data = list_

    def computeValues(self):
        self.min = self.__data[0]
        self.max = self.__data[-1]
        self.med = self.__data[math.floor(len(self.__data) / 2)]
        self.q1 = self.__data[math.floor(len(self.__data) / 4)]
        self.q3 = self.__data[math.floor(len(self.__data) * .75)]
        self.iqr = (self.q3 - self.q1) * 1.5

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, list_):
        list_.sort()
        self.__data = np.array(list_)
        self.computeValues()

    def hasOutLiers(self):
        return len(self.upperOutliers) + len(self.lowerOutliers) > 0

    @property
    def upperOutliers(self):
        return self.__data[self.__data > (self.q3 + self.iqr)]

    @property
    def lowerOutliers(self):
        return self.__data[self.__data < (self.q3 - self.iqr)]


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    box = FiveBox(a)
    # print(box.med)
    # print(box.q1)
    # print(box.q3)
    print(box.hasOutLiers())
    box.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1111]
    print(box.hasOutLiers())
    print(box.upperOutliers)


if __name__ == '__main__': main()
