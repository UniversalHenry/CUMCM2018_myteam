import numpy as np
from . import loaddata

class RGV:
    def __init__(self,time1step,time2step,time3step):
        self.timer = 0
        self.place = 0
        self.action = 0     #0,1,2,3 represent move to the place, 4 hold odd, 5 hold even ,6 clean
        self.thing =
        self.step = [time1step,time2step,time3step]



class CNC:


class Env:                  #our environment
    def __init__(self, setorder, num_process, contain_err):
        self.action_space.n = 7
        self.action_space = range(6)
        self.observation_space = np.zeros(18)

    def reset(self):
        self.__init__()

