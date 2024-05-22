import math

curr_phase = "Phase 0"
the_dict = {}


class Cell:
    def __init__(self, lane, length, max_speed, car_num, busy, tick):
        self.lane = lane
        self.busy = busy
        self.car_num = car_num
        self.arr = []
        self.cells = []
        self.delay = 0
        name = lane.split("-")
        shortname_dictionary = {
            " Lane 0": "L0_",
            " Lane 1": "L1_",
            " Lane 2": "L2_",
            " Lane 3": "L3_",
            " Lane 4": "L4_",
            "Upper Katipunan SB ": "K1_SB_",
            "Middle Katipunan SB ": "K2_SB_",
            "B. Gonzales Road ": "Bgon_",
            "F. dela Rosa Road ": "FdRosa_",
            "Middle Katipunan NB upper ": "K2_NB_R4_",
            "Middle Katipunan NB lower ": "K2_NB_R5R6_",
            "Lower Katipunan NB ": "K3_NB_",
            "Thornton Drive ": "TDrive_",
            " Lower": "lower_L0_",
            " Upper": "upper_L0_",
            " extension": "L0_",
            "University Road upper ": "URd_upper_",
            "University Road lower ": "URd_lower_",
            " Exit": "out_L0_"
        }
        road_lane_name = shortname_dictionary[name[0]] + shortname_dictionary[name[1]]

        for n in range(math.floor(length / (max_speed / tick))):
            self.arr.append((road_lane_name + "C" + str(n), 0, 0))
            self.cells.append(road_lane_name + "C" + str(n))
        self.arr_len = len(self.arr)


K1_SB_0 = Cell("Upper Katipunan SB - Lane 0", 400, 16.67, 0, 0, 1)
K1_SB_1 = Cell("Upper Katipunan SB - Lane 1", 400, 16.67, 0, 0, 1)
K1_SB_2 = Cell("Upper Katipunan SB - Lane 2", 400, 16.67, 0, 0, 1)
K1_SB_3 = Cell("Upper Katipunan SB - Lane 3", 400, 16.67, 0, 0, 1)
K1_SB_4 = Cell("Upper Katipunan SB - Lane 4", 400, 16.67, 0, 0, 1)

BGon_0 = Cell("B. Gonzales Road - Lane 0", 291, 8.33, 0, 0, 1)
BGon_1 = Cell("B. Gonzales Road - Lane 1", 291, 8.33, 0, 0, 1)

TDrive_lower = Cell("Thornton Drive - Lower", 56, 13.89, 0, 0, 1)
TDrive_upper = Cell("Thornton Drive - Upper", 36.72, 13.89, 0, 0, 1)
TDrive_extension = Cell("Thornton Drive - extension", 188.45, 13.89, 0, 0, 1)

K2_SB_0 = Cell("Middle Katipunan SB - Lane 0", 178.37, 16.67, 0, 0, 1)
K2_SB_1 = Cell("Middle Katipunan SB - Lane 1", 178.37, 16.67, 0, 0, 1)
K2_SB_2 = Cell("Middle Katipunan SB - Lane 2", 178.37, 16.67, 0, 0, 1)
K2_SB_3 = Cell("Middle Katipunan SB - Lane 3", 178.37, 16.67, 0, 0, 1)
K2_SB_4 = Cell("Middle Katipunan SB - Lane 4", 178.37, 16.67, 0, 0, 1)

K2_NB_R4_0 = Cell("Middle Katipunan NB upper - Lane 0", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_1 = Cell("Middle Katipunan NB upper - Lane 1", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_2 = Cell("Middle Katipunan NB upper - Lane 2", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_3 = Cell("Middle Katipunan NB upper - Lane 3", 33.4, 16.67, 0, 0, 1)

K2_NB_R5R6_0 = Cell("Middle Katipunan NB lower - Lane 0", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_1 = Cell("Middle Katipunan NB lower - Lane 1", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_2 = Cell("Middle Katipunan NB lower - Lane 2", 137.78, 16.67, 0, 0, 1)

FdRosa_0 = Cell("F. dela Rosa Road - Lane 0", 233.12, 8.33, 0, 0, 1)
FdRosa_1 = Cell("F. dela Rosa Road - Lane 1", 233.12, 8.33, 0, 0, 1)

URd_upper_out = Cell("University Road upper - Exit", 277, 13.89, 0, 0, 1)
URd_lower_out = Cell("University Road lower - Exit", 156.24, 13.89, 0, 0, 1)

K3_NB_0 = Cell("Lower Katipunan NB - Lane 0", 309.12, 16.67, 0, 0, 1)
K3_NB_1 = Cell("Lower Katipunan NB - Lane 1", 309.12, 16.67, 0, 0, 1)
K3_NB_2 = Cell("Lower Katipunan NB - Lane 2", 309.12, 16.67, 0, 0, 1)

Phase_1 = [K1_SB_0, K1_SB_1, K1_SB_2, K1_SB_3, K2_NB_R4_0, K2_NB_R4_1, K2_NB_R4_2, K2_NB_R4_3, K2_SB_0, K2_SB_1,
           K2_SB_2, K2_SB_3, K2_SB_4, K3_NB_0, K3_NB_1, K3_NB_2]

Phase_2 = [BGon_0, BGon_1, URd_lower_out, FdRosa_0, FdRosa_1]

Phase_3 = [K1_SB_4, TDrive_lower, URd_upper_out]

Phase_4 = [K1_SB_0, K1_SB_1, K1_SB_2, K1_SB_3, K1_SB_4, K2_SB_0, K2_SB_1, K2_SB_2, K2_SB_3, K2_SB_4]

network = [K1_SB_0, K1_SB_1, K1_SB_2, K1_SB_3, K1_SB_4, BGon_0, BGon_1, TDrive_lower, TDrive_upper, TDrive_extension,
           K2_SB_0, K2_SB_1, K2_SB_2, K2_SB_3, K2_SB_4, K2_NB_R4_0, K2_NB_R4_1, K2_NB_R4_2, K2_NB_R4_3, K2_NB_R5R6_0,
           K2_NB_R5R6_1, K2_NB_R5R6_2, FdRosa_0, FdRosa_1, URd_upper_out, URd_lower_out, K3_NB_0, K3_NB_1, K3_NB_2]

array = []


def read_input():  # test values only, should be integrated with TraCI
    # current_phase = "Phase 1"
    # traci_cell_dict = {'Bgon_L0_C0': (0, 0.0), 'Bgon_L0_C1': (0, 0.0), 'Bgon_L0_C10': (0, 0.0), 'Bgon_L0_C11': (0, 0.0), 'Bgon_L0_C12': (0, 0.0), 'Bgon_L0_C13': (0, 0.0), 'Bgon_L0_C14': (0, 0.0), 'Bgon_L0_C15': (0, 0.0), 'Bgon_L0_C16': (0, 0.0), 'Bgon_L0_C17': (0, 0.0), 'Bgon_L0_C18': (0, 0.0), 'Bgon_L0_C19': (0, 0.0), 'Bgon_L0_C2': (0, 0.0), 'Bgon_L0_C20': (0, 0.0), 'Bgon_L0_C21': (0, 0.0), 'Bgon_L0_C22': (0, 0.0), 'Bgon_L0_C23': (0, 0.0), 'Bgon_L0_C24': (0, 0.0), 'Bgon_L0_C25': (0, 0.0), 'Bgon_L0_C26': (0, 0.0), 'Bgon_L0_C27': (0, 0.0), 'Bgon_L0_C28': (0, 0.0), 'Bgon_L0_C29': (0, 0.0), 'Bgon_L0_C3': (0, 0.0), 'Bgon_L0_C30': (0, 0.0), 'Bgon_L0_C31': (0, 0.0), 'Bgon_L0_C32': (0, 0.0), 'Bgon_L0_C33': (1, 60.024009603841655), 'Bgon_L0_C4': (0, 0.0), 'Bgon_L0_C5': (0, 0.0), 'Bgon_L0_C6': (0, 0.0), 'Bgon_L0_C7': (0, 0.0), 'Bgon_L0_C8': (0, 0.0), 'Bgon_L0_C9': (0, 0.0), 'Bgon_L1_C0': (0, 0.0), 'Bgon_L1_C1': (0, 0.0), 'Bgon_L1_C10': (0, 0.0), 'Bgon_L1_C11': (1, 3.590571994379954), 'Bgon_L1_C12': (1, 18.738359578249035), 'Bgon_L1_C13': (0, 0.0), 'Bgon_L1_C14': (0, 0.0), 'Bgon_L1_C15': (0, 0.0), 'Bgon_L1_C16': (1, 60.02400960384144), 'Bgon_L1_C17': (0, 0.0), 'Bgon_L1_C18': (0, 0.0), 'Bgon_L1_C19': (3, 67.98823824561275), 'Bgon_L1_C2': (0, 0.0), 'Bgon_L1_C20': (3, 97.5736785213188), 'Bgon_L1_C21': (4, 96.35985804315592), 'Bgon_L1_C22': (4, 96.35897233483803), 'Bgon_L1_C23': (4, 123.98450393029295), 'Bgon_L1_C24': (2, 98.52706585155225), 'Bgon_L1_C25': (2, 98.78724909845958), 'Bgon_L1_C26': (4, 123.98458465577784), 'Bgon_L1_C27': (4, 150.7252945867473), 'Bgon_L1_C28': (6, 149.18259949101866), 'Bgon_L1_C29': (5, 122.77214143071329), 'Bgon_L1_C3': (1, 26.41056422569033), 'Bgon_L1_C30': (2, 98.7873146365294), 'Bgon_L1_C31': (5, 103.9871634769653), 'Bgon_L1_C32': (5, 137.9683102093113), 'Bgon_L1_C33': (4, 113.88810053846328), 'Bgon_L1_C4': (0, 0.0), 'Bgon_L1_C5': (0, 0.0), 'Bgon_L1_C6': (1, 40.81419514648115), 'Bgon_L1_C7': (1, 13.927701612222162), 'Bgon_L1_C8': (0, 0.0), 'Bgon_L1_C9': (0, 0.0), 'FdRosa_L0_C0': (0, 0.0), 'FdRosa_L0_C1': (0, 0.0), 'FdRosa_L0_C10': (0, 0.0), 'FdRosa_L0_C11': (0, 0.0), 'FdRosa_L0_C12': (0, 0.0), 'FdRosa_L0_C13': (0, 0.0), 'FdRosa_L0_C14': (0, 0.0), 'FdRosa_L0_C15': (0, 0.0), 'FdRosa_L0_C16': (0, 0.0), 'FdRosa_L0_C17': (0, 0.0), 'FdRosa_L0_C18': (0, 0.0), 'FdRosa_L0_C19': (0, 0.0), 'FdRosa_L0_C2': (0, 0.0), 'FdRosa_L0_C20': (1, 26.410564225690237), 'FdRosa_L0_C21': (0, 0.0), 'FdRosa_L0_C22': (0, 0.0), 'FdRosa_L0_C23': (0, 0.0), 'FdRosa_L0_C24': (1, 29.07181755982583), 'FdRosa_L0_C25': (3, 97.49562683776983), 'FdRosa_L0_C26': (4, 119.05080290132403), 'FdRosa_L0_C3': (0, 0.0), 'FdRosa_L0_C4': (0, 0.0), 'FdRosa_L0_C5': (0, 0.0), 'FdRosa_L0_C6': (0, 0.0), 'FdRosa_L0_C7': (1, 0.0), 'FdRosa_L0_C8': (1, 0.0), 'FdRosa_L0_C9': (0, 0.0), 'FdRosa_L1_C0': (0, 0.0), 'FdRosa_L1_C1': (0, 0.0), 'FdRosa_L1_C10': (0, 0.0), 'FdRosa_L1_C11': (0, 0.0), 'FdRosa_L1_C12': (0, 0.0), 'FdRosa_L1_C13': (0, 0.0), 'FdRosa_L1_C14': (0, 0.0), 'FdRosa_L1_C15': (0, 0.0), 'FdRosa_L1_C16': (0, 0.0), 'FdRosa_L1_C17': (0, 0.0), 'FdRosa_L1_C18': (0, 0.0), 'FdRosa_L1_C19': (0, 0.0), 'FdRosa_L1_C2': (0, 0.0), 'FdRosa_L1_C20': (0, 0.0), 'FdRosa_L1_C21': (0, 0.0), 'FdRosa_L1_C22': (0, 0.0), 'FdRosa_L1_C23': (1, 26.410564225690237), 'FdRosa_L1_C24': (0, 0.0), 'FdRosa_L1_C25': (2, 71.4666979420436), 'FdRosa_L1_C26': (3, 94.79980866059708), 'FdRosa_L1_C3': (0, 0.0), 'FdRosa_L1_C4': (0, 0.0), 'FdRosa_L1_C5': (0, 0.0), 'FdRosa_L1_C6': (0, 0.0), 'FdRosa_L1_C7': (0, 7.279891598330473), 'FdRosa_L1_C8': (0, 12.407983551729709), 'FdRosa_L1_C9': (0, 0.0), 'K1_SB_L0_C0': (0, 0.0), 'K1_SB_L0_C1': (0, 0.0), 'K1_SB_L0_C10': (1, 29.994001199760017), 'K1_SB_L0_C11': (0, 0.0), 'K1_SB_L0_C12': (0, 0.0), 'K1_SB_L0_C13': (0, 0.0), 'K1_SB_L0_C14': (1, 13.197360527894409), 'K1_SB_L0_C15': (1, 26.81729792001386), 'K1_SB_L0_C16': (5, 95.7736386852118), 'K1_SB_L0_C17': (6, 105.78338852974734), 'K1_SB_L0_C18': (3, 60.12517693427763), 'K1_SB_L0_C19': (4, 66.2695441215109), 'K1_SB_L0_C2': (1, 12.474251984790058), 'K1_SB_L0_C20': (1, 29.994001199760017), 'K1_SB_L0_C21': (1, 22.48645953882045), 'K1_SB_L0_C22': (2, 36.00184280071193), 'K1_SB_L0_C3': (0, 0.0), 'K1_SB_L0_C4': (0, 0.0), 'K1_SB_L0_C5': (0, 0.0), 'K1_SB_L0_C6': (0, 0.0), 'K1_SB_L0_C7': (0, 0.0), 'K1_SB_L0_C8': (1, 7.082788655263627), 'K1_SB_L0_C9': (1, 21.591476491707006), 'K1_SB_L1_C0': (1, 29.994001199760124), 'K1_SB_L1_C1': (0, 0.0), 'K1_SB_L1_C10': (0, 0.0), 'K1_SB_L1_C11': (0, 0.0), 'K1_SB_L1_C12': (1, 13.197360527894409), 'K1_SB_L1_C13': (0, 0.0), 'K1_SB_L1_C14': (0, 0.0), 'K1_SB_L1_C15': (1, 23.90756269492445), 'K1_SB_L1_C16': (4, 97.27016888622056), 'K1_SB_L1_C17': (4, 98.17731225541426), 'K1_SB_L1_C18': (3, 64.19601738741125), 'K1_SB_L1_C19': (2, 32.3181091494184), 'K1_SB_L1_C2': (0, 0.0), 'K1_SB_L1_C20': (1, 13.197360527894409), 'K1_SB_L1_C21': (4, 50.862264343854655), 'K1_SB_L1_C22': (3, 43.241081041194306), 'K1_SB_L1_C3': (0, 0.0), 'K1_SB_L1_C4': (1, 13.197360527894409), 'K1_SB_L1_C5': (0, 0.0), 'K1_SB_L1_C6': (0, 0.0), 'K1_SB_L1_C7': (0, 0.0), 'K1_SB_L1_C8': (0, 0.0), 'K1_SB_L1_C9': (1, 13.197360527894434), 'K1_SB_L2_C0': (0, 0.0), 'K1_SB_L2_C1': (0, 0.0), 'K1_SB_L2_C10': (1, 13.197360527894434), 'K1_SB_L2_C11': (0, 0.0), 'K1_SB_L2_C12': (0, 0.0), 'K1_SB_L2_C13': (1, 13.197360527894434), 'K1_SB_L2_C14': (0, 0.0), 'K1_SB_L2_C15': (3, 19.716632704621944), 'K1_SB_L2_C16': (8, 100.95313505471127), 'K1_SB_L2_C17': (6, 110.72738517722792), 'K1_SB_L2_C18': (10, 148.7529898173122), 'K1_SB_L2_C19': (5, 86.64117277253492), 'K1_SB_L2_C2': (1, 13.197360527894409), 'K1_SB_L2_C20': (4, 65.10317774717173), 'K1_SB_L2_C21': (4, 29.03171063797639), 'K1_SB_L2_C22': (3, 52.78555518593663), 'K1_SB_L2_C3': (1, 29.994001199760124), 'K1_SB_L2_C4': (0, 0.0), 'K1_SB_L2_C5': (1, 29.994001199760124), 'K1_SB_L2_C6': (1, 29.994001199760017), 'K1_SB_L2_C7': (0, 0.0), 'K1_SB_L2_C8': (0, 0.0), 'K1_SB_L2_C9': (0, 0.0), 'K1_SB_L3_C0': (1, 3.093038275743001), 'K1_SB_L3_C1': (1, 8.724598196962532), 'K1_SB_L3_C10': (1, 12.121009478852397), 'K1_SB_L3_C11': (1, 13.197360527894434), 'K1_SB_L3_C12': (1, 13.590338155864961), 'K1_SB_L3_C13': (1, 12.744394897524444), 'K1_SB_L3_C14': (0, 0.0), 'K1_SB_L3_C15': (1, 29.994001199760017), 'K1_SB_L3_C16': (3, 50.88240486549406), 'K1_SB_L3_C17': (12, 150.3758869368905), 'K1_SB_L3_C18': (8, 118.23780897745912), 'K1_SB_L3_C19': (3, 56.38872225554884), 'K1_SB_L3_C2': (1, 29.994001199760017), 'K1_SB_L3_C20': (2, 43.19136172765443), 'K1_SB_L3_C21': (5, 61.237584465923014), 'K1_SB_L3_C22': (3, 45.27394885809727), 'K1_SB_L3_C3': (0, 0.0), 'K1_SB_L3_C4': (0, 0.0), 'K1_SB_L3_C5': (1, 13.197360527894455), 'K1_SB_L3_C6': (0, 0.0), 'K1_SB_L3_C7': (1, 13.197360527894409), 'K1_SB_L3_C8': (0, 0.0), 'K1_SB_L3_C9': (1, 15.05355560813036), 'K1_SB_L4_C0': (1, 13.197360527894409), 'K1_SB_L4_C1': (0, 0.0), 'K1_SB_L4_C10': (0, 0.0), 'K1_SB_L4_C11': (0, 0.0), 'K1_SB_L4_C12': (0, 0.0), 'K1_SB_L4_C13': (0, 0.0), 'K1_SB_L4_C14': (6, 96.59119125898088), 'K1_SB_L4_C15': (7, 115.26959389531055), 'K1_SB_L4_C16': (7, 96.35747734862728), 'K1_SB_L4_C17': (6, 96.96896299651134), 'K1_SB_L4_C18': (6, 95.55574079981385), 'K1_SB_L4_C19': (3, 48.20724365876429), 'K1_SB_L4_C2': (0, 0.0), 'K1_SB_L4_C20': (3, 39.546014677489296), 'K1_SB_L4_C21': (3, 39.39819648027971), 'K1_SB_L4_C22': (2, 43.19136172765443), 'K1_SB_L4_C3': (0, 0.0), 'K1_SB_L4_C4': (0, 0.0), 'K1_SB_L4_C5': (0, 0.0), 'K1_SB_L4_C6': (0, 0.0), 'K1_SB_L4_C7': (0, 0.0), 'K1_SB_L4_C8': (1, 24.82269204670617), 'K1_SB_L4_C9': (1, 3.8515731002641607), 'K2_NB_R4_L0_C0': (5, 97.57477385314353), 'K2_NB_R4_L0_C1': (5, 106.45376854331371), 'K2_NB_R4_L1_C0': (5, 110.60943852167262), 'K2_NB_R4_L1_C1': (6, 106.02767324749097), 'K2_NB_R4_L2_C0': (6, 110.77269080757239), 'K2_NB_R4_L2_C1': (8, 132.3027100400295), 'K2_NB_R4_L3_C0': (2, 38.96313703720198), 'K2_NB_R4_L3_C1': (7, 119.04526128313395), 'K2_NB_R5R6_L0_C0': (0, 0.0), 'K2_NB_R5R6_L0_C1': (0, 0.0), 'K2_NB_R5R6_L0_C2': (0, 0.0), 'K2_NB_R5R6_L0_C3': (0, 0.0), 'K2_NB_R5R6_L0_C4': (0, 0.0), 'K2_NB_R5R6_L0_C5': (0, 0.0), 'K2_NB_R5R6_L0_C6': (0, 0.0), 'K2_NB_R5R6_L0_C7': (0, 0.0), 'K2_NB_R5R6_L1_C0': (0, 0.0), 'K2_NB_R5R6_L1_C1': (0, 0.0), 'K2_NB_R5R6_L1_C2': (0, 0.0), 'K2_NB_R5R6_L1_C3': (0, 0.0), 'K2_NB_R5R6_L1_C4': (0, 0.0), 'K2_NB_R5R6_L1_C5': (0, 0.0), 'K2_NB_R5R6_L1_C6': (0, 0.0), 'K2_NB_R5R6_L1_C7': (0, 0.0), 'K2_NB_R5R6_L2_C0': (0, 0.0), 'K2_NB_R5R6_L2_C1': (0, 0.0), 'K2_NB_R5R6_L2_C2': (0, 0.0), 'K2_NB_R5R6_L2_C3': (0, 0.0), 'K2_NB_R5R6_L2_C4': (0, 0.0), 'K2_NB_R5R6_L2_C5': (0, 0.0), 'K2_NB_R5R6_L2_C6': (0, 0.0), 'K2_NB_R5R6_L2_C7': (0, 0.0), 'K2_SB_L0_C0': (0, 0.0), 'K2_SB_L0_C1': (1, 8.596309539045006), 'K2_SB_L0_C2': (1, 3.3413029384594872), 'K2_SB_L0_C3': (1, 29.904306220095712), 'K2_SB_L0_C4': (0, 0.0), 'K2_SB_L0_C5': (0, 0.0), 'K2_SB_L0_C6': (0, 0.0), 'K2_SB_L0_C7': (0, 0.0), 'K2_SB_L0_C8': (2, 22.824715568597302), 'K2_SB_L0_C9': (4, 45.336842986029815), 'K2_SB_L1_C0': (1, 29.994001199760035), 'K2_SB_L1_C1': (0, 0.0), 'K2_SB_L1_C2': (1, 21.737455864330723), 'K2_SB_L1_C3': (1, 7.283629385724981), 'K2_SB_L1_C4': (1, 29.994001199760046), 'K2_SB_L1_C5': (0, 0.0), 'K2_SB_L1_C6': (1, 28.37684449489218), 'K2_SB_L1_C7': (0, 0.0), 'K2_SB_L1_C8': (2, 26.55401327700664), 'K2_SB_L1_C9': (1, 30.469226081657517), 'K2_SB_L2_C0': (0, 0.0), 'K2_SB_L2_C1': (1, 13.19736052789442), 'K2_SB_L2_C2': (1, 13.19736052789442), 'K2_SB_L2_C3': (1, 13.001182469411384), 'K2_SB_L2_C4': (0, 0.0), 'K2_SB_L2_C5': (1, 16.71617485395306), 'K2_SB_L2_C6': (2, 38.268570417547146), 'K2_SB_L2_C7': (2, 13.403229761943432), 'K2_SB_L2_C8': (3, 56.90072639225181), 'K2_SB_L2_C9': (1, 30.156815440289503), 'K2_SB_L3_C0': (0, 0.0), 'K2_SB_L3_C1': (1, 13.19736052789442), 'K2_SB_L3_C2': (0, 0.0), 'K2_SB_L3_C3': (0, 0.0), 'K2_SB_L3_C4': (1, 26.756126659239506), 'K2_SB_L3_C5': (1, 10.976326850058635), 'K2_SB_L3_C6': (0, 0.0), 'K2_SB_L3_C7': (1, 29.994001199760046), 'K2_SB_L3_C8': (0, 0.0), 'K2_SB_L3_C9': (3, 57.45721271393642), 'K2_SB_L4_C0': (0, 0.0), 'K2_SB_L4_C1': (0, 0.0), 'K2_SB_L4_C2': (0, 0.0), 'K2_SB_L4_C3': (0, 0.0), 'K2_SB_L4_C4': (0, 0.0), 'K2_SB_L4_C5': (0, 0.0), 'K2_SB_L4_C6': (0, 0.0), 'K2_SB_L4_C7': (0, 0.0), 'K2_SB_L4_C8': (0, 0.0), 'K2_SB_L4_C9': (0, 0.0), 'K3_NB_L0_C0': (0, 0.0), 'K3_NB_L0_C1': (1, 18.480552794925543), 'K3_NB_L0_C10': (6, 96.96905422253292), 'K3_NB_L0_C11': (8, 123.36394734670463), 'K3_NB_L0_C12': (5, 97.5757208663836), 'K3_NB_L0_C13': (7, 123.59003231868945), 'K3_NB_L0_C14': (5, 97.57552379554869), 'K3_NB_L0_C15': (5, 80.77864807131492), 'K3_NB_L0_C16': (8, 123.36456052543063), 'K3_NB_L0_C17': (4, 95.12048416483967), 'K3_NB_L0_C2': (1, 9.233904313652781), 'K3_NB_L0_C3': (1, 13.197360527894434), 'K3_NB_L0_C4': (3, 42.83437519020018), 'K3_NB_L0_C5': (3, 52.967536933235024), 'K3_NB_L0_C6': (3, 75.70378673679285), 'K3_NB_L0_C7': (10, 137.06330893763467), 'K3_NB_L0_C8': (5, 111.35105463874864), 'K3_NB_L0_C9': (8, 137.16754591852924), 'K3_NB_L1_C0': (1, 13.193964790027767), 'K3_NB_L1_C1': (0, 0.0), 'K3_NB_L1_C10': (4, 98.18177468477191), 'K3_NB_L1_C11': (5, 111.28213195202095), 'K3_NB_L1_C12': (11, 162.95623627778474), 'K3_NB_L1_C13': (9, 131.22438943575094), 'K3_NB_L1_C14': (9, 125.76214613019312), 'K3_NB_L1_C15': (7, 126.89941693605068), 'K3_NB_L1_C16': (6, 110.77276645039515), 'K3_NB_L1_C17': (7, 117.94401178387055), 'K3_NB_L1_C2': (1, 29.994001199760124), 'K3_NB_L1_C3': (0, 0.0), 'K3_NB_L1_C4': (1, 13.197360527894409), 'K3_NB_L1_C5': (6, 95.74101682339409), 'K3_NB_L1_C6': (11, 140.46038344415118), 'K3_NB_L1_C7': (7, 110.1658126533164), 'K3_NB_L1_C8': (5, 97.5743082057095), 'K3_NB_L1_C9': (5, 97.57559422068479), 'K3_NB_L2_C0': (1, 0.0), 'K3_NB_L2_C1': (0, 0.0), 'K3_NB_L2_C10': (9, 136.56193311939714), 'K3_NB_L2_C11': (4, 98.18177241773847), 'K3_NB_L2_C12': (6, 80.05088080833664), 'K3_NB_L2_C13': (5, 97.57535409581742), 'K3_NB_L2_C14': (7, 114.7058957250977), 'K3_NB_L2_C15': (10, 133.95118374422358), 'K3_NB_L2_C16': (10, 133.95213881797852), 'K3_NB_L2_C17': (8, 123.54534334495457), 'K3_NB_L2_C2': (1, 13.197360527894409), 'K3_NB_L2_C3': (0, 0.0), 'K3_NB_L2_C4': (1, 29.994001199760017), 'K3_NB_L2_C5': (4, 78.72052818057242), 'K3_NB_L2_C6': (6, 110.44356523092573), 'K3_NB_L2_C7': (4, 98.17991720722678), 'K3_NB_L2_C8': (7, 122.80034174695757), 'K3_NB_L2_C9': (9, 122.19513503995294), 'TDrive_L0_C0': (0, 0.0), 'TDrive_L0_C1': (0, 0.0), 'TDrive_L0_C10': (0, 0.0), 'TDrive_L0_C11': (0, 0.0), 'TDrive_L0_C12': (0, 0.0), 'TDrive_L0_C2': (0, 0.0), 'TDrive_L0_C3': (0, 0.0), 'TDrive_L0_C4': (0, 0.0), 'TDrive_L0_C5': (0, 0.0), 'TDrive_L0_C6': (0, 0.0), 'TDrive_L0_C7': (0, 0.0), 'TDrive_L0_C8': (0, 0.0), 'TDrive_L0_C9': (0, 0.0), 'TDrive_lower_L0_C0': (0, 0.0), 'TDrive_lower_L0_C1': (0, 0.0), 'TDrive_lower_L0_C2': (0, 0.0), 'TDrive_lower_L0_C3': (1, 15.838732901367884), 'TDrive_upper_L0_C0': (0, 0.0), 'TDrive_upper_L0_C1': (0, 0.0), 'URd_lower_out_L0_C0': (0, 0.0), 'URd_lower_out_L0_C1': (0, 0.0), 'URd_lower_out_L0_C10': (4, 83.51331893448516), 'URd_lower_out_L0_C2': (0, 0.0), 'URd_lower_out_L0_C3': (1, 35.997120230381604), 'URd_lower_out_L0_C4': (0, 0.0), 'URd_lower_out_L0_C5': (0, 0.0), 'URd_lower_out_L0_C6': (0, 0.0), 'URd_lower_out_L0_C7': (0, 0.0), 'URd_lower_out_L0_C8': (0, 0.0), 'URd_lower_out_L0_C9': (0, 0.0), 'URd_upper_out_L0_C0': (1, 15.838732901367875), 'URd_upper_out_L0_C1': (0, 0.0), 'URd_upper_out_L0_C10': (1, 2.9751045130192457), 'URd_upper_out_L0_C11': (1, 11.135766617290273), 'URd_upper_out_L0_C12': (0, 0.0), 'URd_upper_out_L0_C13': (0, 0.0), 'URd_upper_out_L0_C14': (1, 35.997120230381604), 'URd_upper_out_L0_C15': (5, 101.8048722665807), 'URd_upper_out_L0_C16': (6, 112.86980196805705), 'URd_upper_out_L0_C17': (6, 112.92903994859962), 'URd_upper_out_L0_C18': (5, 108.32141180668347), 'URd_upper_out_L0_C2': (0, 0.0), 'URd_upper_out_L0_C3': (0, 0.0), 'URd_upper_out_L0_C4': (0, 0.0), 'URd_upper_out_L0_C5': (0, 0.0), 'URd_upper_out_L0_C6': (0, 0.0), 'URd_upper_out_L0_C7': (0, 0.0), 'URd_upper_out_L0_C8': (0, 0.0), 'URd_upper_out_L0_C9': (0, 0.0)}
    current_phase = curr_phase
    traci_cell_dict = the_dict

    for cell_group in network:
        for cell in cell_group.arr:
            index = cell_group.arr.index(cell)
            listed_tuple = list(cell)
            listed_tuple[1] = traci_cell_dict[listed_tuple[0]][0]
            listed_tuple[2] = round(traci_cell_dict[listed_tuple[0]][1], 2)
            cell_group.arr[index] = tuple(listed_tuple)
        array.append(cell_group.arr)
    # return current_phase, array
    return traci_cell_dict


# phase, get_array = read_input()
# print(phase)
# print(get_array)


def evaluate_delay(cell):
    traci_cell_dict = read_input()
    delay_time = 0
    for cells in cell.cells:
        if traci_cell_dict[cells][1] > 95:
            delay_time += 1
    cell.delay = delay_time


# !/usr/bin/env python

import os
import sys
import optparse

# we need to import some python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # Checks for the binary in environ vars
import traci


def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                          default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options


def getLaneParams():
    cells = traci.lanearea.getIDList()
    cell_dict = dict()
    for cell in cells:
        # print(cell)
        cell_vehicles = traci.lanearea.getLastStepVehicleNumber(cell)
        # print(cell_vehicles)
        occupancy = traci.lanearea.getLastStepOccupancy(cell)
        # print(occupancy)
        # if cell_vehicles != 0:
        cell_dict[cell] = (cell_vehicles, occupancy)
        # cell_list.append((cell, (cell_vehicles, occupancy)))

    if len(cell_dict) > 0:
        # print(cell_dict)
        return cell_dict


# TraCI control loop
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()  # move one second in simulation
        if (step % 5 == 0):
            print("time step:" + str(step))
            # print(str(traci.trafficlight.getPhase("kuf")) + " : " + str(traci.trafficlight.getPhaseDuration("kuf")))
            #if (traci.trafficlight.getPhase("kuf") in [0, 3, 6, 9]):
            kuf_phase = traci.trafficlight.getPhase("kuf")
            kuf_phase_name = traci.trafficlight.getPhaseName("kuf")

            time_remaining = traci.trafficlight.getNextSwitch("kuf")

            print("NextSwitch:" + str(time_remaining))
            #if (kuf_phase != old_kuf_phase):
            global curr_phase
            global the_dict
            curr_phase = kuf_phase_name.split(" - ")
            the_dict = getLaneParams()
            print("---------------------------------------------------")
            print("The current phase with light color:" + str(kuf_phase_name))
            print("The current phase only:" + str(curr_phase[0]))
            print("dict w/ lane name, veh count and occupancy:")
            print(str(the_dict))
            print("---------------------------------------------------")

            phase1delay = 0
            phase2delay = 0
            phase3delay = 0
            phase4delay = 0

            for phases in Phase_1:
                evaluate_delay(phases)
                phase1delay += phases.delay

            for phases in Phase_2:
                evaluate_delay(phases)
                phase2delay += phases.delay

            for phases in Phase_3:
                evaluate_delay(phases)
                phase3delay += phases.delay

            for phases in Phase_4:
                evaluate_delay(phases)
                phase4delay += phases.delay

            print("phase 1=" + str(phase1delay) +" phase 2=" + str(phase2delay) +" phase 3=" + str(phase3delay) +" phase 4=" + str(phase4delay) )
            print("===================================================")
            #print(phase1delay, phase2delay, phase3delay, phase4delay)
            # this tracks green changes in KUF
        step += 1


    # traci.close()
    # sys.stdout.flush()


if __name__ == "__main__":
    options = get_options()

    # check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # traci starts sumo as a subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "osm.sumocfg",
                 "--tripinfo-output", "tripinfo.xml"])
    # getLaneParams()

    run()
