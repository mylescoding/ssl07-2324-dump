class Cell:
    def __init__(self, lane, length, max_speed, car_num, busy, tick):
        self.lane = lane
        self.busy = busy
        self.car_num = car_num
        self.arr = [0] * int(length/(max_speed/tick))
        
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
        
def main():
    # testing
    print(K1_SB_1.lane)
    print(K1_SB_1.arr)
    
main()