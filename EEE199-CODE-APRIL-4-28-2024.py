import math
import botorch
import torch
from botorch.models import SingleTaskGP, ModelListGP
from gpytorch.mlls.exact_marginal_log_likelihood import ExactMarginalLogLikelihood
from botorch import fit_gpytorch_model
from botorch.aquisition.monte_carlo import qExpectedImprovement
from botorch.optim import optimize_acqf

class Vertex:
    def __init__(self, name, car_num, busy, speed, leng, source, dest):
        self.name = name  # Returns number of cars on path
        self.car_num = car_num  # Returns number of cars on path
        self.busy = busy  # Returns 1 if busy, 0 if free
        self.speed = speed  # Constant showing speed of cars in m/s
        self.leng = leng  # Constant showing length of path in meters
        self.source = source
        self.dest = dest

    def __str__(self):
        return f"{self.name}"


# Generation Vertices do not have source or dest attributes.
# 0 is given instead as a place holder

Cars_Passed = 0  # Number of Cars that have exited system
Time = float(0.0)  # Current Time

#generation vertices
K = Vertex("Katipunan", 0, 0,5, 100, 0, 0)  # Generation Vertex at LaVista
Gonza = Vertex("Gonza", 0, 0,5, 10,  0, 0)  # Generation Vertex at Gonzales
TDrive = Vertex( "TDrive",0, 0, 5, 10, 0, 0)  # Generation Vertex at Thornton Drive
K2S = Vertex("K2S", 0, 0, 5, 100, 0 , 0)  # Road between Katip-Gonza_TDrive and Katip-FDRosa-URd, Northbound
K2N = Vertex("K2N", 0, 0, 5, 100, 0, 0)  # Same as above, but southbound
FDRosa = Vertex("FDRosa", 0, 0, 5, 0, 0,0)  # Generation Vertex at FDRosa
K3 = Vertex("K3", 0, 0, 5, 100, 0,0)  # Generation at Aurora Katipunan
URd = Vertex("URd", 0, 0, 5, 10, 0,0)  # Combination of all four mini roads in the direction of Ateneo
Uturn = Vertex("Uturn", 0, 0, 5, 10, 0,0)

K_Gonza = Vertex("K_Gonza",0, 0, 5, 10, K, Gonza)  # Katip to Katip2
K_K2S = Vertex("K_K2S",0, 0, 5, 200, K, K2S)  # Katipu LaVista to Katipunan-FDRosa-URd Intersec
K_TDrive = Vertex("K_TDrive",0, 0, 5, 10, K, TDrive)  # Katip to Thornton
K_Uturn = Vertex("K_Uturn",0, 0, 5, 10, K, Uturn)  # Katip uturn to self

Gonza_K = Vertex("Gonza_K",0, 0, 5, 10, Gonza, K)  # Gonzales to Katip
Gonza_TDrive = Vertex("Gonza_TDrive",0, 0, 5, 10, Gonza, TDrive)  # Gonzales to Thornton Drive
Gonza_K2S = Vertex("Gonza_K2S",0, 0, 5, 10, Gonza, K2S)  # Gonzales to Katipunan-FDRosa-URd Intersec

TDrive_K = Vertex("TDrive_K",0, 0, 5, 10, TDrive, K)  # Thornton to Katip LaVista
TDrive_Gonza = Vertex("TDrive_Gonza",0, 0, 5, 10, TDrive, Gonza)  # TDrive to Gonza
TDrive_K2S = Vertex("TDrive_K2S",0, 0, 5, 10, TDrive, K2S)  # TDrive to Katipunan-FDRosa-URd Intersec

K2N_K = Vertex("K2N_K",0, 0, 5, 200, K2N, K)  # Road from Katip2 to Katip1
K2N_TDrive = Vertex("K2N_TDrive",0, 0, 5, 110, K2N, TDrive)  # Katip2 to Tdrive
K2S_URd = Vertex("K2S_URd",0, 0, 5, 110, K2S, URd)  # Katip2 to University Road
K2S_K2N = Vertex("K2S_K2N",0, 0, 5, 110, K2N, Uturn)  # Katip2 Uturn
K2N_K2S = Vertex("K2N_K2S",0, 0, 5, 110, K2N, Uturn)  # Katip2 Uturn
K2S_K3 = Vertex("K2S_K3",0, 0, 5, 200, K2S, K3)  # Katip2 to Katip3(Aurora)
K2S_FDRosa = Vertex("K2S_FDRosa",0, 0, 5, 110, K2S, FDRosa)  # Katip2 to FDRosa

FDRosa_K2N = Vertex("FDRosa_K2N",0, 0, 5, 110, FDRosa, K2N)  # FDRosa to K2
FDRosa_URd = Vertex("FDRosa_URd",0, 0, 5, 10, FDRosa, URd)  # FDRosa to University Road
FDRosa_K3 = Vertex("FDRosa_K3",0, 0, 5, 110, FDRosa, K3)  # FDRosa to K3

URd_K3 = Vertex("URd_K3",0, 0, 5, 10, URd, K3)  # University Road to K3 Southbound
URd_K2N = Vertex("URd_K2N",0, 0, 5, 10, URd, K2N) # University Road to K2 Northbound

K3_K2N = Vertex("K3_K2N",0, 0, 5, 200, K3, K2N)  # K3 to K2 Northbound
K3_URd = Vertex("K3_URd",0, 0, 5, 110, K3, URd)  # K3 to University Road

Roads = [K_Gonza, K_K2S, K_TDrive, K_Uturn, Gonza_K, Gonza_TDrive, Gonza_K2S,
         TDrive_K, TDrive_Gonza, TDrive_K2S, FDRosa_K2N, FDRosa_URd, FDRosa_K3,
         K2N_K, K2N_TDrive, K2S_URd, K2N_K2S, K2S_K2N, K2S_K3, K2S_FDRosa, K3_K2N, K3_URd] #list of the roads

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
    print("Number of Cars in K:")
    print(K.car_num)
    x = int(K.car_num)
    while x > 0:
        K_Gonza.car_num += int((Rate1 * K.car_num))
        x -= int((Rate1 * K.car_num))
        K.car_num -= int((Rate1 * K.car_num))

        K_K2S.car_num += int((Rate2 * K.car_num))
        x -= int((Rate2 * K.car_num))
        K.car_num -= int((Rate2 * K.car_num))

        K_TDrive.car_num += int((Rate3 * K.car_num))
        x -= int((Rate3 * K.car_num))
        K.car_num -= int((Rate3 * K.car_num))

        K_Uturn.car_num += int((Rate4 * K.car_num))
        x -= int((Rate4 * K.car_num))
        K.car_num -= int((Rate4 * K.car_num))

        if x > 0:
            x -= 1
            K.car_num += 1
    K.car_num = 0


def Distribute_K2N(Rate1, Rate2):
    print("Number of Cars in K2N:")
    print(K2N.car_num)
    x = int(K2N.car_num)
    while x > 0:
        r1 = int((Rate1 * K2N.car_num))
        K2N_TDrive.car_num += r1
        x -= r1
        K2N.car_num -= r1

        r2 = int((Rate2 * K2N.car_num))
        K2N_K.car_num += r2
        x -= r2
        K2N.car_num -= r2

        if x > 0:
            x -= 1
            K2N_K.car_num += 1
    K2N.car_num = 0


def Distribute_K2S(Rate1, Rate2, Rate4):
    print("Number of Cars in K2S:")
    print(K2S.car_num)
    x = int(K2S.car_num)
    while x > 0:
        r1 = int((Rate1 * K2S.car_num))
        K2S_K3.car_num += r1
        x -= r1
        K2S.car_num -= r1

        r2 = int((Rate2 * K2S.car_num))
        K2S_URd.car_num += r2
        x -= r2
        K2S.car_num -= r2

        r4 = int((Rate4 * K2S.car_num))
        K2S_K2N.car_num += r4
        x -= r4
        K2S.car_num -= r4

        if x > 0:
            x -= 1
            K2N_K.car_num += 1
    K2S.car_num = 0


def Evaluate_Busy(Green_Time):
    for i in range(len(Roads)): #go through all the lanes
        if Roads[i].busy == 1: #if the selected road is busy meaning there is a presence of car/s
            y = math.ceil(Green_Time / (Roads[i].leng / Roads[i].speed))  # Number of Cars that can pass through in green time
            Roads[i].car_num = Roads[i].car_num - y  # Remove from road
            if Roads[i].car_num < 0:  # Handles negative car number
                y = y + Roads[i].car_num #
                Roads[i].car_num = 0
            if Roads[i].dest == K2N or K2S:
                Roads[i].dest.car_num = Roads[i].dest.car_num + y
            if Roads[i].dest != K2N or K2S:
                global Cars_Passed
                Cars_Passed = Cars_Passed + y
        print(f"Road {Roads[i].name} has {Roads[i].car_num} cars")
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
    Set_Busy(K_Uturn)
    Set_Busy(TDrive_K2S)
    Set_Busy(TDrive_K)

    # Katip-Univ-F.dela
    Set_Busy(URd_K3)
    Set_Busy(URd_K2N)

def Phase_4():
    # Katip-B.Gon-Thornton
    Set_Busy(K_K2S)
    Set_Busy(K_TDrive)
    Set_Busy(K_Uturn)

    # Katip-Univ-F.dela
    Set_Busy(K2S_URd)
    Set_Busy(K2S_K2N)
    Set_Busy(K2S_K3)


def Unassert():
    for i in range(len(Roads)):
        Set_Stall(Roads[i])


#The function below is only for testing and isn't important for the full code
# Due to this, it is commented out
'''
def test_function(Green_Time):
    Total_Cars = 0
    for i in range(len(Roads)):
        Roads[i].car_num = 10
        print(f"Road {Roads[i].name} has {Roads[i].car_num} cars")
        Total_Cars = Total_Cars + Roads[i].car_num
    print("Total Cars:" + str(Total_Cars))
    print("------------------------------------" )
    i = 0
    while Cars_Passed < Total_Cars:
        print("Cycle:" + str(i+1))
        print("------------------------------------")
        Unassert()
        Phase_1()
        Evaluate_Busy(Green_Time)
        #Distribute_Katipunan(.25, 0.25, 0.25, 0.25)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.25, 0.25, 0.5)
        Unassert()
        Phase_2()
        Evaluate_Busy(Green_Time)
        #Distribute_Katipunan(.25, 0.25, 0.25, 0.25)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.25, 0.25, 0.5)
        Unassert()
        Phase_3()
        Evaluate_Busy(Green_Time)
        #Distribute_Katipunan(.25, 0.25, 0.25, 0.25)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.25, 0.25, 0.5)
        Unassert()
        Phase_4()
        Evaluate_Busy(Green_Time)
        #Distribute_Katipunan(.25, 0.25, 0.25, 0.25)
        Distribute_K2N(0.5, 0.5)
        Distribute_K2S(0.25, 0.25, 0.5)
        Unassert()
        print("Number of Cars Passed this Cycle:" + str(Cars_Passed))
        print("Time Passed This Cycle:" + str(Time))
    flow_rate = []
    flow_rate.append(float(Cars_Passed/ Time))
    print("Total Flow Rate:" + str(flow_rate))
    return torch.tensor(flow_rate)
'''


def target_function(GreenTime):
    global Cars_Passed = 0
    global Time = 0
    Total = 0
    for i in range(len(Roads)):
        if Roads[i].busy == 1:
            Total = Roads[i].car_num + Total
    Evaluate_Busy(GreenTime)
    flow_rate = []
    flow_rate.append(float(Cars_Passed / Time))
    print("Total Flow Rate:" + str(flow_rate))
    return torch.tensor(flow_rate)



def generate_initial_data(n): #This function generates the base data needed
    train_greentime = torch.rand(n,1)   #for bayesian optimization
    exact_obj = target_function(train_greentime).unsqueeze(-1)
    best_flowrate = exact_obj.max().item()
    return train_greentime, exact_obj, best_flowrate



def optimize_function(init_greentime, init_flowrate, best_flowrate, bnds, npts):
    single_model = SingleTaskGP(init_greentime, init_flowrate)
    mll = ExactMarginalLogLikelihood(single_model.likelihood, single_model)
    fit_gpytorch_model(mll)
    EI = qExpectedImprovement(single_model, best_flowrate)
    candidates,_ = optimize_acqf(
        acq_function = EI,
        bounds = bnds, #bounds
        q = npts, #Number of points we times we want to be suggested
        num_restarts = 200,
        raw_samples=512,
        options={"batch_limit":5, "maxiter":200}
        )
    return candidates

def optimization_loop(loops):
    init_greentime, init_flowrate, best_flowrate = generate_initial_data(30)
    boundaries = torch.tensor([15], [120])
    for i in range(loops):
        print(f"Number of optimization run: {i}")
        new_candidates = optimize_function(init_greentime, init_flowrate, best_flowrate, bnds, 1)
        new_results = target_function(new_candidates).unsqeeze(-1)
        
        print(f"The new Candidate is: {new_candidates}")
        init_greentime = torch.cat([init_greentime, new_candidates])
        init_flowrate = torch.cat([init_flowrate, new_candidates])
        best_flowrate = init_flowrate.max().items()
        
        print(f"Best Flow Rate Is: {best_flowrate}")
    

def helper(Diksyonaryo, phase):
    K2S.car_num = Diksyonaryo("Label")
    #Do for every road
    Unassert() # This happens only once
    if phase == 1:
        Phase_1()
    #Do for all phases
    optimization_loop(10)