import math

class Cell:
    def __init__(self, lane, length, max_speed, car_num, busy, tick):
        self.lane = lane
        self.busy = busy
        self.car_num = car_num
        self.arr = []
        name = lane.split("-")
        shortname_dictionary = {
            " Lane 0" : "L0_",
            " Lane 1" : "L1_",
            " Lane 2" : "L2_",
            " Lane 3" : "L3_",
            " Lane 4" : "L4_",
            "Upper Katipunan SB ": "K1_SB_",
            "Middle Katipunan SB ": "K2_SB_",
            "B. Gonzales Road ": "Bgon_",
            "F. dela Rosa Road ": "FdRosa_",
            "Middle Katipunan NB upper ": "K2_NB_R4_",
            "Middle Katipunan NB lower ": "K2_NB_R5R6_",
            "Lower Katipunan NB ": "K3_NB_",
            "Thornton Drive ":"TDrive_",
            " Lower":"lower_L0_",
            " Upper":"upper_L0_",
            " extension": "L0_",
            "University Road upper ": "URd_upper_",
            "University Road lower ": "URd_lower_",
            " Exit":"out_L0_"
        }
        road_lane_name = shortname_dictionary[name[0]] + shortname_dictionary[name[1]]

        for n in range (math.floor(length/(max_speed/tick))):
            self.arr.append((road_lane_name + "C" + str(n), 0))
        self.arr_len = len(self.arr)
        
        #print(str(lane) +" "+str(self.arr_len))
        

#done, change length to 400
K1_SB_0 = Cell("Upper Katipunan SB - Lane 0", 400, 16.67, 0, 0, 1)
K1_SB_1 = Cell("Upper Katipunan SB - Lane 1", 400, 16.67, 0, 0, 1)
K1_SB_2 = Cell("Upper Katipunan SB - Lane 2", 400, 16.67, 0, 0, 1)
K1_SB_3 = Cell("Upper Katipunan SB - Lane 3", 400, 16.67, 0, 0, 1)
K1_SB_4 = Cell("Upper Katipunan SB - Lane 4", 400, 16.67, 0, 0, 1)

# K1 NB doesn't need cells
# K1_NB_0 = Cell("Upper Katipunan NB - Lane 0", 399.88, 16.67, 0, 0, 1)
# K1_NB_1 = Cell("Upper Katipunan NB - Lane 1", 399.88, 16.67, 0, 0, 1)
# K1_NB_2 = Cell("Upper Katipunan NB - Lane 2", 399.88, 16.67, 0, 0, 1)
# K1_NB_3 = Cell("Upper Katipunan NB - Lane 3", 399.88, 16.67, 0, 0, 1)

#done, changed length from 294.8 to 291
BGon_0 = Cell("B. Gonzales Road - Lane 0", 291, 8.33, 0, 0, 1)
BGon_1 = Cell("B. Gonzales Road - Lane 1", 291, 8.33, 0, 0, 1)

#done, lower changed from 48.8 to 56 
TDrive_lower = Cell("Thornton Drive - Lower", 56, 13.89, 0, 0, 1)
TDrive_upper = Cell("Thornton Drive - Upper", 36.72, 13.89, 0, 0, 1)
TDrive_extension = Cell("Thornton Drive - extension", 188.45, 13.89, 0, 0, 1)

#done
K2_SB_0 = Cell("Middle Katipunan SB - Lane 0", 178.37, 16.67, 0, 0, 1)
K2_SB_1 = Cell("Middle Katipunan SB - Lane 1", 178.37, 16.67, 0, 0, 1)
K2_SB_2 = Cell("Middle Katipunan SB - Lane 2", 178.37, 16.67, 0, 0, 1)
K2_SB_3 = Cell("Middle Katipunan SB - Lane 3", 178.37, 16.67, 0, 0, 1)
K2_SB_4 = Cell("Middle Katipunan SB - Lane 4", 178.37, 16.67, 0, 0, 1)

#done
K2_NB_R4_0 = Cell("Middle Katipunan NB upper - Lane 0", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_1 = Cell("Middle Katipunan NB upper - Lane 1", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_2 = Cell("Middle Katipunan NB upper - Lane 2", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_3 = Cell("Middle Katipunan NB upper - Lane 3", 33.4, 16.67, 0, 0, 1)

#done
K2_NB_R5R6_0 = Cell("Middle Katipunan NB lower - Lane 0", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_1 = Cell("Middle Katipunan NB lower - Lane 1", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_2 = Cell("Middle Katipunan NB lower - Lane 2", 137.78, 16.67, 0, 0, 1)

#done changed length from 243.12 to 233.12
FdRosa_0 = Cell("F. dela Rosa Road - Lane 0", 233.12, 8.33, 0, 0, 1)
FdRosa_1 = Cell("F. dela Rosa Road - Lane 1", 233.12, 8.33, 0, 0, 1)

#done, updated URoad length aligned to sumo
URd_upper_out = Cell("University Road upper - Exit", 277, 13.89, 0, 0, 1)
#URd_upper_in = Cell("University Road upper - Entrance", 135.42, 13.89, 0, 0, 1)
URd_lower_out = Cell("University Road lower - Exit", 156.24, 13.89, 0, 0, 1)
#URd_lower_in = Cell("University Road lower - Entrance", 134.83, 13.89, 0, 0, 1)

# K3 SB doesn't need cells
# K3_SB_0 = Cell("Lower Katipunan SB - Lane 0", 309.21, 16.67, 0, 0, 1)
# K3_SB_1 = Cell("Lower Katipunan SB - Lane 1", 309.21, 16.67, 0, 0, 1)
# K3_SB_2 = Cell("Lower Katipunan SB - Lane 2", 309.21, 16.67, 0, 0, 1)
# K3_SB_3 = Cell("Lower Katipunan SB - Lane 3", 309.21, 16.67, 0, 0, 1)
# K3_SB_4 = Cell("Lower Katipunan SB - Lane 4", 309.21, 16.67, 0, 0, 1)

#done
K3_NB_0 = Cell("Lower Katipunan NB - Lane 0", 309.12, 16.67, 0, 0, 1)
K3_NB_1 = Cell("Lower Katipunan NB - Lane 1", 309.12, 16.67, 0, 0, 1)
K3_NB_2 = Cell("Lower Katipunan NB - Lane 2", 309.12, 16.67, 0, 0, 1)

network = [K1_SB_0, K1_SB_1, K1_SB_2, K1_SB_3, K1_SB_4, BGon_0, BGon_1, TDrive_lower, TDrive_upper, TDrive_extension, K2_SB_0, K2_SB_1, K2_SB_2, K2_SB_3, K2_SB_4, 
           K2_NB_R4_0, K2_NB_R4_1, K2_NB_R4_2, K2_NB_R4_3, K2_NB_R5R6_0, K2_NB_R5R6_1, K2_NB_R5R6_2, FdRosa_0, FdRosa_1, URd_upper_out, URd_lower_out, K3_NB_0, K3_NB_1, K3_NB_2]


class Vehicle:
    def __init__(self, type, length, distance):
        self.type = type
        self.length = length
        self.offset = distance
        
motor = Vehicle("Motorcycle", 2.3, 0.2)
car = Vehicle("Car", 4.8, 0.4)
        
def read_input():
    traci_cell_dict = {'Bgon_L0_C0': 0, 'Bgon_L0_C1': 0, 'Bgon_L0_C10': 0, 'Bgon_L0_C11': 0, 'Bgon_L0_C12': 0, 'Bgon_L0_C13': 0, 'Bgon_L0_C14': 0, 'Bgon_L0_C15': 0, 'Bgon_L0_C16': 0, 'Bgon_L0_C17': 0, 'Bgon_L0_C18': 0, 'Bgon_L0_C19': 0, 'Bgon_L0_C2': 0, 'Bgon_L0_C20': 0, 'Bgon_L0_C21': 0, 'Bgon_L0_C22': 0, 'Bgon_L0_C23': 0, 'Bgon_L0_C24': 0, 'Bgon_L0_C25': 0, 'Bgon_L0_C26': 0, 'Bgon_L0_C27': 0, 'Bgon_L0_C28': 0, 'Bgon_L0_C29': 0, 'Bgon_L0_C3': 0, 'Bgon_L0_C30': 0, 'Bgon_L0_C31': 0, 'Bgon_L0_C32': 0, 'Bgon_L0_C33': 0, 'Bgon_L0_C4': 0, 'Bgon_L0_C5': 1, 'Bgon_L0_C6': 0, 'Bgon_L0_C7': 1, 'Bgon_L0_C8': 0, 'Bgon_L0_C9': 0, 'Bgon_L1_C0': 0, 'Bgon_L1_C1': 0, 'Bgon_L1_C10': 0, 'Bgon_L1_C11': 0, 'Bgon_L1_C12': 1, 'Bgon_L1_C13': 0, 'Bgon_L1_C14': 0, 'Bgon_L1_C15': 0, 'Bgon_L1_C16': 0, 'Bgon_L1_C17': 0, 'Bgon_L1_C18': 0, 'Bgon_L1_C19': 1, 'Bgon_L1_C2': 0, 'Bgon_L1_C20': 1, 'Bgon_L1_C21': 0, 'Bgon_L1_C22': 0, 'Bgon_L1_C23': 0, 'Bgon_L1_C24': 0, 'Bgon_L1_C25': 2, 'Bgon_L1_C26': 3, 'Bgon_L1_C27': 4, 'Bgon_L1_C28': 3, 'Bgon_L1_C29': 4, 'Bgon_L1_C3': 0, 'Bgon_L1_C30': 3, 'Bgon_L1_C31': 4, 'Bgon_L1_C32': 3, 'Bgon_L1_C33': 4, 'Bgon_L1_C4': 0, 'Bgon_L1_C5': 0, 'Bgon_L1_C6': 0, 'Bgon_L1_C7': 0, 'Bgon_L1_C8': 0, 'Bgon_L1_C9': 0, 'FdRosa_L0_C0': 0, 'FdRosa_L0_C1': 0, 'FdRosa_L0_C10': 0, 'FdRosa_L0_C11': 0, 'FdRosa_L0_C12': 0, 'FdRosa_L0_C13': 0, 'FdRosa_L0_C14': 0, 'FdRosa_L0_C15': 1, 'FdRosa_L0_C16': 0, 'FdRosa_L0_C17': 1, 'FdRosa_L0_C18': 0, 'FdRosa_L0_C19': 0, 'FdRosa_L0_C2': 0, 'FdRosa_L0_C20': 0, 'FdRosa_L0_C21': 0, 'FdRosa_L0_C22': 0, 'FdRosa_L0_C23': 0, 'FdRosa_L0_C24': 0, 'FdRosa_L0_C25': 2, 'FdRosa_L0_C26': 4, 'FdRosa_L0_C3': 0, 'FdRosa_L0_C4': 0, 'FdRosa_L0_C5': 0, 'FdRosa_L0_C6': 0, 'FdRosa_L0_C7': 0, 'FdRosa_L0_C8': 0, 'FdRosa_L0_C9': 1, 'FdRosa_L1_C0': 0, 'FdRosa_L1_C1': 0, 'FdRosa_L1_C10': 0, 'FdRosa_L1_C11': 1, 'FdRosa_L1_C12': 1, 'FdRosa_L1_C13': 1, 'FdRosa_L1_C14': 0, 'FdRosa_L1_C15': 0, 'FdRosa_L1_C16': 0, 'FdRosa_L1_C17': 0, 'FdRosa_L1_C18': 0, 'FdRosa_L1_C19': 0, 'FdRosa_L1_C2': 1, 'FdRosa_L1_C20': 0, 'FdRosa_L1_C21': 0, 'FdRosa_L1_C22': 0, 'FdRosa_L1_C23': 0, 'FdRosa_L1_C24': 0, 'FdRosa_L1_C25': 1, 'FdRosa_L1_C26': 3, 'FdRosa_L1_C3': 0, 'FdRosa_L1_C4': 0, 'FdRosa_L1_C5': 0, 'FdRosa_L1_C6': 0, 'FdRosa_L1_C7': 0, 'FdRosa_L1_C8': 0, 'FdRosa_L1_C9': 0, 'K1_SB_L0_C0': 0, 'K1_SB_L0_C1': 1, 'K1_SB_L0_C10': 0, 'K1_SB_L0_C11': 0, 'K1_SB_L0_C12': 1, 'K1_SB_L0_C13': 0, 'K1_SB_L0_C14': 0, 'K1_SB_L0_C15': 3, 'K1_SB_L0_C16': 3, 'K1_SB_L0_C17': 5, 'K1_SB_L0_C18': 3, 'K1_SB_L0_C19': 2, 'K1_SB_L0_C2': 1, 'K1_SB_L0_C20': 3, 'K1_SB_L0_C21': 1, 'K1_SB_L0_C22': 3, 'K1_SB_L0_C3': 0, 'K1_SB_L0_C4': 0, 'K1_SB_L0_C5': 0, 'K1_SB_L0_C6': 0, 'K1_SB_L0_C7': 0, 'K1_SB_L0_C8': 1, 'K1_SB_L0_C9': 0, 'K1_SB_L1_C0': 1, 'K1_SB_L1_C1': 0, 'K1_SB_L1_C10': 0, 'K1_SB_L1_C11': 1, 'K1_SB_L1_C12': 0, 'K1_SB_L1_C13': 0, 'K1_SB_L1_C14': 1, 'K1_SB_L1_C15': 0, 'K1_SB_L1_C16': 3, 'K1_SB_L1_C17': 5, 'K1_SB_L1_C18': 4, 'K1_SB_L1_C19': 3, 'K1_SB_L1_C2': 0, 'K1_SB_L1_C20': 1, 'K1_SB_L1_C21': 2, 'K1_SB_L1_C22': 2, 'K1_SB_L1_C3': 1, 'K1_SB_L1_C4': 0, 'K1_SB_L1_C5': 0, 'K1_SB_L1_C6': 0, 'K1_SB_L1_C7': 0, 'K1_SB_L1_C8': 0, 'K1_SB_L1_C9': 0, 'K1_SB_L2_C0': 0, 'K1_SB_L2_C1': 1, 'K1_SB_L2_C10': 0, 'K1_SB_L2_C11': 1, 'K1_SB_L2_C12': 1, 'K1_SB_L2_C13': 0, 'K1_SB_L2_C14': 1, 'K1_SB_L2_C15': 3, 'K1_SB_L2_C16': 4, 'K1_SB_L2_C17': 10, 'K1_SB_L2_C18': 4, 'K1_SB_L2_C19': 3, 'K1_SB_L2_C2': 0, 'K1_SB_L2_C20': 2, 'K1_SB_L2_C21': 2, 'K1_SB_L2_C22': 2, 'K1_SB_L2_C3': 0, 'K1_SB_L2_C4': 1, 'K1_SB_L2_C5': 0, 'K1_SB_L2_C6': 0, 'K1_SB_L2_C7': 0, 'K1_SB_L2_C8': 0, 'K1_SB_L2_C9': 1, 'K1_SB_L3_C0': 0, 'K1_SB_L3_C1': 0, 'K1_SB_L3_C10': 0, 'K1_SB_L3_C11': 0, 'K1_SB_L3_C12': 0, 'K1_SB_L3_C13': 1, 'K1_SB_L3_C14': 0, 'K1_SB_L3_C15': 2, 'K1_SB_L3_C16': 9, 'K1_SB_L3_C17': 6, 'K1_SB_L3_C18': 7, 'K1_SB_L3_C19': 2, 'K1_SB_L3_C2': 1, 'K1_SB_L3_C20': 4, 'K1_SB_L3_C21': 1, 'K1_SB_L3_C22': 1, 'K1_SB_L3_C3': 0, 'K1_SB_L3_C4': 1, 'K1_SB_L3_C5': 1, 'K1_SB_L3_C6': 0, 'K1_SB_L3_C7': 1, 'K1_SB_L3_C8': 1, 'K1_SB_L3_C9': 1, 'K1_SB_L4_C0': 1, 'K1_SB_L4_C1': 0, 'K1_SB_L4_C10': 0, 'K1_SB_L4_C11': 0, 'K1_SB_L4_C12': 0, 'K1_SB_L4_C13': 1, 'K1_SB_L4_C14': 1, 'K1_SB_L4_C15': 0, 'K1_SB_L4_C16': 3, 'K1_SB_L4_C17': 4, 'K1_SB_L4_C18': 2, 'K1_SB_L4_C19': 3, 'K1_SB_L4_C2': 0, 'K1_SB_L4_C20': 2, 'K1_SB_L4_C21': 4, 'K1_SB_L4_C22': 3, 'K1_SB_L4_C3': 0, 'K1_SB_L4_C4': 0, 'K1_SB_L4_C5': 0, 'K1_SB_L4_C6': 1, 'K1_SB_L4_C7': 0, 'K1_SB_L4_C8': 0, 'K1_SB_L4_C9': 0, 'K2_NB_R4_L0_C0': 4, 'K2_NB_R4_L0_C1': 6, 'K2_NB_R4_L1_C0': 1, 'K2_NB_R4_L1_C1': 4, 'K2_NB_R4_L2_C0': 2, 'K2_NB_R4_L2_C1': 8, 'K2_NB_R4_L3_C0': 1, 'K2_NB_R4_L3_C1': 5, 'K2_NB_R5R6_L0_C0': 0, 'K2_NB_R5R6_L0_C1': 0, 'K2_NB_R5R6_L0_C2': 0, 'K2_NB_R5R6_L0_C3': 0, 'K2_NB_R5R6_L0_C4': 0, 'K2_NB_R5R6_L0_C5': 0, 'K2_NB_R5R6_L0_C6': 0, 'K2_NB_R5R6_L0_C7': 0, 'K2_NB_R5R6_L1_C0': 0, 'K2_NB_R5R6_L1_C1': 0, 'K2_NB_R5R6_L1_C2': 0, 'K2_NB_R5R6_L1_C3': 0, 'K2_NB_R5R6_L1_C4': 0, 'K2_NB_R5R6_L1_C5': 0, 'K2_NB_R5R6_L1_C6': 0, 'K2_NB_R5R6_L1_C7': 0, 'K2_NB_R5R6_L2_C0': 0, 'K2_NB_R5R6_L2_C1': 0, 'K2_NB_R5R6_L2_C2': 0, 'K2_NB_R5R6_L2_C3': 0, 'K2_NB_R5R6_L2_C4': 0, 'K2_NB_R5R6_L2_C5': 0, 'K2_NB_R5R6_L2_C6': 0, 'K2_NB_R5R6_L2_C7': 0, 'K2_SB_L0_C0': 0, 'K2_SB_L0_C1': 0, 'K2_SB_L0_C2': 2, 'K2_SB_L0_C3': 1, 'K2_SB_L0_C4': 1, 'K2_SB_L0_C5': 1, 'K2_SB_L0_C6': 0, 'K2_SB_L0_C7': 0, 'K2_SB_L0_C8': 0, 'K2_SB_L0_C9': 2, 'K2_SB_L1_C0': 1, 'K2_SB_L1_C1': 1, 'K2_SB_L1_C2': 1, 'K2_SB_L1_C3': 1, 'K2_SB_L1_C4': 2, 'K2_SB_L1_C5': 1, 'K2_SB_L1_C6': 0, 'K2_SB_L1_C7': 2, 'K2_SB_L1_C8': 1, 'K2_SB_L1_C9': 2, 'K2_SB_L2_C0': 5, 'K2_SB_L2_C1': 2, 'K2_SB_L2_C2': 1, 'K2_SB_L2_C3': 1, 'K2_SB_L2_C4': 1, 'K2_SB_L2_C5': 1, 'K2_SB_L2_C6': 2, 'K2_SB_L2_C7': 2, 'K2_SB_L2_C8': 2, 'K2_SB_L2_C9': 2, 'K2_SB_L3_C0': 1, 'K2_SB_L3_C1': 1, 'K2_SB_L3_C2': 1, 'K2_SB_L3_C3': 0, 'K2_SB_L3_C4': 0, 'K2_SB_L3_C5': 0, 'K2_SB_L3_C6': 0, 'K2_SB_L3_C7': 0, 'K2_SB_L3_C8': 0, 'K2_SB_L3_C9': 1, 'K2_SB_L4_C0': 0, 'K2_SB_L4_C1': 0, 'K2_SB_L4_C2': 0, 'K2_SB_L4_C3': 0, 'K2_SB_L4_C4': 0, 'K2_SB_L4_C5': 0, 'K2_SB_L4_C6': 0, 'K2_SB_L4_C7': 0, 'K2_SB_L4_C8': 0, 'K2_SB_L4_C9': 0, 'K3_NB_L0_C0': 0, 'K3_NB_L0_C1': 1, 'K3_NB_L0_C10': 5, 'K3_NB_L0_C11': 13, 'K3_NB_L0_C12': 6, 'K3_NB_L0_C13': 5, 'K3_NB_L0_C14': 5, 'K3_NB_L0_C15': 4, 'K3_NB_L0_C16': 6, 'K3_NB_L0_C17': 5, 'K3_NB_L0_C2': 0, 'K3_NB_L0_C3': 1, 'K3_NB_L0_C4': 0, 'K3_NB_L0_C5': 1, 'K3_NB_L0_C6': 0, 'K3_NB_L0_C7': 0, 'K3_NB_L0_C8': 1, 'K3_NB_L0_C9': 6, 'K3_NB_L1_C0': 1, 'K3_NB_L1_C1': 1, 'K3_NB_L1_C10': 6, 'K3_NB_L1_C11': 4, 'K3_NB_L1_C12': 5, 'K3_NB_L1_C13': 12, 'K3_NB_L1_C14': 9, 'K3_NB_L1_C15': 10, 'K3_NB_L1_C16': 5, 'K3_NB_L1_C17': 10, 'K3_NB_L1_C2': 0, 'K3_NB_L1_C3': 0, 'K3_NB_L1_C4': 1, 'K3_NB_L1_C5': 0, 'K3_NB_L1_C6': 0, 'K3_NB_L1_C7': 1, 'K3_NB_L1_C8': 4, 'K3_NB_L1_C9': 4, 'K3_NB_L2_C0': 1, 'K3_NB_L2_C1': 0, 'K3_NB_L2_C10': 5, 'K3_NB_L2_C11': 4, 'K3_NB_L2_C12': 8, 'K3_NB_L2_C13': 9, 'K3_NB_L2_C14': 6, 'K3_NB_L2_C15': 6, 'K3_NB_L2_C16': 12, 'K3_NB_L2_C17': 4, 'K3_NB_L2_C2': 1, 'K3_NB_L2_C3': 0, 'K3_NB_L2_C4': 1, 'K3_NB_L2_C5': 1, 'K3_NB_L2_C6': 1, 'K3_NB_L2_C7': 0, 'K3_NB_L2_C8': 1, 'K3_NB_L2_C9': 7, 'TDrive_L0_C0': 0, 'TDrive_L0_C1': 0, 'TDrive_L0_C10': 0, 'TDrive_L0_C11': 0, 'TDrive_L0_C12': 0, 'TDrive_L0_C2': 0, 'TDrive_L0_C3': 0, 'TDrive_L0_C4': 0, 'TDrive_L0_C5': 0, 'TDrive_L0_C6': 0, 'TDrive_L0_C7': 0, 'TDrive_L0_C8': 0, 'TDrive_L0_C9': 0, 'TDrive_lower_L0_C0': 0, 'TDrive_lower_L0_C1': 0, 'TDrive_lower_L0_C2': 0, 'TDrive_lower_L0_C3': 2, 'TDrive_upper_L0_C0': 0, 'TDrive_upper_L0_C1': 0, 'URd_lower_out_L0_C0': 0, 'URd_lower_out_L0_C1': 0, 'URd_lower_out_L0_C10': 4, 'URd_lower_out_L0_C2': 0, 'URd_lower_out_L0_C3': 0, 'URd_lower_out_L0_C4': 0, 'URd_lower_out_L0_C5': 1, 'URd_lower_out_L0_C6': 0, 'URd_lower_out_L0_C7': 0, 'URd_lower_out_L0_C8': 0, 'URd_lower_out_L0_C9': 1, 'URd_upper_out_L0_C0': 0, 'URd_upper_out_L0_C1': 0, 'URd_upper_out_L0_C10': 1, 'URd_upper_out_L0_C11': 0, 'URd_upper_out_L0_C12': 0, 'URd_upper_out_L0_C13': 0, 'URd_upper_out_L0_C14': 1, 'URd_upper_out_L0_C15': 0, 'URd_upper_out_L0_C16': 0, 'URd_upper_out_L0_C17': 5, 'URd_upper_out_L0_C18': 5, 'URd_upper_out_L0_C2': 0, 'URd_upper_out_L0_C3': 0, 'URd_upper_out_L0_C4': 0, 'URd_upper_out_L0_C5': 0, 'URd_upper_out_L0_C6': 0, 'URd_upper_out_L0_C7': 0, 'URd_upper_out_L0_C8': 0, 'URd_upper_out_L0_C9': 1}
    for cell_group in network:
        for cell in cell_group.arr:
            index = cell_group.arr.index(cell)
            listed_tuple = list(cell)
            listed_tuple[1] = traci_cell_dict[listed_tuple[0]]
            cell_group.arr[index] = tuple(listed_tuple)
        print(cell_group.arr)
            
            
    
    
    
# def main():
#     # testing
#     print(K1_SB_1.lane)
#     print(K1_SB_1.arr_len)
    
#     print(K1_NB_1.lane)
#     print(K1_NB_1.arr_len)
    
#     print(BGon_1.lane)
#     print(BGon_1.arr_len)
    
#     print(TDrive_lower.lane)
#     print(TDrive_lower.arr_len)
    
#     print(K2_SB_1.lane)
#     print(K2_SB_1.arr_len)
    
#     print(K2_NB_R4_1.lane)
#     print(K2_NB_R4_1.arr_len)
    
#     print(K2_NB_R5R6_1.lane)
#     print(K2_NB_R5R6_1.arr_len)
    
#     print(FdRosa_1.lane)
#     print(FdRosa_1.arr_len)
    
#     print(URd_lower_out.lane)
#     print(URd_lower_out.arr_len)
    
#     print(K3_NB_1.lane)
#     print(K3_NB_1.arr_len)
    
# main()

read_input()