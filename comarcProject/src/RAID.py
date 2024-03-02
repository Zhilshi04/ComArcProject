import math

class HDD:
    writeSpeed = 500
    readSpeed = 500
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
    def changeCapacity(self,capacity):
        self.capacity = capacity
    def changeName(self,name):
        self.name = name
    def getCapacity(self):
        return self.capacity
    def getName(self):
        return self.name
    def getWriteSpeed(self):
        return self.writeSpeed
    def getReadSpeed(self):
        return self.readSpeed

class RAID:
    RAID_LS = []
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def getLevel(self):
        return self.level
    def getName(self):
        return self.name
    def addHDD(self,HDD):
        self.RAID_LS.append(HDD)
    def getRAIDLS(self):
        return self.RAID_LS
    def getSUMcapacity(self):
        sum = 0
        min = 100000000
        for i in self.RAID_LS:
            if(i.getCapacity() < min):
                min = i.getCapacity()
        if(self.level == 0):
            if len(self.RAID_LS) <= 2:
                for i in self.RAID_LS:
                    sum += i.getCapacity()
                return sum
            else:
                return "RAID 0 Need 2 driver"
        elif(self.level == 1):
            if len(self.RAID_LS) >= 2:
                return ((len(self.RAID_LS)/2)*min)
            else:
                return "RAID 1 Need 2 driver"
        elif(self.level == 2):
            if len(self.RAID_LS) >= 3:
                return int(pow(2,math.log2(len(self.RAID_LS)+1)) - math.log2(len(self.RAID_LS)+1) -1 )
            else:
                return "RAID 2 Need 2 driver"
        elif(self.level == 3):
            if len(self.RAID_LS) >= 3:
                return ((len(self.RAID_LS)-1)*min)
            else:
                return "RAID 3 Need 3 driver"
        elif(self.level == 4):
            if len(self.RAID_LS) >= 3:
                return ((len(self.RAID_LS)-1)*min)      
            else:
                return "RAID 4 Need 3 driver"      
        elif(self.level == 5):
            if len(self.RAID_LS) >= 3:
                return ((len(self.RAID_LS)-1)*min)      
            else:
                return "RAID 5 Need 3 driver"      
        elif(self.level == 6):
            if len(self.RAID_LS) >= 4:
                return ((len(self.RAID_LS)-2)*min)
            else:
                return "RAID 6 Need 4 driver"

    
R1 = RAID('RAID0',5)
H1 = HDD('HDD1',2)
H2 = HDD('HDD2',2)
H3 = HDD('HDD3',2)
H4 = HDD('HDD4',1)
R1.addHDD(H1)
R1.addHDD(H2)
R1.addHDD(H3)
R1.addHDD(H4)
for i in R1.getRAIDLS():
    print(f'NAME HDD : {i.getName()} CAPACITY : {i.getCapacity()}TB ')

if isinstance(R1.getSUMcapacity(), int):
    print(f'{R1.getSUMcapacity()}TB')
else:
    print(f'{R1.getSUMcapacity()}')


    