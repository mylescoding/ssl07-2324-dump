# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:06:24 2024

@author: Eurick Evardone
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:00:41 2024

@author: Eurick Evardone
"""


class Road:
    def __init__(self,name, busy, speed, leng):
        self.name = name  # Returns 1 if busy, 0 if free
        self.busy = busy  # Returns 1 if busy, 0 if free
        self.speed = speed  # Constant showing speed of cars in m/s
        self.leng = leng  # Constant showing length of path in meters

    def __str__(self):
        return f"{self.name}"

class Route:
    def __init__(self,car_num, source, dest):
        self.car_num = car_num  # Returns number of cars on path
        self.source = source
        self.dest = dest


# Generation Vertices do not have source or dest attributes.
# 0 is given instead as a place holder

Cars_Passed = int(0)  # Number of Cars that have exited system
Time = float(0.0)  # Current Time

K = Road("K", 0, 5, 10, 0, 0)  # Generation Vertex at LaVista
Gonza = Road("Gonza", 0, 0, 10, 0, 0)  # Generation Vertex at Gonzales
TDrive = Road("TDrive", 0, 0, 10, 0, 0)  # Generation Vertex at Thornton Drive
K2S = Road("K2S", 0, 5, 100, 0, 0)  # Road between Katip-Gonza_TDrive and Katip-FDRosa-URd, Northbound
K2N = Road("K2N", 0, 5, 100, 0, 0)  # Same as above, but southbound
FDRosa = Road("FDRosa", 0, 0, 10, 0, 0)  # Generation Vertex at FDRosa
K3 = Road("K3", 0, 5, 10, 0, 0)  # Generation at Aurora Katipunan
URd = Road("URd", 0, 5, 10, 0, 0)  # Combination of all four mini roads in the direction of Ateneo
Uturn = Road("Uturn", 0, 5, 10, 0, 0)

K_Gonza = Route(K, Gonza)  # Katip to Katip2
K_K2S = Vertex(0, 0, 5, 10, K, K2S)  # Katipu LaVista to Katipunan-FDRosa-URd Intersec
K_TDrive = Vertex(0, 0, 5, 10, K, TDrive)  # Katip to Thornton
K_Uturn = Vertex(0, 0, 5, 10, K, Uturn)  # Katip uturn to self

Gonza = Vertex(0, 0, 0, 10, 0, 0)  # Generation Vertex at Gonzales
Gonza_K = Vertex(0, 0, 5, 10, Gonza, K)  # Gonzales to Katip
Gonza_TDrive = Vertex(0, 0, 5, 10, Gonza, TDrive)  # Gonzales to Thornton Drive
Gonza_K2S = Vertex(0, 0, 5, 10, Gonza, K2S)  # Gonzales to Katipunan-FDRosa-URd Intersec

TDrive_K = Vertex(0, 0, 5, 10, TDrive, K)  # Thornton to Katip LaVista
TDrive_Gonza = Vertex(0, 0, 5, 10, TDrive, Gonza)  # TDrive to Gonza
TDrive_K2S = Vertex(0, 0, 5, 10, TDrive, K2S)  # TDrive to Katipunan-FDRosa-URd Intersec

K2N_K = Vertex(0, 0, 5, 10, K2N, K)  # Road from Katip2 to Katip1
K2N_TDrive = Vertex(0, 0, 5, 10, K2N, TDrive)  # Katip2 to Tdrive
K2S_URd = Vertex(0, 0, 5, 10, K2S, URd)  # Katip2 to University Road
K2S_K2N = Vertex(0, 0, 5, 10, K2N, Uturn)  # Katip2 Uturn
K2N_K2S = Vertex(0, 0, 5, 10, K2N, Uturn)  # Katip2 Uturn
K2S_K3 = Vertex(0, 0, 5, 10, K2S, K3)  # Katip2 to Katip3(Aurora)
K2S_FDRosa = Vertex(0, 0, 5, 10, K2S, FDRosa)  # Katip2 to FDRosa

FDRosa_K2N = Vertex(0, 0, 5, 10, FDRosa, K2N)  # FDRosa to K2
FDRosa_URd = Vertex(0, 0, 5, 10, FDRosa, URd)  # FDRosa to University Road
FDRosa_K3 = Vertex(0, 0, 5, 10, FDRosa, K3)  # FDRosa to K3

URd_K3 = Vertex(0, 0, 5, 10, URd, K3)
URd_K2N = Vertex(0, 0, 5, 10, URd, K2N)

K3_K2N = Vertex(0, 0, 5, 10, K3, K2N)  # K3 to K2
K3_URd = Vertex(0, 0, 5, 10, K3, URd)  # K3 to University Road

Roads = [K_Gonza, K_K2S, K_TDrive, K_Uturn, Gonza_K, Gonza_TDrive, Gonza_K2S,
         TDrive_K, TDrive_Gonza, TDrive_K2S, FDRosa_K2N, FDRosa_URd, FDRosa_K3,
         K2N_K, K2N_TDrive, K2S_URd, K2N_K2S, K2S_K2N, K2S_K3, K2S_FDRosa, K3_K2N, K3_URd]

Entrance_Nodes = [K, Gonza, TDrive, K3, FDRosa, URd]
Exit_Nodes = [FDRosa, K, K3, URd, TDrive, Gonza]


def Set_Busy(Vertex):
    if Vertex.busy == 0:
        Vertex.busy = 1
    else:
        pass


def Set_Stall(Vertex):
    if Vertex.busy == 1:
        Vertex.busy = 0
    else:
        pass


def Distribute_Katipunan(Rate1, Rate2, Rate3, Rate4):
    # Thia function distributes all the vehicles from the generation nodes
    x = int(K.car_num)
    while x > 0:
        K_Gonza.car_num = int((Rate1 * K_Gonza.car_num))
        x = x - int((Rate1 * K_Gonza.car_num))
        K_K2S.car_num = int((Rate2 * K_Gonza.car_num))
        x = x - int((Rate2 * K_Gonza.car_num))
        K_TDrive.car_num = int((Rate3 * K_Gonza.car_num))
        x = x - int((Rate3 * K_Gonza.car_num))
        K_Uturn.car_num = int((Rate4 * K_Gonza.car_num))
        x = x - int((Rate4 * K_Gonza.car_num))
        if x > 0:
            x = x - 1
            K_Gonza.car_num = K_Gonza.car_num + 1
        else:
            pass
    K.car_num = 0


def Distribute_K2N(Rate1, Rate2):
    x = int(K2N.car_num)
    while x > 0:
        K2N_TDrive.car_num = int((Rate1 * K2N_TDrive.car_num))
        x = x - int((Rate1 * K2N_TDrive.car_num))
        K2N_K.car_num = int((Rate2 * K2N_K.car_num))
        x = x - int((Rate2 * K2N_K.car_num))
        if x > 0:
            x = x - 1
            K2N_K.car_num = K2N_K.car_num + 1
        else:
            pass


def Distribute_K2S(Rate1, Rate2, Rate4):
    x = int(K2S.car_num)
    while x > 0:
        K2S_K3.car_num = int((Rate1 * K2S_K3.car_num))
        x = x - int((Rate1 * K2S_K3.car_num))
        K2S_URd.car_num = int((Rate2 * K2S_URd.car_num))
        x = x - int((Rate2 * K2S_URd.car_num))
        K2S_K2N.car_num = int((Rate4 * K2S_K2N.car_num))
        x = x - int((Rate4 * K2S_K2N.car_num))
        if x > 0:
            x = x - 1
            K2N_K.car_num = K2N_K.car_num + 1


def Evaluate_Busy(Green_Time):
    for i in range(len(Roads)):
        if Roads[i].busy == 1:
            y = (Green_Time / (Roads[i].leng / Roads[i].speed))  # Number of Cars that can pass through in green time
            Roads[i].car_num = Roads[i].car_num - int(y)  # Remove from road
            if Roads[i].car_num < 0:  # Handles negative car number
                y = y + Roads[i].car_num
                Roads[i].car_num = 0
            else:
                pass
            if Roads[i].dest == K2N or K2S:
                Roads[i].dest.car_num = Roads[i].dest.car_num + y
            else:
                global Cars_Passed
                Cars_Passed = Cars_Passed + y
        else:
            pass
    global Time
    Time = Time + Green_Time


def Phase_1():
    # Katip-B.Gon-Thornton
    Set_Busy(K_K2S)
    Set_Busy(K2N_K)
    Set_Busy(K2N_TDrive)

    # Katip-Univ-F.dela
    Set_Busy(K2S_K3)
    Set_Busy(K3_K2N)
    Set_Busy(K3_URd)


def Phase_2():
    # Katip-B.Gon-Thornton
    Set_Busy(Gonza_K)
    Set_Busy(Gonza_K2S)

    # Katip-Univ-F.dela
    Set_Busy(URd_K3)
    Set_Busy(FDRosa_K2N)
    Set_Busy(FDRosa_K3)
    Set_Busy(FDRosa_URd)


def Phase_3():
    # Katip-B.Gon-Thornton
    Set_Busy(K_Uturn)  # KS to KN
    Set_Busy(TDrive_K2S)
    Set_Busy(TDrive_K)

    # Katip-Univ-F.dela
    Set_Busy(URd_K3)
    Set_Busy(URd_K2N)


def Phase_4():
    # Katip-B.Gon-Thornton
    Set_Busy(K_K2S)
    Set_Busy(K_TDrive)

    # Katip-Univ-F.dela
    Set_Busy(K2S_URd)
    Set_Busy(K2S_K2N)
    Set_Busy(K2S_K3)


def Unassert():
    for i in range(len(Roads)):
        Set_Stall(Roads[i])


def main():
    for i in range(len(Roads)):
        Roads[i].car_num = 5
    i = 0
    while i < 3:
        Unassert()
        Phase_1()
        Evaluate_Busy(30)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.5, 0.25, 0.25)
        Unassert()
        Phase_2()
        Evaluate_Busy(30)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.5, 0.25, 0.25)
        Unassert()
        Phase_3()
        Evaluate_Busy(30)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.5, 0.25, 0.25)
        Unassert()
        Phase_4()
        Evaluate_Busy(30)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.5, 0.25, 0.25)
        Unassert()
        i = i + 1
    flow_rate = float(Cars_Passed / Time)
    print(flow_rate)


main()