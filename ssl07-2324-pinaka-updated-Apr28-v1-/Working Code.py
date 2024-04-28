# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:00:41 2024

@author: Eurick Evardone
"""


class vertex:
    def __init___(self, car_num, busy, speed, leng, source, dest):
        self.car_num = car_num  # Returns number of cars on path
        self.busy = busy  # Returns 1 if busy, 0 if free
        self.speed = speed  # Constant showing speed of cars in m/s
        self.len = leng  # Constant showing length of path in meters
        self.source = source
        self.dest = dest


# Generation Vertices do not have source or dest attributes.
# 0 is given instead as a place holder

K = vertex(0, 0, 5, 10, 0, 0)  # Generation vertex at LaVista
Gonza = vertex(0, 0, 0, 10, 0, 0)  # Generation Vertex at Gonzales
TDrive = vertex(0, 0, 0, 10, 0, 0)  # Generation Vertex at Thornton Drive
K2 = vertex(0, 0, 5, 100, 0, 0)  # Road between Katip-Gonza_TDrive and Katip-FDRosa-URd
FDRosa = vertex(0, 0, 0, 10, 0, 0)  # Generation Vertex at FDRosa
K3 = vertex(0, 0, 5, 10, 0, 0)  # Generation at Aurora Katipunan
Uturn = "Special Node"
URd = "Exit Node Only"

K_Gonza = vertex(0, 0, 5, 10, K, Gonza)  # Katip to Katip2
K_K2 = vertex(0, 0, 5, 10, K, K2)  # Katipu LaVista to Katipunan-FDRosa-URd Intersec
K_TDrive = vertex(0, 0, 5, 10, K, TDrive)  # Katip to Thornton
K_Uturn = vertex(0, 0, 5, 10, K, Uturn)  # Katip uturn to self

Gonza = vertex(0, 0, 0, 10, 0, 0)  # Generation Vertex at Gonzales
Gonza_K = vertex(0, 0, 5, 10, Gonza, K)  # Gonzales to Katip
Gonza_TDrive = vertex(0, 0, 5, 10, Gonza, TDrive)  # Gonzales to Thornton Drive
Gonza_K2 = vertex(0, 0, 5, 10, Gonza, K2)  # Gonzales to Katipunan-FDRosa-URd Intersec

TDrive_K = vertex(0, 0, 5, 10, TDrive, K)  # Thornton to Katip LaVista
TDrive_Gonza = vertex(0, 0, 5, 10, TDrive, Gonza)  # TDrive to Gonza
TDrive_K2 = vertex(0, 0, 5, 10, TDrive, K2)  # TDrive to Katipunan-FDRosa-URd Intersec

K2_K = vertex(0, 0, 5, 10, K2, K)  # Road from Katip2 to Katip1
K2_TDrive = vertex(0, 0, 5, 10, K2, TDrive)  # Katip2 to Tdrive
K2_URd = vertex(0, 0, 5, 10, K2, URd)  # Katip2 to University Road
K2_Uturn = vertex(0, 0, 5, 10, K2, Uturn)  # Katip2 Uturn
K2_K3 = vertex(0, 0, 5, 10, K2, K3)  # Katip2 to Katip3(Aurora)
K2_FDRosa = vertex(0, 0, 5, 10, K2, FDRosa)  # Katip2 to FDRosa

FDRosa_K2 = vertex(0, 0, 5, 10, FDRosa, K2)  # FDRosa to K2
FDRosa_URd = vertex(0, 0, 5, 10, FDRosa, URd)  # FDRosa to University Road
FDRosa_K3 = vertex(0, 0, 5, 10, FDRosa, K3)  # FDRosa to K3

K3_K2 = vertex(0, 0, 5, 10, K3, K2)  # K3 to K2
K3_Urd = vertex(0, 0, 5, 10, K3, K2)  # K3 to University Road

Roads = [K_Gonza, K_K2, K_TDrive, K_Uturn, Gonza_K, Gonza_TDrive, Gonza_K2,
         TDrive_K, TDrive_Gonza, TDrive_K2, FDRosa_K2, FDRosa_URd, FDRosa_K3,
         K2_K, K2_TDrive, K2_URd, K2_Uturn, K2_K3, K2_FDRosa, K3_K2, K3_Urd]

Entrance_Nodes = [K, Gonza, TDrive, K3, FDRosa, ]
Exit_Nodes = [FDRosa, K, K3, URd, TDrive, Gonza]


def Set_Busy(vertex):
    if vertex.busy == 0:
        vertex.busy = 1
    else:
        pass


def Set_Stall(Vertex):
    if vertex.busy == 1:
        vertex.busy = 0
    else:
        pass

def Distribute_Katipunan(Rate1, Rate2, Rate3, Rate4):
    # Thia function distributes all the vehicles from the generation nodes
    x = int(K.car_num)
    while x > 0:
        K_Gonza.car_num = int((Rate1 * K_Gonza.car_num))
        x = x - int((Rate1 * K_Gonza.car_num))
        K_K2.car_num = int((Rate2 * K_Gonza.car_num))
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

def Evaluate_Path(Path, Green_Time):
    # This function evaluates the path selected
    # Assumes phase is in sync
    for i in Roads:
        if Roads(i).source == Path:
            x = (Green_Time / (Roads(i).leng / Roads(i).speed))
            Roads(i).car_num = Roads(i).car_num + int(x)
        elif Roads(i).dest == Path:
            y = (Green_Time / (Roads(i).leng / Roads(i).speed))
            Roads(i).car_num = Roads(i).car_num - int(y)
        else:
            pass

