#!/usr/bin/env python

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


    

def getParams():
    edge_list = traci.edge.getIDList()
    step = 0
    
    road_list = {
        "katip_t_nb": ['R1', 'R2', 'R3'],
        "katip_t_sb": ['L1'],
        "thornton_nb": ['thornton-drive-extension-outward', 'thornton-drive-upper-out'],
        "thornton_sb": ['thornton-drive-extension-outward', 'thornton-drive-lower-out'],
        "thornton_in": ['thornton-drive-in', 'thornton-drive-extension-towards'],
        "bgon": ['b.gonzales-extension-road', 'b.gonzales-road'],
        "katip_m_nb": ['R4', 'R5', 'R6'],
        "katip_m_sb": ['L2', 'L3', 'L4', 'L5', 'L6'],
        "univrd_t_out": ['univ-road-upper-out'],
        "univrd_t_in": ['univ-road-upper-in'],
        "univrd_b_out": ['univ-road-lower-out'],
        "univrd_b_in": ['univ-road-lower-in'],
        "fdrosa": ['f.dela-rosa-extension-road', 'f.dela-rosa-road'],
        "katip_b_nb": ['R7'],
        "katip_b_sb": ['L7', 'L8', 'L9', 'L10', 'L11', 'L12']
    }
    
    #vehicles in the road params
    road_veh_count = {key + "_count": 0 for key in road_list}
    road_veh_wait_time = {key + "_wait_time": 1 for key in road_list}
    road_veh_accumulated_wait_time = {key + "_accl_wait_time": 1 for key in road_list}
    
    #road network params
    road_lengths = {key + "_len": 1 for key in road_list}
 
    
    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        if (step%1000 == 0):
            for edge in edge_list:
                veh_count_in_edge = traci.edge.getLastStepVehicleNumber(edge)
                veh_wait_in_edge = traci.edge.getWaitingTime(edge)
                #veh_accl_wait_in_edge = traci.edge.getAccumulatedWaitingTime(edge)

                for key, value in road_list.items():
                    if edge in value:
                        road_veh_count[str(key + "_count")] += veh_count_in_edge
                        road_veh_wait_time[str(key + "_wait_time")] += veh_wait_in_edge
                        #road_veh_accumulated_wait_time[str(key + "_accl_wait_time")] = veh_accl_wait_in_edge #is this correct HAHAHA will do some checking

                        
            print(road_veh_count)
            print(road_veh_wait_time)
            #print(road_veh_accumulated_wait_time)
            road_veh_count = {key + "_count": 0 for key in road_list} #reset
            
        step +=1
    
    



# TraCI control loop
def run():
    edge_list = traci.edge.getIDList()
    #   print(edge_list)
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
     
        if step%100 == 0:
            for edge in edge_list:
                veh_count_in_edge = traci.edge.getLastStepVehicleNumber(edge)
                if (veh_count_in_edge != 0):
                    print("Current number of vehicles in edge " + str(edge) + " is " + str(veh_count_in_edge))
        
            pass
        step += 1

    traci.close()
    sys.stdout.flush()



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
    getParams()