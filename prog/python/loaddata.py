def loaddata(setorder):
    if setorder == 1:
        RGVtime1step,RGVtime2step,RGVtime3step, \
        CNCtime1in1,CNCtime1in2,CNCtime2in2, \
        RGVtimeOddCNC,RGVtimeEvenCNC,RGVtimeclean \
        = 20,33,46,560,400,378,28,31,25
    elif setorder == 2:
        RGVtime1step,RGVtime2step,RGVtime3step, \
        CNCtime1in1,CNCtime1in2,CNCtime2in2, \
        RGVtimeOddCNC,RGVtimeEvenCNC,RGVtimeclean \
        =23,41,59,580,280,500,30,35,30
    elif setorder == 3:
        RGVtime1step,RGVtime2step,RGVtime3step, \
        CNCtime1in1,CNCtime1in2,CNCtime2in2, \
        RGVtimeOddCNC,RGVtimeEvenCNC,RGVtimeclean \
        =18,41,59,580,280,500,30,35,30

    return [RGVtime1step,RGVtime2step,RGVtime3step], \
           [CNCtime1in1,CNCtime1in2,CNCtime2in2], \
           [RGVtimeOddCNC,RGVtimeEvenCNC,RGVtimeclean]
