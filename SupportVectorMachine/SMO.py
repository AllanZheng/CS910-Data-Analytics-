import numpy as np
import math
import os
class Train:
    def _init_(kwargs ):
        os.path.exists("../Sample_Data")

def select_Rand(i,m):
    b = i
    if(b == i):
        b = math.random(0,m)
        return b
def clipAlpha(low,high,alp):
    if(alp>high):
        alp = high
    if (alp<low):
        alp = low
    return alp

def simpleSMO(data,label,C,toler,maxIter):
    if()
    return