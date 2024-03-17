import random

x = random.randint(0,4)

source_demand_dict = {'kbt-4': 46, 'kbt-4a': 426, 'kbt-5': 3886, 'kbt-7': 643, 'kbt-8': 13, 'kbt-9': 23, 'kbt-10': 97, 'kbt-12': 10, 'kuf-2': 3803, 'kuf-3': 245, 'kuf-3a': 27, 'kuf-7': 155, 'kuf-8': 101, 'kuf-8a': 98, 'kuf-9': 79, 'kuf-10b': 199, 'kuf-10c': 506, 'kuf-12a': 0}
intermediate_demand_dict = {'kuf-4':135, 'kuf-4a_to_kbt-2': x, 'kuf-4a_to_kbt-3':4-x, 'kuf-4b':115, 'kuf-5':3754, 'kbt-2':3925, 'kbt-3':37}

source_demand_dict_wholeday = {
        'kbt-4': [46, 52, 56, 43, 40, 36, 36, 46, 44, 48, 52, 59, 52, 46],
        'kbt-4a': [426, 483, 518, 397, 365, 334, 331, 421, 407, 446, 475, 541, 483, 427],
        'kbt-5': [3886, 4402, 4717, 3615, 3328, 3045, 3014, 3836, 3710, 4060, 4331, 4932, 4403, 3890],
        'kbt-7': [643, 728, 780, 598, 550, 504, 498, 634, 613, 671, 716, 815, 728, 643],
        'kbt-8': [13, 15, 16, 13, 12, 11, 10, 13, 13, 14, 15, 17, 15, 13],
        'kbt-9': [23, 27, 28, 22, 20, 18, 18, 23, 22, 25, 26, 30, 27, 23],
        'kbt-10': [97, 110, 118, 90, 83, 76, 75, 96, 93, 101, 108, 123, 110, 97],
        'kbt-12': [10, 12, 13, 10, 9, 8, 8, 10, 10, 11, 12, 13, 12, 10],
        'kuf-2': [3803, 4308, 4615, 3537, 3257, 2980, 2949, 3754, 3631, 3973, 4238, 4826, 4309, 3807],
        'kuf-3': [245, 278, 297, 228, 210, 192, 190, 242, 234, 256, 273, 311, 278, 245],
        'kuf-3a': [27, 31, 33, 25, 23, 21, 21, 27, 26, 28, 30, 35, 31, 27],
        'kuf-7': [155, 176, 188, 144, 133, 122, 120, 153, 148, 162, 173, 197, 176, 155],
        'kuf-8': [101, 114, 123, 94, 86, 79, 78, 100, 96, 105, 112, 128, 114, 101],
        'kuf-8a': [98, 112, 120, 92, 84, 77, 76, 97, 94, 103, 110, 125, 112, 99],
        'kuf-9': [79, 90, 96, 74, 68, 62, 61, 78, 76, 83, 88, 101, 90, 79],
        'kuf-10b': [199, 225, 241, 185, 170, 156, 154, 196, 190, 208, 221, 252, 225, 199],
        'kuf-10c': [506, 574, 615, 471, 434, 397, 393, 500, 483, 529, 564, 643, 574, 507],
        'kuf-12a': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
    
intermediate_demand_dict_wholeday = {
        'kuf-4': [135, 153, 164, 125, 115, 106, 105, 133, 129, 141, 150, 171, 153, 135],
        'kuf-4a': [4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
        'kuf-4a_to_kbt-2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'kuf-4a_to_kbt-3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'kuf-4b': [115, 130, 140, 107, 98, 90, 89, 113, 110, 120, 128, 146, 130, 115],
        'kuf-5': [3754, 4252, 4555, 3491, 3214, 2941, 2911, 3705, 3583, 3922, 4183, 4764, 4253, 3757],
        'kbt-2': [3925, 4446, 4763, 3651, 3361, 3076, 3044, 3874, 3747, 4100, 4373, 4981, 4447, 3928],
        'kbt-3': [37, 42, 45, 35, 32, 29, 29, 37, 35, 39, 41, 47, 42, 37]
    }


# split demand from kuf-4a to both kbt-2 and kbt-3
for idx in range(14):
    x = random.randint(0,intermediate_demand_dict_wholeday['kuf-4a'][idx])
    y = intermediate_demand_dict_wholeday['kuf-4a'][idx] - x 
    intermediate_demand_dict_wholeday['kuf-4a_to_kbt-2'][idx] = x
    intermediate_demand_dict_wholeday['kuf-4a_to_kbt-3'][idx] = y


def createXML_hourly(dic, idx):
    count = 0
    xml_entries = []
    
    start_end_times = [('0.0', '3600.0'), ('3600.0', '7200.0'), ('7200.0', '10800.0'), ('10800.0', '14400.0'), ('14400.0', '18000.0'), ('18000.0', '21600.0'), ('21600.0', '25200.0'), ('25200.0', '28800.0'), ('28800.0', '32400.0'), ('32400.0', '36000.0'), ('36000.0', '39600.0'), ('39600.0', '43200.0'), ('43200.0', '46800.0'), ('46800.0', '50400.0')]
    
    for key in dic:
        
        xml_entry = '<flow id ="f_' + str(count) +'"' + ' type = "CAR" begin="'  + str(start_end_times[idx][0]) + '0" route="' + str(key) + '" end="'+ str(start_end_times[idx][1]) + '0" vehsPerHour="'+ str(dic[key]) +'"/>' 
        count = count + 1
        if dic[key] != 0:
            xml_entries.append(xml_entry)

    for entry in xml_entries:
        print(entry)
        pass

    return

def createXML_wholeday(dic):
    count = 0
    xml_entries = []
    
    start_end_times = [('0.0', '3600.0'), ('3600.0', '7200.0'), ('7200.0', '10800.0'), ('10800.0', '14400.0'), ('14400.0', '18000.0'), ('18000.0', '21600.0'), ('21600.0', '25200.0'), ('25200.0', '28800.0'), ('28800.0', '32400.0'), ('32400.0', '36000.0'), ('36000.0', '39600.0'), ('39600.0', '43200.0'), ('43200.0', '46800.0'), ('46800.0', '50400.0')]
    for idx in range(14):
        for key in dic:
            xml_entry = '<flow id ="f_' + str(count) +'"' + ' type = "CAR" begin="'  + str(start_end_times[idx][0]) + '0" route="' + str(key) + '" end="'+ str(start_end_times[idx][1]) + '0" vehsPerHour="'+ str(dic[key]) +'"/>' 
            count = count + 1
            if dic[key] != 0:
                xml_entries.append(xml_entry)

    for entry in xml_entries:
        print(entry)
        

    return

def distribute(time_slot):

    for source_node in sources:
        sum_out_src = 0
        if (source_node.getPossibleRoutes() != []):
            for intermediate_node in intermediates:  
                if (intermediate_node.getIntermediate_Node_Name() in source_node.getPossibleRoutes()):
                    #print( source_node.getPossibleRoutes()) 
                    # kbt5: ["kuf4", "kuf4a_kbt2", "kuf4a_kbt3", "kuf4b", "kuf5"]
                    #print("Intermediate: " + str(intermediate_node.getIntermediate_Node_Name()))
                    #sum_out_src += intermediate_demand_dict[intermediate_node.getIntermediate_Node_Name()]
                    sum_out_src += intermediate_demand_dict_wholeday[intermediate_node.getIntermediate_Node_Name()][time_slot]
                    #print("sum_out_src is:" + str(sum_out_src))
            for route in source_node.getPossibleRoutes():
                #once we get the some, get ratio
                ratio = intermediate_demand_dict_wholeday[route][time_slot] / sum_out_src
                #print("ratio:" + str(ratio))
                demand = round(source_demand_dict_wholeday[source_node.getSourceName()][time_slot] * ratio)
                new_route_name = str(source_node.getSourceName()) + "_to_" + str(route)
                route_dict[new_route_name] = demand    
                route_name_list.append(new_route_name)
                    
        elif(source_node.getPossibleRoutes() == []):
            route_dict[source_node.getSourceName()] = source_demand_dict_wholeday[source_node.getSourceName()][time_slot]
            route_name_list.append(source_node.getSourceName())
    return

class Source:
    def __init__(self, source_name, possible_routes):
        self.source_name = source_name
        self.possible_routes = possible_routes
        
    def getSourceName(self):
        return self.source_name
    def getPossibleRoutes(self):
        return self.possible_routes

class Intermediate:
    def __init__(self, node_name, possible_sources):
        self.node_name = node_name
        self.possible_sources = possible_sources
    def getIntermediate_Node_Name(self):
        return self.node_name
    def getPossibleSources(self):
        return self.possible_sources

#source demands, only for 6-7am will turn into arrays for the whole thing
kbt4 = Source("kbt-4",[])
kbt4a = Source("kbt-4a",[])
kbt5 = Source("kbt-5",["kuf-4", "kuf-4a_to_kbt-2", "kuf-4a_to_kbt-3", "kuf-4b", "kuf-5"])
kbt7 = Source("kbt-7",[])
kbt8 = Source("kbt-8",[])
kbt9 = Source("kbt-9",["kuf-4", "kuf-4a_to_kbt-2", "kuf-4a_to_kbt-3", "kuf-4b", "kuf-5"])
kbt10 = Source("kbt-10",["kuf-4", "kuf-4a_to_kbt-2", "kuf-4a_to_kbt-3", "kuf-4b", "kuf-5"])
kbt12 = Source("kbt-12",[])

kuf2 = Source("kuf-2",["kbt-2", "kbt-3"])
kuf3 = Source("kuf-3",[])
kuf3a = Source("kuf-3a",[])
kuf7 = Source("kuf-7",["kbt-2", "kbt-3"])
kuf8 = Source("kuf-8",[])
kuf8a = Source("kuf-8a",[])
kuf9 = Source("kuf-9",[])
kuf10b = Source("kuf-10b",[])
kuf10c = Source("kuf-10c",[])
kuf12a = Source("kuf-12a",[])

sources = [kbt4, kbt4a, kbt5, kbt7, kbt8, kbt9, kbt10, kbt12, kuf2, kuf3, kuf3a, kuf7, kuf8, kuf8a, kuf9, kuf10b, kuf10c, kuf12a]

#intermediate nodes

kuf4 = Intermediate("kuf-4",["kbt-10","kbt-5", "kbt-9"])
kuf4a_kbt2 = Intermediate("kuf-4a_to_kbt-2", ["kbt-10","kbt-5", "kbt-9"])
kuf4a_kbt3 = Intermediate("kuf-4a_to_kbt-3", ["kbt-10","kbt-5", "kbt-9"])
kuf4b = Intermediate("kuf-4b", ["kbt-10","kbt-5", "kbt-9"])
kuf5 = Intermediate("kuf-5", ["kbt-10","kbt-5", "kbt-9"])
kbt2 = Intermediate("kbt-2",["kuf4a_to_kbt2","kuf4a_to_kbt3","kuf-12a","kuf-2", "kuf-7"])
kbt3 = Intermediate("kbt-3",["kuf-4a_to_kbt-2","kuf-4a_to_kbt-3","kuf-12a","kuf-2", "kuf-7"])

intermediates = [kuf4, kuf4a_kbt2, kuf4a_kbt3, kuf4b, kuf5, kbt2, kbt3]


route_dict = {}
route_name_list=[]

# FOR HOURLY XML FILE

#time_idx = 10 # set time index here, 0 is 6-7 AM, 1 is 7-8 AM, ... ,13 is 7-8 PM
#distribute(time_idx)
#createXML_hourly(route_dict, time_idx)


# WHOLE DAY XML FILE
for idx in range(14):
    distribute(idx)
createXML_wholeday(route_dict)

    
    






