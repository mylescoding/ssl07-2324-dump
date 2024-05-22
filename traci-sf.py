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


    

def getLaneParams():
    edge_list = traci.edge.getIDList()
    lane_list = traci.lane.getIDList()
    output_list = []
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
    # road_position_direction_lanenum : smaller lanes part of that lane
    lane_dict = {
        "katip_t_nb_0": ['R1_0', 'R2_0'],
        "katip_t_nb_1": ['R1_1', 'R2_1'],
        "katip_t_nb_2": ['R1_2', 'R2_2'],
        "katip_t_nb_3": ['R1_3', 'R2_3'],
        "katip_t_sb_0": ['L1_0'],
        "katip_t_sb_1": ['L1_1'],
        "katip_t_sb_2": ['L1_2'],
        "katip_t_sb_3": ['L1_3'],
        "katip_t_sb_4": ['L1_4'],
        "thornton-drive-lower-out_0": ['thornton-drive-lower-out_0'],
        "thornton-drive-in_0": ['thornton-drive-in_0'],
        "katip_m_u_nb_0": ['R4_0'],
        "katip_m_u_nb_1": ['R4_1'],
        "katip_m_u_nb_2": ['R4_2'],
        "katip_m_u_nb_3": ['R4_3'],
        "katip_m_l_nb_0": ['R5_0', 'R6_0'],
        "katip_m_l_nb_1": ['R5_1', 'R6_1'],
        "katip_m_l_nb_2": ['R5_2', 'R6_2'],
        "b.gonzales-road_0" : ['b.gonzales-road_0'],
        "b.gonzales-road_1" : ['b.gonzales-road_1'],
        "katip_m_sb_0": ['L2_0','L3_0','L4_0','L5_0','L6_0'],
        "katip_m_sb_1": ['L2_1','L3_1','L4_1','L5_1','L6_1'],
        "katip_m_sb_2": ['L2_2','L3_2','L4_2','L5_2','L6_2'],
        "katip_m_sb_3": ['L2_3','L3_3','L4_3','L5_3','L6_3'],
        "katip_m_sb_4": ['L2_4','L3_4','L4_4','L5_4','L6_4'],
        "univ-road-upper-out_0" : ['univ-road-upper-out_0'],
        "univ-road-upper-in_0" : ['univ-road-upper-in_0'],
        "univ-road-lower-out_0" : ['univ-road-lower-out_0'],
        "univ-road-lower-in_0" : ['univ-road-lower-in_0'],
        "f.dela-rosa-road_1" : ['f.dela-rosa-road_1'],
        "f.dela-rosa-road_0" : ['f.dela-rosa-road_0'],
        "katip_b_sb_0": ['L7_0','L8_0','L9_0','L10_0','L11_0','L12_0'],
        "katip_b_sb_1": ['L7_1','L8_1','L9_1','L10_1','L11_1','L12_1'],
        "katip_b_sb_2": ['L7_2','L8_2','L9_2','L10_2','L11_2','L12_2'],
        "katip_b_sb_3": ['L7_3','L8_3','L9_3','L10_3','L11_3','L12_3'],
        "katip_b_sb_4": ['L7_4','L8_4','L9_4','L10_4','L11_4','L12_4'],
        "katip_b_nb_0": ['R7_0'],
        "katip_b_nb_1": ['R7_1'],
        "katip_b_nb_2": ['R7_2']
    }
    lane_veh_count_dict = {key + "_count": 0 for key in lane_dict}
    
    for lane in lane_list:
        lane_veh_count = traci.lane.getLastStepVehicleNumber(lane)
        for key, value in lane_dict.items():
            if lane in value:
                lane_veh_count_dict[str(key + "_count")] += lane_veh_count
                break
    print(lane_veh_count_dict)
    
    return lane_veh_count_dict
    



# TraCI control loop
def run():

    step = 0

    # print("PROGRAM LOGICS")
    # print("Katipunan Univ Road F Dela Rosa")
    # print(traci.trafficlight.getAllProgramLogics("kuf"))
    # print("Katipunan B Gonzales Thornton")
    # print(traci.trafficlight.getAllProgramLogics("kbt"))
    
    
    # print("PROGRAM DEFINITIONS")
    # print("Katipunan Univ Road F Dela Rosa")
    # print(traci.trafficlight.getCompleteRedYellowGreenDefinition("kuf"))
    # print("Katipunan B Gonzales Thornton")
    # print(traci.trafficlight.getCompleteRedYellowGreenDefinition("kbt"))
    
    # print(traci.trafficlight.getPhase("kuf"))
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
            vehicle_count_dict = getLaneParams()
            print(vehicle_count_dict)
            # eurick-greentime = function(kuf_phase_name,vehicle_count_dict)
            # traci.trafficlight.setPhaseDuration(eurick-greentime)   
            #this tracks green changes in KUF
        old_kuf_phase = kuf_phase
        
        if(traci.trafficlight.getPhase("kbt") in [0,3,6,9]):
            kbt_phase = traci.trafficlight.getPhase("kbt")
            kbt_phase_name = traci.trafficlight.getPhase("kbt")
        if(kbt_phase != old_kbt_phase):
            print("CURRENT PHASE AND NAME FOR KBT: " + str(kbt_phase) + " : " + str(kbt_phase_name))
            # this indicates that a red light turned into a green
            # we call eurick's code here, then retrieve the green time for the phase
            vehicle_count_dict = getLaneParams()
            # eurick-greentime = function(kbtvehicle_count_dict)
            # traci.trafficlight.setPhaseDuration(eurick-greentime)
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
    #getLaneParams()
    
    run()