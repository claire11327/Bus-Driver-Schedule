# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:40:37 2019

@author: user
"""

import json
import random
from operator import attrgetter

routeTime_data = [[],[],[],[],[],[],[]]


rD1 = open('data/route-cal_1.json', encoding = 'utf8')
rD2 = open('data/route-cal_2.json', encoding = 'utf8')
rD3 = open('data/route-cal_3.json', encoding = 'utf8')
rD4 = open('data/route-cal_4.json', encoding = 'utf8')
rD5 = open('data/route-cal_5.json', encoding = 'utf8')
rD6 = open('data/route-cal_6.json', encoding = 'utf8')
rD7 = open('data/route-cal_7.json', encoding = 'utf8')

routeTime_data[0] = json.load(rD1)
routeTime_data[1] = json.load(rD2)
routeTime_data[2] = json.load(rD3)
routeTime_data[3] = json.load(rD4)
routeTime_data[4] = json.load(rD5)
routeTime_data[5] = json.load(rD6)
routeTime_data[6] = json.load(rD7)





# record start & end time of bus route


class routeData_struct:
    def __init_(self):
        self.start = -1
        self.end = -1
        self.dur = -1
        self.sID = -1
        self.rID = -1
        self.dID = -1
        self.rC = -1
    def __str__(self):
        return  str(self.__dict__)

class driver_struct:
    def __init__(self):
        self.dID = -1
        self.end = 0
        self.work = [[],[],[],[],[],[],[]]
        self.dayoff = -1
        self.hasRest = 0
        self.status = -1
        self.workTime = 0
    def __str__(self):
        return  str(self.__dict__)
        



route_id = 0





# can change
driverNum = 150
stationNum = 8




RD = [[] for j in range(7)]

RDList = [[] for j in range(stationNum)]

# cal rest time
Dayoff = [[0,0,0,0,0,0,0] for j in range(stationNum)]
DayoffLast = [[0,0,0,0,0,0,0] for j in range(stationNum)]
routeA = [[0,0,0,0,0,0,0] for j in range(stationNum)] # [[7 days of this station]]
driverA = [0 for j in range(stationNum)]

# driver state
#[[],[]]
Driver = [[] for j in range(7)] # driver depart by station
DriverList = [[] for j in range(stationNum)] 
Work = []
WorkList = {}


# rest time
avaliableTime = 480 # 480 min
minRestTime = 10; # min
lunchBreak = 60;


# content number
contentNum = [{},{},{},{},{},{},{}]



# 7 times
for k in range(7):
    for i in range(len(routeTime_data[k])):
        contentNum[k][str(routeTime_data[k][i]['route_id'])] = len(routeTime_data[k][i]['content'])
        for j in range(len(routeTime_data[k][i]['content'])):    
            rd = routeData_struct()
            rd.start = routeTime_data[k][i]['content'][j]['time_from']
            rd.end   = routeTime_data[k][i]['content'][j]['time_to']
            rd.dur   = routeTime_data[k][i]['content'][j]['duration']
            rd.sID   = routeTime_data[k][i]['content'][j]['start_station']
            rd.rID   = routeTime_data[k][i]['route_id']
            rd.dID   = -1
            rd.rC    = routeTime_data[k][i]['content'][j]['route_combine']
            RDList[rd.sID].append(rd)
    RD[k] = RDList
    RDList = [[] for j in range(stationNum)]
 


for i in range(7):
    for j in range(len(RD[i])):
        RD[i][j].sort(key = lambda s: s.start)    






for i in range(7):
    print("Day ", i)
    for j in range(len(RD[i])):
        print("station ", j)
        for k in range(len(RD[i][j])):
            print(RD[i][j][k].start)



for i in range(7):
    for j in range(len(RD[i])):
        for k in range(len(RD[i][j])):
            
        DriverList[j] = WorkList
    Driver[i] = DriverList







'''
driverA = [45, 35, 23, 30, 10, 17, 6, 13]

print(sum(driverA))
# calcilate dayoff driver
        # doff each station each day dayoff 
        # total_doff this station dayoff num in 7 days
total_doff = 0
doff_amount = 0
for i in range(stationNum):
    total_doff = 0
    for j in range(7):
        if(sum(routeA[i]) == 0):
            doff_amount = 0
        else:
            doff_amount = round(driverA[i]*(routeA[i][j]/sum(routeA[i])))
        total_doff += doff_amount
        Dayoff[i][j] = doff_amount
        DayoffLast[i][j] = doff_amount
    if(total_doff < driverA[i]):
        for k in range(driverA[i]-total_doff):
            Dayoff[i][5-(k % 6)] += 1
            DayoffLast[i][5-(k % 6)] += 1
    elif(total_doff > driverA[i]):        
        for k in range(total_doff - driverA[i]):
            Dayoff[i][k % 6] -= 1
            DayoffLast[i][k % 6] -= 1

    


# init driver state
k = 0

Total_Driver = 0
for i in range(stationNum):
    k = 0
    for j in range(driverA[i]):
        dr = driver_struct()
        dr.dID = Total_Driver
        Total_Driver += 1
        if DayoffLast[i][k] == 0:
            for k in range(7):  
                if DayoffLast[i][k] != 0:
                    DayoffLast[i][k] -= 1
                    break
        else:
            DayoffLast[i][k] -= 1
        dr.dayoff = k    
        dr.end = 0
        dr.work = [[],[],[],[],[],[],[]]
        dr.hasRest = 0
        dr.status = -1
        dr.workTime = 0
        Driver[i].append(dr)    



for i in range(7):
    RD[i].sort(key = lambda s: s.start)

#for i in range(len(RD[0])):
#    print(RD[0][i].__dict__)

 '''   
    
'''
# cal

def greedy( dr, aT, mRT, lB, rD, wD, driverA):
    count = [0 for j in range(len(Driver))]
    global Total_Driver
    for i in range(len(rD)):
        last = 0
        cannotwork = 0
        
        #print(rand)
        for j in range(driverA[rD[i].sID]):            
            cannotwork = 0
            if dr[rD[i].sID][j].dayoff == wD:
                cannotwork = 1
                for kk in range(wD):
                    if dr[rD[i].sID][j].work[kk] == []:
                        dr[rD[i].sID][j].dayoff = kk
                        cannotwork = 0
                        break
                if cannotwork == 1:
                    if(j == driverA[rD[i].sID]-1):
                        last == -1
                #print("dID ",dr[rD[i].sID][j].dID,"dayoff ",dr[rD[i].sID][j].dayoff)
                # a day off for a week
                #continue
            elif dr[rD[i].sID][j].workTime >= aT-30: 
                cannotwork = 1
                if(j == driverA[rD[i].sID]-1):
                    last == -1       # 30 : min time for a shift
                # after aT, off work
                dr[rD[i].sID][j].status = 0
                #print("out of work")
                #continue
            elif (aT/2-dr[rD[i].sID][j].workTime) < min(rD[i].dur,70) and dr[rD[i].sID][j].hasRest == 0:
                cannotwork = 1
                if(j == driverA[rD[i].sID]-1):
                    last == -1
                dr[rD[i].sID][j].hasRest = 1
                dr[rD[i].sID][j].end += 60
                #continue
                # if aT/2-worktime < 70 & has not rest, then rest
                # at least a hour off after half of aS
                    # if driver Num available
            
                
            if cannotwork == 0 and (dr[rD[i].sID][j].end+10) < (rD[i].start):
                dr[rD[i].sID][j].end = (rD[i].dur+rD[i].start)
                dr[rD[i].sID][j].workTime += (rD[i].dur)
                dr[rD[i].sID][j].work[wD].append(i)  
                rD[i].dID = dr[rD[i].sID][j].dID
                break
            elif j == (driverA[rD[i].sID]-1+last):# and cannotwork == 1:
                count[rD[i].sID] += 1
                ## 加driver
                ## driver + Driver[rD[i].sID] 
                
    return dr, rD, driverA, count


for i in range(7):     
    Count = [0 for j in range(len(Driver))]
    #print("wD = ",i, "-----------------------------")
    for k in range(len(Driver)):
        for j in range(len(Driver[k])):
            Driver[k][j].end = 0
            Driver[k][j].hasRest = 0
            Driver[k][j].status = 0
            Driver[k][j].workTime = 0
    Driver, RD[i], driverA, Count = greedy( Driver, avaliableTime, minRestTime, lunchBreak, RD[i], i, driverA)
    print(Count)
    #print()
    
   
    


for j in range(len(RD)):
    wrap = []
    data = {}
    contentKeyNum = 0
    for key in range(len(contentNum[j])):
        data = {}
        data['route_id'] = key
        data['route_item'] = {}
        route_item = {}
        route_item['0'] = {}
        route_item['1'] = {}
        for i in range(contentNum[j][str(key)]):
            route_item['0'][str(i)] = RD[j][contentKeyNum].dID
            route_item['1'][str(i)] = RD[j][contentKeyNum].dID
            contentKeyNum += 1
        data['route_item'] = (route_item)
        #print(len(data['route_item']['0']))
        wrap.append(data)
        #print(wrap[0]['route_id'])
        filename = 'route_'+str(j)+'.json'
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(wrap, ensure_ascii=False, indent=4))

         


    
         

            
data = {}
for wD in range(7):
    data['date'] = str(wD)
    
    data['schedule'] = []
    bus_driver_schedule = []
    for i in range(len(DriverList)):
        bus_driver_schedule = []
        for k in range(len(DriverList[i].work[wD])):
            for l in range(len(RD[wD][DriverList[i].work[wD][k]].rC)):
                if RD[wD][DriverList[i].work[wD][k]].rC[l]["route_detail_id"] == -1:
                    continue
                bus_driver_schedule.append({
                    'route_id': RD[wD][DriverList[i].work[wD][k]].rID,
                    'route_item_id': RD[wD][DriverList[i].work[wD][k]].rC[l]["route_item_id"],
                    'route_detail_id': RD[wD][DriverList[i].work[wD][k]].rC[l]["route_detail_id"],
                })
        data['schedule'].append({
            'bus_driver_id': i,
            'bus_driver_schedule': bus_driver_schedule,
        })
    filename = "driver_"+str(wD)+".json"
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(data, ensure_ascii=False, indent=4))
'''