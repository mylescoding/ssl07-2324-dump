import math
import torch
from botorch.models import SingleTaskGP, ModelListGP
from gpytorch.mlls.exact_marginal_log_likelihood import ExactMarginalLogLikelihood
from botorch import fit_gpytorch_model
from botorch.acquisition.monte_carlo import qExpectedImprovement
from botorch.optim import optimize_acqf
import random


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



# generation vertices
#indiv roads
K = Vertex("Katipunan", 0, 0, 17, 406, 0, 0)  # Generation Vertex at LaVista
Gonza = Vertex("Gonza", 0, 0, 9, 300,  0, 0)  # Generation Vertex at Gonzales
TDrive = Vertex( "TDrive",0, 0, 14, 230, 0, 0)  # Generation Vertex at Thornton Drive
K2S = Vertex("K2S", 0, 0, 17, 178, 0 , 0)  # Road between Katip-Gonza_TDrive and Katip-FDRosa-URd, Northbound
K2N = Vertex("K2N", 0, 0, 17, 170, 0, 0)  # Same as above, but southbound
FDRosa = Vertex("FDRosa", 0, 0, 9, 243, 0,0)  # Generation Vertex at FDRosa
K3 = Vertex("K3", 0, 0, 17, 309, 0,0)  # Generation at Aurora Katipunan
URd = Vertex("URd", 0, 0, 14, 140, 0,0)  # Combination of all four mini roads in the direction of Ateneo
Uturn = Vertex("Uturn", 0, 0, 14, 10, 0,0)

#routes
K_Gonza = Vertex("K_Gonza",0, 0, 9, 7, K, Gonza)  # Katip to Katip2
K_K2S = Vertex("K_K2S",0, 0, 17, 7, K, K2S)  # Katipu LaVista to Katipunan-FDRosa-URd Intersec
K_TDrive = Vertex("K_TDrive",0, 0, 14, 7, K, TDrive)  # Katip to Thornton
K_Uturn = Vertex("K_Uturn",0, 0, 9, 7, K, Uturn)  # Katip uturn to self

Gonza_K = Vertex("Gonza_K",0, 0, 5, 7, Gonza, K)  # Gonzales to Katip
Gonza_TDrive = Vertex("Gonza_TDrive",0, 0, 5, 7, Gonza, TDrive)  # Gonzales to Thornton Drive
Gonza_K2S = Vertex("Gonza_K2S",0, 0, 5, 7, Gonza, K2S)  # Gonzales to Katipunan-FDRosa-URd Intersec

TDrive_K = Vertex("TDrive_K",0, 0, 14, 7, TDrive, K)  # Thornton to Katip LaVista
TDrive_Gonza = Vertex("TDrive_Gonza",0, 0, 9, 7, TDrive, Gonza)  # TDrive to Gonza
TDrive_K2S = Vertex("TDrive_K2S",0, 0, 14, 7, TDrive, K2S)  # TDrive to Katipunan-FDRosa-URd Intersec

K2N_K = Vertex("K2N_K",0, 0, 17, 7, K2N, K)  # Road from Katip2 to Katip1
K2N_TDrive = Vertex("K2N_TDrive",0, 0, 14, 7, K2N, TDrive)  # Katip2 to Tdrive
K2S_URd = Vertex("K2S_URd",0, 0, 14, 7, K2S, URd)  # Katip2 to University Road
K2S_K2N = Vertex("K2S_K2N",0, 0, 9, 7, K2N, Uturn)  # Katip2 Uturn
K2N_K2S = Vertex("K2N_K2S",0, 0, 9, 7, K2N, Uturn)  # Katip2 Uturn
K2S_K3 = Vertex("K2S_K3",0, 0, 17, 7, K2S, K3)  # Katip2 to Katip3(Aurora)
K2S_FDRosa = Vertex("K2S_FDRosa",0, 0, 14, 7, K2S, FDRosa)  # Katip2 to FDRosa

FDRosa_K2N = Vertex("FDRosa_K2N",0, 0, 9, 7, FDRosa, K2N)  # FDRosa to K2
FDRosa_URd = Vertex("FDRosa_URd",0, 0, 9, 7, FDRosa, URd)  # FDRosa to University Road
FDRosa_K3 = Vertex("FDRosa_K3",0, 0, 9, 7, FDRosa, K3)  # FDRosa to K3

URd_K3 = Vertex("URd_K3",0, 0, 14, 7, URd, K3)  # University Road to K3 Southbound
URd_K2N = Vertex("URd_K2N",0, 0, 14, 7, URd, K2N) # University Road to K2 Northbound

K3_K2N = Vertex("K3_K2N",0, 0, 17, 7, K3, K2N)  # K3 to K2 Northbound
K3_URd = Vertex("K3_URd",0, 0, 14, 7, K3, URd)  # K3 to University Road

Roads = [K_Gonza, K_K2S, K_TDrive, K_Uturn, Gonza_K, Gonza_TDrive, Gonza_K2S,
         TDrive_K, TDrive_Gonza, TDrive_K2S, FDRosa_K2N, FDRosa_URd, FDRosa_K3,
         K2N_K, K2N_TDrive, K2S_URd, K2N_K2S, K2S_K2N, K2S_K3, K2S_FDRosa, K3_K2N, K3_URd]  # list of the roads

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
    #print("Number of Cars in K:")
    #print(K.car_num)
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
    #print("Number of Cars in K2N:")
    #print(K2N.car_num)
    x = int(K2N.car_num)
    while x > 0:
        r1 = int((Rate1 * K2N.car_num).sum().item())
        K2N_TDrive.car_num += r1
        x -= r1
        K2N.car_num -= r1

        r2 = int((Rate2 * K2N.car_num).sum().item())
        if x >= r2:
            K2N_K.car_num += r2
            x -= r2
        else:
            K2N_K.car_num += x
            x = 0

        if x > 0:
            x -= 1
            K2N_K.car_num += 1
    K2N.car_num = 0


def Distribute_K2S(Rate1, Rate2, Rate4):
    #print("Number of Cars in K2S:")
    #print(K2S.car_num)
    x = int(K2S.car_num)
    while x > 0:
        r1 = int((Rate1 * K2S.car_num))
        K2S_K3.car_num += r1
        x -= r1
        K2S.car_num -= r1

        r2 = int((Rate2 * K2S.car_num))
        if x >= r2:
            K2S_URd.car_num += r2
            x -= r2
        else:
            K2S_URd.car_num += x
            x = 0

        r4 = int((Rate4 * K2S.car_num))
        if x >= r4:
            K2S_K2N.car_num += r4
            x -= r4
        else:
            K2S_K2N.car_num += x
            x = 0

        if x > 0:
            x -= 1
            K2N_K.car_num += 1
    K2S.car_num = 0


def Evaluate_Busy(Green_Time):
    for i in range(len(Roads)):  # go through all the lanes
        if Roads[i].busy == 1:  # if the selected road is busy meaning there is a presence of car/s
            y = torch.ceil(Green_Time / (Roads[i].leng / Roads[i].speed))[-1]  # Number of Cars that can pass through in green time
            Roads[i].car_num = Roads[i].car_num - y  # Remove from road
            if Roads[i].car_num.any() < 0:  # Handles negative car number
                y = y + Roads[i].car_num  #
                Roads[i].car_num = 0
            if Roads[i].dest == K2N or K2S:
                Roads[i].dest.car_num = Roads[i].dest.car_num + y
            if Roads[i].dest != K2N or K2S:
                global Cars_Passed
                Cars_Passed = Cars_Passed + y
        #print(f"Road {Roads[i].name} has {Roads[i].car_num} cars")
    global Time
    #print(f"Time: {Time} ")
    #print(f"Green_Time: {Green_Time} ")
    #Time = Time + Green_Time


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
    Set_Busy(K_Uturn)
    Set_Busy(K_K2S)
    Set_Busy(K_TDrive)

    # Katip-Univ-F.dela
    Set_Busy(K2S_URd)
    Set_Busy(K2S_K2N)
    Set_Busy(K2S_K3)


def Unassert():
    for i in range(len(Roads)):
        Set_Stall(Roads[i])



for_helper_phase = "phase 4 - kuf-green"
for_helper_dictionary = {'katip_t_nb_0_count': 0, 'katip_t_nb_1_count': 0, 'katip_t_nb_2_count': 0, 'katip_t_nb_3_count': 0, 'katip_t_sb_0_count': 0, 'katip_t_sb_1_count': 0, 'katip_t_sb_2_count': 0, 'katip_t_sb_3_count': 0, 'katip_t_sb_4_count': 0, 'thornton-drive-lower-out_0_count': 0, 'thornton-drive-in_0_count': 0, 'katip_m_u_nb_0_count': 0, 'katip_m_u_nb_1_count': 0, 'katip_m_u_nb_2_count': 0, 'katip_m_u_nb_3_count': 0, 'katip_m_l_nb_0_count': 0, 'katip_m_l_nb_1_count': 0, 'katip_m_l_nb_2_count': 0, 'b.gonzales-road_0_count': 0, 'b.gonzales-road_1_count': 0, 'katip_m_sb_0_count': 0, 'katip_m_sb_1_count': 0, 'katip_m_sb_2_count': 0, 'katip_m_sb_3_count': 0, 'katip_m_sb_4_count': 0, 'univ-road-upper-out_0_count': 0, 'univ-road-upper-in_0_count': 0, 'univ-road-lower-out_0_count': 0, 'univ-road-lower-in_0_count': 0, 'f.dela-rosa-road_1_count': 0, 'f.dela-rosa-road_0_count': 0, 'katip_b_sb_0_count': 0, 'katip_b_sb_1_count': 0, 'katip_b_sb_2_count': 0, 'katip_b_sb_3_count': 0, 'katip_b_sb_4_count': 0, 'katip_b_nb_0_count': 100, 'katip_b_nb_1_count': 100, 'katip_b_nb_2_count': 100}

def helper_function(phase,diksyonaryo):
    phase = phase.partition(" - ")[0]
    #Mid Katipunan to Top Katipunan
    K2N_K.car_num = diksyonaryo["katip_t_nb_0_count"]
    K2N_K.car_num += diksyonaryo["katip_t_nb_1_count"]
    K2N_K.car_num += diksyonaryo["katip_t_nb_2_count"]
    # Mid Katipunan to Thornton
    K2N_TDrive.car_num += diksyonaryo["katip_t_nb_3_count"]
    #Top Katipunan to Mid Katipunan
    K_K2S.car_num = diksyonaryo["katip_t_sb_0_count"]
    K_K2S.car_num += diksyonaryo["katip_t_sb_1_count"]
    K_K2S.car_num += diksyonaryo["katip_t_sb_2_count"]
    K_K2S.car_num += diksyonaryo["katip_t_sb_3_count"]
    # Top Katipunan U-turn
    K_Uturn.car_num += diksyonaryo["katip_t_sb_4_count"]
    # Thornton Drive (Divide divide)
    divide_thornton = int(diksyonaryo["thornton-drive-lower-out_0_count"] / 2)
    mod = diksyonaryo["thornton-drive-lower-out_0_count"] % 2
    TDrive_K.car_num = divide_thornton
    TDrive_K2S.car_num = divide_thornton
    random_number = random.randint(1, 2)
    if random_number == 1:
        TDrive_K.car_num += mod
    else:
        TDrive_K2S.car_num  += mod
    #From Mid Katipunan to Thornton Drive
    K2N_TDrive.car_num += diksyonaryo["thornton-drive-in_0_count"]
    K2N_TDrive.car_num += diksyonaryo["katip_m_u_nb_0_count"]
    #From Mid Katipunan Upper to Top Katipunan  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    K2N_TDrive.car_num += diksyonaryo["katip_m_u_nb_1_count"]
    K2N_TDrive.car_num += diksyonaryo["katip_m_u_nb_2_count"]
    K2N_TDrive.car_num += diksyonaryo["katip_m_u_nb_3_count"]
    # From Mid Katipunan Lower to Top Katipunan $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    K2N_TDrive.car_num += diksyonaryo["katip_m_l_nb_0_count"]
    K2N_TDrive.car_num += diksyonaryo["katip_m_l_nb_1_count"]
    K2N_TDrive.car_num += diksyonaryo["katip_m_l_nb_2_count"]
    #B.Gonzales to Mid Katipunan
    Gonza_K2S.car_num +=diksyonaryo["b.gonzales-road_0_count"]
####B. Gonzales Divide2x
    divide_gonza = int(diksyonaryo["b.gonzales-road_1_count"] / 2)
    mod = diksyonaryo["b.gonzales-road_1_count"] % 2
    TDrive_K.car_num = divide_gonza
    TDrive_K2S.car_num = divide_gonza
    random_number = random.randint(1, 2)
    if random_number == 1:
        # B.Gonzales to Top Katipunan
        Gonza_K2S.car_num += mod
    else:
        # B.Gonzales to Thornton Drive
        Gonza_TDrive.car_num += mod
    # From Mid Katipunan to Bottom Katipunan
    K2S_K3.car_num += diksyonaryo["katip_m_sb_0_count"]
    K2S_K3.car_num += diksyonaryo["katip_m_sb_1_count"]
    K2S_K3.car_num += diksyonaryo["katip_m_sb_2_count"]
    # From Mid Katipunan to University Drive
    K2S_URd.car_num +=diksyonaryo["katip_m_sb_3_count"]
    # From Mid Katipunan U-turn
    K2S_K2N.car_num+= diksyonaryo["katip_m_sb_4_count"]#
########University Road Upper Out Divide2x
    divide_urduo = int(diksyonaryo["univ-road-upper-out_0_count"] / 2)
    mod = diksyonaryo["univ-road-upper-out_0_count"] % 2
    URd_K2N.car_num = divide_urduo
    URd_K3.car_num = divide_urduo
    random_number = random.randint(1, 2)
    if random_number == 1:
        # University Road Upper Out to Mid Katipunan
        URd_K2N.car_num += mod
    else:
        # University Road Upper Out to Bottom Katipunan
        URd_K3.car_num  += mod
    # University Road Lower Out
    URd_K3.car_num= diksyonaryo["univ-road-lower-out_0_count"]
    # F.delaRosa to Mid Katip
    FDRosa_K2N.car_num += diksyonaryo["f.dela-rosa-road_1_count"]
######## F.delaRosa Divide2x
    divide_frosa = int(diksyonaryo["f.dela-rosa-road_0_count"] / 2)
    mod = diksyonaryo["f.dela-rosa-road_0_count"] % 2
    FDRosa_URd.car_num += divide_frosa
    FDRosa_K3.car_num += divide_frosa
    random_number = random.randint(1, 2)
    if random_number == 1:
        # F.delaRosa to University Road
        FDRosa_URd.car_num += mod
    else:
        # F.delaRosa to Bottom Katipunan
        FDRosa_K3.car_num += mod
    #did not include these v since exit node
    #'katip_b_sb_0_count': 4, 'katip_b_sb_1_count': 3, 'katip_b_sb_2_count': 7, 'katip_b_sb_3_count': 0, 'katip_b_sb_4_count': 0,

    # Bottom Katipunan to Mid Katipunan
    K3_K2N.car_num += diksyonaryo["katip_b_nb_1_count"]
    K3_K2N.car_num += diksyonaryo["katip_b_nb_2_count"]
    # Bottom Katipunan to Urd
    K3_URd.car_num += diksyonaryo["katip_b_nb_0_count"]
    Unassert()  # This happens only once
    x = int(15) #This is the minimum green time
    for i in range(len(Roads)):
        print("Number of cars in", Roads[i].name, ":", Roads[i].car_num)
    if phase == "phase 1":
        Phase_1()
        if (K_K2S.car_num == 0 and K2N_K.car_num == 0 and K2N_TDrive.car_num == 0 and K2S_K3.car_num == 0 and K3_K2N.car_num == 0 and K3_URd.car_num == 0):
            return x
    elif phase =="phase 2":
        if (Gonza_K.car_num == 0) and (Gonza_K2S.car_num == 0) and (URd_K3.car_num == 0) and (FDRosa_K2N.car_num == 0) and (FDRosa_K3.car_num == 0) and (FDRosa_URd.car_num == 0):
            return x
    elif phase == "phase 3":
        Phase_3()
        if (K_Uturn.car_num == 0 and TDrive_K2S.car_num ==  0 and TDrive_K.car_num == 0 and URd_K3.car_num == 0 and URd_K2N.car_num == 0):
            return x
    elif phase == "phase 4":
        Phase_4()
        if (K_Uturn.car_num == 0 and K_K2S.car_num == 0 and K_TDrive.car_num == 0 and K2S_URd.car_num == 0 and K2S_K2N.car_num == 0 and K2S_K3.car_num == 0):
            return x
    return optimization_loop(3) 


def target_function(train_greentime):
    # Standardize the input data
    mu = train_greentime.mean()
    sigma = train_greentime.std()
    std_train_greentime = (train_greentime - mu) / sigma
    Evaluate_Busy(train_greentime)

    flow_rate = Cars_Passed.item() / std_train_greentime
    #print("Total Flow Rate:" + str(flow_rate))
    return flow_rate.unsqueeze(-1)


def generate_initial_data(n):  # This function generates the base data needed
    train_greentime = torch.rand((n, 1), dtype=torch.float64)  # for bayesian optimization
    exact_obj = target_function(train_greentime)
    best_flowrate = exact_obj.max().item()
    return train_greentime, exact_obj.squeeze(-1), best_flowrate


def optimize_function(init_greentime, init_flowrate, best_flowrate, bnds, npts):
    single_model = SingleTaskGP(init_greentime, init_flowrate)
    mll = ExactMarginalLogLikelihood(single_model.likelihood, single_model)
    fit_gpytorch_model(mll)
    EI = qExpectedImprovement(single_model, best_flowrate)
    candidates, _ = optimize_acqf(
        acq_function=EI,
        bounds=bnds,  # bounds
        q=npts,  # Number of points we times we want to be suggested
        num_restarts=500,  # Increase the number of restarts
        raw_samples=1024,  # Increase the number of raw samples
        options={"batch_limit": 5, "maxiter": 200}
    )
    return candidates

def optimization_loop(loops):
    init_greentime, init_flowrate, best_flowrate = generate_initial_data(10)
    bnds = torch.tensor([[15.0], [120.0]], dtype=torch.float32)
    for i in range(loops):
        print(f"Number of optimization run: {i+1}")
        new_candidates = optimize_function(init_greentime, init_flowrate, best_flowrate, bnds, 1)
        new_results = target_function(new_candidates).unsqueeze(-1)

        print(f"The new best Green Time Candidate is: {new_candidates.item()}")
        init_greentime = torch.cat([init_greentime, new_candidates])
        init_flowrate = target_function(init_greentime).squeeze(-1)
        best_flowrate = init_flowrate.max().item()

        print(f"Best Flow Rate Is: {best_flowrate}")
    return new_candidates.item()


print("HOY ITO NA GREENTIME")
print(helper_function(for_helper_phase,for_helper_dictionary))