import math

class Cell:
    def __init__(self, lane, length, max_speed, car_num, busy, tick):
        self.lane = lane
        self.busy = busy
        self.car_num = car_num
        self.arr = [0] * math.floor(length/(max_speed/tick))
        self.arr_len = len(self.arr)
        
K1_SB_1 = Cell("Upper Katipunan SB - Lane 1", 406.8, 16.67, 0, 0, 1)
K1_SB_2 = Cell("Upper Katipunan SB - Lane 2", 406.8, 16.67, 0, 0, 1)
K1_SB_3 = Cell("Upper Katipunan SB - Lane 3", 406.8, 16.67, 0, 0, 1)
K1_SB_4 = Cell("Upper Katipunan SB - Lane 4", 406.8, 16.67, 0, 0, 1)
K1_SB_5 = Cell("Upper Katipunan SB - Lane 5", 406.8, 16.67, 0, 0, 1)

K1_NB_1 = Cell("Upper Katipunan NB - Lane 1", 399.88, 16.67, 0, 0, 1)
K1_NB_2 = Cell("Upper Katipunan NB - Lane 2", 399.88, 16.67, 0, 0, 1)
K1_NB_3 = Cell("Upper Katipunan NB - Lane 3", 399.88, 16.67, 0, 0, 1)
K1_NB_4 = Cell("Upper Katipunan NB - Lane 4", 399.88, 16.67, 0, 0, 1)

BGon_1 = Cell("B. Gonzales Road - Lane 1", 260.23, 8.33, 0, 0, 1)
BGon_2 = Cell("B. Gonzales Road - Lane 2", 260.23, 8.33, 0, 0, 1)

TDrive_lower = Cell("Thornton Drive - Lower", 237.25, 13.89, 0, 0, 1)
TDrive_upper = Cell("Thornton Drive - Upper", 225.17, 13.89, 0, 0, 1)

K2_SB_1 = Cell("Middle Katipunan SB - Lane 1", 178.37, 16.67, 0, 0, 1)
K2_SB_2 = Cell("Middle Katipunan SB - Lane 2", 178.37, 16.67, 0, 0, 1)
K2_SB_3 = Cell("Middle Katipunan SB - Lane 3", 178.37, 16.67, 0, 0, 1)
K2_SB_4 = Cell("Middle Katipunan SB - Lane 4", 178.37, 16.67, 0, 0, 1)
K2_SB_5 = Cell("Middle Katipunan SB - Lane 5", 178.37, 16.67, 0, 0, 1)

K2_NB_R4_1 = Cell("Middle Katipunan NB upper - Lane 1", 33, 16.67, 0, 0, 1)
K2_NB_R4_2 = Cell("Middle Katipunan NB upper - Lane 2", 33, 16.67, 0, 0, 1)
K2_NB_R4_3 = Cell("Middle Katipunan NB upper - Lane 3", 33, 16.67, 0, 0, 1)
K2_NB_R4_4 = Cell("Middle Katipunan NB upper - Lane 4", 33, 16.67, 0, 0, 1)

K2_NB_R5R6_1 = Cell("Middle Katipunan NB lower - Lane 1", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_2 = Cell("Middle Katipunan NB lower - Lane 2", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_3 = Cell("Middle Katipunan NB lower - Lane 3", 137.78, 16.67, 0, 0, 1)

FdRosa_1 = Cell("F. dela Rosa Road - Lane 1", 242.21, 8.33, 0, 0, 1)
FdRosa_2 = Cell("F. dela Rosa Road - Lane 2", 242.21, 8.33, 0, 0, 1)

URd_upper_out = Cell("University Road upper - Exit", 147.65, 13.89, 0, 0, 1)
URd_upper_in = Cell("University Road upper - Entrance", 135.42, 13.89, 0, 0, 1)
URd_lower_out = Cell("University Road lower - Exit", 156.24, 13.89, 0, 0, 1)
URd_lower_in = Cell("University Road lower - Entrance", 134.83, 13.89, 0, 0, 1)

K3_SB_1 = Cell("Lower Katipunan SB - Lane 1", 309.21, 16.67, 0, 0, 1)
K3_SB_2 = Cell("Lower Katipunan SB - Lane 2", 309.21, 16.67, 0, 0, 1)
K3_SB_3 = Cell("Lower Katipunan SB - Lane 3", 309.21, 16.67, 0, 0, 1)
K3_SB_4 = Cell("Lower Katipunan SB - Lane 4", 309.21, 16.67, 0, 0, 1)
K3_SB_5 = Cell("Lower Katipunan SB - Lane 5", 309.21, 16.67, 0, 0, 1)
K3_NB_1 = Cell("Lower Katipunan NB - Lane 1", 309.12, 16.67, 0, 0, 1)
K3_NB_2 = Cell("Lower Katipunan NB - Lane 2", 309.12, 16.67, 0, 0, 1)
K3_NB_3 = Cell("Lower Katipunan NB - Lane 3", 309.12, 16.67, 0, 0, 1)

class Vehicle:
    def __init__(self, type, length, distance):
        self.type = type
        self.length = length
        self.offset = distance
        
motor = Vehicle("Motorcycle", 2.3, 0.2)
car = Vehicle("Car", 4.8, 0.4)
        
def read_input():
    tuples_list = [('Bgon_L0_C0', 0), ('Bgon_L0_C1', 0), ('Bgon_L0_C10', 0), ('Bgon_L0_C11', 0), ('Bgon_L0_C12', 0), ('Bgon_L0_C13', 0), ('Bgon_L0_C14', 0), ('Bgon_L0_C15', 0), ('Bgon_L0_C16', 0), ('Bgon_L0_C17', 0), ('Bgon_L0_C18', 0), ('Bgon_L0_C19', 0), ('Bgon_L0_C2', 0), ('Bgon_L0_C20', 0), ('Bgon_L0_C21', 0), ('Bgon_L0_C22', 0), ('Bgon_L0_C23', 0), ('Bgon_L0_C24', 0), ('Bgon_L0_C25', 0), ('Bgon_L0_C26', 0), ('Bgon_L0_C27', 0), ('Bgon_L0_C28', 0), ('Bgon_L0_C29', 0), ('Bgon_L0_C3', 0), ('Bgon_L0_C30', 0), ('Bgon_L0_C31', 0), ('Bgon_L0_C32', 0), ('Bgon_L0_C33', 0), ('Bgon_L0_C4', 0), ('Bgon_L0_C5', 0), ('Bgon_L0_C6', 0), ('Bgon_L0_C7', 0), ('Bgon_L0_C8', 0), ('Bgon_L0_C9', 0), ('Bgon_L1_C0', 0), ('Bgon_L1_C1', 0), ('Bgon_L1_C10', 0), ('Bgon_L1_C11', 0), ('Bgon_L1_C12', 0), ('Bgon_L1_C13', 0), ('Bgon_L1_C14', 0), ('Bgon_L1_C15', 0), ('Bgon_L1_C16', 0), ('Bgon_L1_C17', 0), ('Bgon_L1_C18', 0), ('Bgon_L1_C19', 0), ('Bgon_L1_C2', 0), ('Bgon_L1_C20', 0), ('Bgon_L1_C21', 0), ('Bgon_L1_C22', 0), ('Bgon_L1_C23', 0), ('Bgon_L1_C24', 0), ('Bgon_L1_C25', 0), ('Bgon_L1_C26', 0), ('Bgon_L1_C27', 0), ('Bgon_L1_C28', 0), ('Bgon_L1_C29', 0), ('Bgon_L1_C3', 0), ('Bgon_L1_C30', 0), ('Bgon_L1_C31', 0), ('Bgon_L1_C32', 0), ('Bgon_L1_C33', 0), ('Bgon_L1_C4', 0), ('Bgon_L1_C5', 0), ('Bgon_L1_C6', 0), ('Bgon_L1_C7', 0), ('Bgon_L1_C8', 0), ('Bgon_L1_C9', 0), ('FdRosa_L0_C0', 0), ('FdRosa_L0_C1', 0), ('FdRosa_L0_C10', 0), ('FdRosa_L0_C11', 0), ('FdRosa_L0_C12', 0), ('FdRosa_L0_C13', 0), ('FdRosa_L0_C14', 0), ('FdRosa_L0_C15', 0), ('FdRosa_L0_C16', 0), ('FdRosa_L0_C17', 0), ('FdRosa_L0_C18', 0), ('FdRosa_L0_C19', 0), ('FdRosa_L0_C2', 0), ('FdRosa_L0_C20', 0), ('FdRosa_L0_C21', 0), ('FdRosa_L0_C22', 0), ('FdRosa_L0_C23', 0), ('FdRosa_L0_C24', 0), ('FdRosa_L0_C25', 0), ('FdRosa_L0_C26', 0), ('FdRosa_L0_C3', 0), ('FdRosa_L0_C4', 0), ('FdRosa_L0_C5', 0), ('FdRosa_L0_C6', 0), ('FdRosa_L0_C7', 0), ('FdRosa_L0_C8', 0), ('FdRosa_L0_C9', 0), ('FdRosa_L1_C0', 0), ('FdRosa_L1_C1', 0), ('FdRosa_L1_C10', 0), ('FdRosa_L1_C11', 0), ('FdRosa_L1_C12', 0), ('FdRosa_L1_C13', 0), ('FdRosa_L1_C14', 0), ('FdRosa_L1_C15', 0), ('FdRosa_L1_C16', 0), ('FdRosa_L1_C17', 0), ('FdRosa_L1_C18', 0), ('FdRosa_L1_C19', 0), ('FdRosa_L1_C2', 0), ('FdRosa_L1_C20', 0), ('FdRosa_L1_C21', 0), ('FdRosa_L1_C22', 0), ('FdRosa_L1_C23', 0), ('FdRosa_L1_C24', 0), ('FdRosa_L1_C25', 0), ('FdRosa_L1_C26', 0), ('FdRosa_L1_C3', 0), ('FdRosa_L1_C4', 0), ('FdRosa_L1_C5', 0), ('FdRosa_L1_C6', 0), ('FdRosa_L1_C7', 0), ('FdRosa_L1_C8', 0), ('FdRosa_L1_C9', 0), ('K1_SB_L0_C0', 0), ('K1_SB_L0_C1', 0), ('K1_SB_L0_C10', 0), ('K1_SB_L0_C11', 0), ('K1_SB_L0_C12', 0), ('K1_SB_L0_C13', 0), ('K1_SB_L0_C14', 0), ('K1_SB_L0_C15', 0), ('K1_SB_L0_C16', 0), ('K1_SB_L0_C17', 0), ('K1_SB_L0_C18', 0), ('K1_SB_L0_C19', 0), ('K1_SB_L0_C2', 0), ('K1_SB_L0_C20', 0), ('K1_SB_L0_C21', 0), ('K1_SB_L0_C22', 0), ('K1_SB_L0_C3', 0), ('K1_SB_L0_C4', 0), ('K1_SB_L0_C5', 0), ('K1_SB_L0_C6', 0), ('K1_SB_L0_C7', 0), ('K1_SB_L0_C8', 0), ('K1_SB_L0_C9', 0), ('K1_SB_L1_C0', 0), ('K1_SB_L1_C1', 0), ('K1_SB_L1_C10', 0), ('K1_SB_L1_C11', 0), ('K1_SB_L1_C12', 0), ('K1_SB_L1_C13', 0), ('K1_SB_L1_C14', 0), ('K1_SB_L1_C15', 0), ('K1_SB_L1_C16', 0), ('K1_SB_L1_C17', 0), ('K1_SB_L1_C18', 0), ('K1_SB_L1_C19', 0), ('K1_SB_L1_C2', 0), ('K1_SB_L1_C20', 0), ('K1_SB_L1_C21', 0), ('K1_SB_L1_C22', 0), ('K1_SB_L1_C3', 0), ('K1_SB_L1_C4', 0), ('K1_SB_L1_C5', 0), ('K1_SB_L1_C6', 0), ('K1_SB_L1_C7', 0), ('K1_SB_L1_C8', 0), ('K1_SB_L1_C9', 0), ('K1_SB_L2_C0', 0), ('K1_SB_L2_C1', 0), ('K1_SB_L2_C10', 0), ('K1_SB_L2_C11', 0), ('K1_SB_L2_C12', 0), ('K1_SB_L2_C13', 0), ('K1_SB_L2_C14', 0), ('K1_SB_L2_C15', 0), ('K1_SB_L2_C16', 0), ('K1_SB_L2_C17', 0), ('K1_SB_L2_C18', 0), ('K1_SB_L2_C19', 0), ('K1_SB_L2_C2', 0), ('K1_SB_L2_C20', 0), ('K1_SB_L2_C21', 0), ('K1_SB_L2_C22', 0), ('K1_SB_L2_C3', 0), ('K1_SB_L2_C4', 0), ('K1_SB_L2_C5', 0), ('K1_SB_L2_C6', 0), ('K1_SB_L2_C7', 0), ('K1_SB_L2_C8', 0), ('K1_SB_L2_C9', 0), ('K1_SB_L3_C0', 0), ('K1_SB_L3_C1', 0), ('K1_SB_L3_C10', 0), ('K1_SB_L3_C11', 0), ('K1_SB_L3_C12', 0), ('K1_SB_L3_C13', 0), ('K1_SB_L3_C14', 0), ('K1_SB_L3_C15', 0), ('K1_SB_L3_C16', 0), ('K1_SB_L3_C17', 0), ('K1_SB_L3_C18', 0), ('K1_SB_L3_C19', 0), ('K1_SB_L3_C2', 0), ('K1_SB_L3_C20', 0), ('K1_SB_L3_C21', 0), ('K1_SB_L3_C22', 0), ('K1_SB_L3_C3', 0), ('K1_SB_L3_C4', 0), ('K1_SB_L3_C5', 0), ('K1_SB_L3_C6', 0), ('K1_SB_L3_C7', 0), ('K1_SB_L3_C8', 0), ('K1_SB_L3_C9', 0), ('K1_SB_L4_C0', 0), ('K1_SB_L4_C1', 0), ('K1_SB_L4_C10', 0), ('K1_SB_L4_C11', 0), ('K1_SB_L4_C12', 0), ('K1_SB_L4_C13', 0), ('K1_SB_L4_C14', 0), ('K1_SB_L4_C15', 0), ('K1_SB_L4_C16', 0), ('K1_SB_L4_C17', 0), ('K1_SB_L4_C18', 0), ('K1_SB_L4_C19', 0), ('K1_SB_L4_C2', 0), ('K1_SB_L4_C20', 0), ('K1_SB_L4_C21', 0), ('K1_SB_L4_C22', 0), ('K1_SB_L4_C3', 0), ('K1_SB_L4_C4', 0), ('K1_SB_L4_C5', 0), ('K1_SB_L4_C6', 0), ('K1_SB_L4_C7', 0), ('K1_SB_L4_C8', 0), ('K1_SB_L4_C9', 0), ('K2_NB_L1_C2', 0), ('K2_NB_R4_L0_C0', 0), ('K2_NB_R4_L0_C1', 0), ('K2_NB_R4_L1_C0', 0), ('K2_NB_R4_L1_C1', 0), ('K2_NB_R4_L2_C0', 0), ('K2_NB_R4_L2_C1', 0), ('K2_NB_R4_L3_C0', 0), ('K2_NB_R4_L3_C1', 0), ('K2_NB_R5R6_L0_C0', 0), ('K2_NB_R5R6_L0_C1', 0), ('K2_NB_R5R6_L0_C2', 0), ('K2_NB_R5R6_L0_C3', 0), ('K2_NB_R5R6_L0_C4', 0), ('K2_NB_R5R6_L0_C5', 0), ('K2_NB_R5R6_L0_C6', 0), ('K2_NB_R5R6_L0_C7', 0), ('K2_NB_R5R6_L1_C0', 0), ('K2_NB_R5R6_L1_C1', 0), ('K2_NB_R5R6_L1_C3', 0), ('K2_NB_R5R6_L1_C4', 0), ('K2_NB_R5R6_L1_C5', 0), ('K2_NB_R5R6_L1_C6', 0), ('K2_NB_R5R6_L1_C7', 0), ('K2_NB_R5R6_L2_C0', 0), ('K2_NB_R5R6_L2_C1', 0), ('K2_NB_R5R6_L2_C2', 0), ('K2_NB_R5R6_L2_C3', 0), ('K2_NB_R5R6_L2_C4', 0), ('K2_NB_R5R6_L2_C5', 0), ('K2_NB_R5R6_L2_C6', 0), ('K2_NB_R5R6_L2_C7', 0), ('K2_SB_L0_C0', 0), ('K2_SB_L0_C1', 0), ('K2_SB_L0_C2', 0), ('K2_SB_L0_C3', 0), ('K2_SB_L0_C4', 0), ('K2_SB_L0_C5', 0), ('K2_SB_L0_C6', 0), ('K2_SB_L0_C7', 0), ('K2_SB_L0_C8', 0), ('K2_SB_L0_C9', 0), ('K2_SB_L1_C0', 0), ('K2_SB_L1_C1', 0), ('K2_SB_L1_C2', 0), ('K2_SB_L1_C3', 0), ('K2_SB_L1_C4', 0), ('K2_SB_L1_C5', 0), ('K2_SB_L1_C6', 0), ('K2_SB_L1_C7', 0), ('K2_SB_L1_C8', 0), ('K2_SB_L1_C9', 0), ('K2_SB_L2_C0', 0), ('K2_SB_L2_C1', 0), ('K2_SB_L2_C2', 0), ('K2_SB_L2_C3', 0), ('K2_SB_L2_C4', 0), ('K2_SB_L2_C5', 0), ('K2_SB_L2_C6', 0), ('K2_SB_L2_C7', 0), ('K2_SB_L2_C8', 0), ('K2_SB_L2_C9', 0), ('K2_SB_L3_C0', 0), ('K2_SB_L3_C1', 0), ('K2_SB_L3_C2', 0), ('K2_SB_L3_C3', 0), ('K2_SB_L3_C4', 0), ('K2_SB_L3_C5', 0), ('K2_SB_L3_C6', 0), ('K2_SB_L3_C7', 0), ('K2_SB_L3_C8', 0), ('K2_SB_L3_C9', 0), ('K2_SB_L4_C0', 0), ('K2_SB_L4_C1', 0), ('K2_SB_L4_C2', 0), ('K2_SB_L4_C3', 0), ('K2_SB_L4_C4', 0), ('K2_SB_L4_C5', 0), ('K2_SB_L4_C6', 0), ('K2_SB_L4_C7', 0), ('K2_SB_L4_C8', 0), ('K2_SB_L4_C9', 0), ('K3_NB_L0_C0', 0), ('K3_NB_L0_C1', 0), ('K3_NB_L0_C10', 0), ('K3_NB_L0_C11', 0), ('K3_NB_L0_C12', 0), ('K3_NB_L0_C13', 0), ('K3_NB_L0_C14', 0), ('K3_NB_L0_C15', 0), ('K3_NB_L0_C16', 0), ('K3_NB_L0_C17', 0), ('K3_NB_L0_C2', 0), ('K3_NB_L0_C3', 0), ('K3_NB_L0_C4', 0), ('K3_NB_L0_C5', 0), ('K3_NB_L0_C6', 0), ('K3_NB_L0_C7', 0), ('K3_NB_L0_C8', 0), ('K3_NB_L0_C9', 0), ('K3_NB_L1_C0', 0), ('K3_NB_L1_C1', 0), ('K3_NB_L1_C10', 0), ('K3_NB_L1_C11', 0), ('K3_NB_L1_C12', 0), ('K3_NB_L1_C13', 0), ('K3_NB_L1_C14', 0), ('K3_NB_L1_C15', 0), ('K3_NB_L1_C16', 0), ('K3_NB_L1_C17', 0), ('K3_NB_L1_C2', 0), ('K3_NB_L1_C3', 0), ('K3_NB_L1_C4', 0), ('K3_NB_L1_C5', 0), ('K3_NB_L1_C6', 0), ('K3_NB_L1_C7', 0), ('K3_NB_L1_C8', 0), ('K3_NB_L1_C9', 0), ('K3_NB_L2_C0', 0), ('K3_NB_L2_C1', 0), ('K3_NB_L2_C10', 0), ('K3_NB_L2_C11', 0), ('K3_NB_L2_C12', 0), ('K3_NB_L2_C13', 0), ('K3_NB_L2_C14', 0), ('K3_NB_L2_C15', 0), ('K3_NB_L2_C16', 0), ('K3_NB_L2_C17', 0), ('K3_NB_L2_C2', 0), ('K3_NB_L2_C3', 0), ('K3_NB_L2_C4', 0), ('K3_NB_L2_C5', 0), ('K3_NB_L2_C6', 0), ('K3_NB_L2_C7', 0), ('K3_NB_L2_C8', 0), ('K3_NB_L2_C9', 0), ('TDrive_L0_C0', 0), ('TDrive_L0_C1', 0), ('TDrive_L0_C10', 0), ('TDrive_L0_C11', 0), ('TDrive_L0_C12', 0), ('TDrive_L0_C2', 0), ('TDrive_L0_C3', 0), ('TDrive_L0_C4', 0), ('TDrive_L0_C5', 0), ('TDrive_L0_C6', 0), ('TDrive_L0_C7', 0), ('TDrive_L0_C8', 0), ('TDrive_L0_C9', 0), ('TDrive_lower_L0_C0', 0), ('TDrive_lower_L0_C1', 0), ('TDrive_lower_L0_C2', 0), ('TDrive_lower_L0_C3', 0), ('TDrive_upper_L0_C0', 0), ('TDrive_upper_L0_C1', 0), ('URd_lower_out_L0_C1', 0), ('URd_lower_out_L0_C10', 0), ('URd_lower_out_L0_C11', 0), ('URd_lower_out_L0_C2', 0), ('URd_lower_out_L0_C3', 0), ('URd_lower_out_L0_C4', 0), ('URd_lower_out_L0_C5', 0), ('URd_lower_out_L0_C6', 0), ('URd_lower_out_L0_C7', 0), ('URd_lower_out_L0_C8', 0), ('URd_lower_out_L0_C9', 0), ('URd_upper_out_L0_C1', 0), ('URd_upper_out_L0_C10', 0), ('URd_upper_out_L0_C11', 0), ('URd_upper_out_L0_C12', 0), ('URd_upper_out_L0_C13', 0), ('URd_upper_out_L0_C14', 0), ('URd_upper_out_L0_C15', 0), ('URd_upper_out_L0_C16', 0), ('URd_upper_out_L0_C17', 0), ('URd_upper_out_L0_C18', 0), ('URd_upper_out_L0_C19', 0), ('URd_upper_out_L0_C2', 0), ('URd_upper_out_L0_C3', 0), ('URd_upper_out_L0_C4', 0), ('URd_upper_out_L0_C5', 0), ('URd_upper_out_L0_C6', 0), ('URd_upper_out_L0_C7', 0), ('URd_upper_out_L0_C8', 0), ('URd_upper_out_L0_C9', 0)]

    
def main():
    # testing
    print(K1_SB_1.lane)
    print(K1_SB_1.arr_len)
    
    print(K1_NB_1.lane)
    print(K1_NB_1.arr_len)
    
    print(BGon_1.lane)
    print(BGon_1.arr_len)
    
    print(TDrive_lower.lane)
    print(TDrive_lower.arr_len)
    
    print(K2_SB_1.lane)
    print(K2_SB_1.arr_len)
    
    print(K2_NB_R4_1.lane)
    print(K2_NB_R4_1.arr_len)
    
    print(K2_NB_R5R6_1.lane)
    print(K2_NB_R5R6_1.arr_len)
    
    print(FdRosa_1.lane)
    print(FdRosa_1.arr_len)
    
    print(URd_lower_out.lane)
    print(URd_lower_out.arr_len)
    
    print(K3_NB_1.lane)
    print(K3_NB_1.arr_len)
    
main()