import numpy as np
from . import loaddata

def get_err_pro(time_1run):
    err_pro_1time = 0.01
    err_pro_1s = 1 - (1-err_pro_1time)**(1/(time_1run))
    return err_pro_1s

class CNC:
    def __init__(self,num_process,contain_err,CNCtime):
        self.timer = 0
        self.thing = 0
        if num_process == 1:
            self.processtime = [CNCtime[0]]
        if num_process == 2:
            self.processtime = [CNCtime[2]]

class RGV:
    def __init__(self,time1step,time2step,time3step,holdodd,holdeven,clean,num_process,contain_err,CNCtime):
        self.timer = 0
        self.place = 0
        self.action = 0     #0,1,2,3 represent move to the place, 4 hold odd, 5 hold even ,6 clean
        self.thing = -1
        self.steptime = [0,time1step,time2step,time3step]
        self.holdtime = [holdeven,holdodd]
        self.cleantime = clean
        self.CNC = [CNC(num_process,contain_err,CNCtime) for i in range(8)]

    def act(self):


class Env:                  #our environment
    def __init__(self, setorder, num_process, contain_err):
        self.action_space.n = 7
        self.action_space = range(6)
        self.observation_space = np.zeros(18)
        RGVtime1,CNCtime,RGVtime2 = loaddata(setorder)
        self.RGV = RGV(RGVtime1[0],GVtime1[1],GVtime1[2],
                       GVtime2[0],GVtime2[1],GVtime2[2],
                       num_process,contain_err,CNCtime)


    def reset(self):
        self.__init__()

