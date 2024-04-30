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
 
    for edge in edge_list:
        veh_count_in_edge = traci.edge.getLastStepVehicleNumber(edge)
        veh_wait_in_edge = traci.edge.getWaitingTime(edge)
        #veh_accl_wait_in_edge = traci.edge.getAccumulatedWaitingTime(edge)

        for key, value in road_list.items():
            if edge in value:
                road_veh_count[str(key + "_count")] += veh_count_in_edge
                road_veh_wait_time[str(key + "_wait_time")] += veh_wait_in_edge
                #road_veh_accumulated_wait_time[str(key + "_accl_wait_time")] = veh_accl_wait_in_edge #is this correct HAHAHA will do some checking

    output_dict = road_veh_count                    
    #print(road_veh_count)
    #print(road_veh_wait_time)
    #print("as of printing, current ")
    #print(road_veh_accumulated_wait_time)
    road_veh_count = {key + "_count": 0 for key in road_list} #reset
    
    return output_dict
    
    
            
  
    
    



# TraCI control loop
def run():

    step = 0
    
    #phase_dict =
    


    #print(traci.lane.getIDList())
    print("PROGRAM LOGICS")
    print("Katipunan Univ Road F Dela Rosa")
    print(traci.trafficlight.getAllProgramLogics("kuf"))
    print("Katipunan B Gonzales Thornton")
    print(traci.trafficlight.getAllProgramLogics("kbt"))
    
    
    print("PROGRAM DEFINITIONS")
    print("Katipunan Univ Road F Dela Rosa")
    print(traci.trafficlight.getCompleteRedYellowGreenDefinition("kuf"))
    print("Katipunan B Gonzales Thornton")
    print(traci.trafficlight.getCompleteRedYellowGreenDefinition("kbt"))
    
    print(traci.trafficlight.getPhase("kuf"))
    old_kuf_phase = 0
    old_kbt_phase = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep() # move one second in simulation
        #print(str(traci.trafficlight.getPhase("kuf")) + " : " + str(traci.trafficlight.getPhaseDuration("kuf")))
        if(traci.trafficlight.getPhase("kuf") in [0,3,6,9]):
            kuf_phase = traci.trafficlight.getPhase("kuf")
            kuf_phase_name = traci.trafficlight.getPhaseName("kuf")
        if(kuf_phase != old_kuf_phase):
            print("CURRENT PHASE AND NAME FOR KUF: " + str(kuf_phase) + " : " + str(kuf_phase_name))    
            # this indicates that a red light turned into a green
            # we call eurick's code here, then retrieve the green time for the phase
            vehicle_count_dict = getParams()
            print(vehicle_count_dict)
            # eurick-greentime = function(kuf_phase_name,vehicle_count_dict)
            # traci.trafficlight.setPhaseDuration(eurick-greentime)
            print("LANES")
            print(traci.trafficlight.getControlledLanes("kuf"))
            print("LINKS")
            print(traci.trafficlight.getControlledLinks("kuf"))    
            #this tracks green changes in KUF
        old_kuf_phase = kuf_phase
        
        if(traci.trafficlight.getPhase("kbt") in [0,3,6,9]):
            kbt_phase = traci.trafficlight.getPhase("kbt")
            kbt_phase_name = traci.trafficlight.getPhase("kbt")
        if(kbt_phase != old_kbt_phase):
            print("CURRENT PHASE AND NAME FOR KBT: " + str(kbt_phase) + " : " + str(kbt_phase_name))
            # this indicates that a red light turned into a green
            # we call eurick's code here, then retrieve the green time for the phase
            # vehicle_count_dict = getParams(kbt)
            # eurick-greentime = function(kbtvehicle_count_dict)
            # traci.trafficlight.setPhaseDuration(eurick-greentime)
            print("LANES")
            print(traci.trafficlight.getControlledLanes("kbt"))
            print("LINKS")
            print(traci.trafficlight.getControlledLinks("kbt"))   
            #this tracks green changes in KBT
        old_kbt_phase = kbt_phase
        
        
     

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
    #getParams()
    
    run()