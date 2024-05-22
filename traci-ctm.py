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

from_params = "Phase 0" , {}
def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options


    

def getParams():
    edge_list = traci.edge.getIDList()

    cells = traci.lanearea.getIDList()
    #print(cells)
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
    
    print(cells)
    cell_dict = dict()
    old_kuf_phase = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        if (step%5 == 0):
            if (traci.trafficlight.getPhase("kuf") in [0, 3, 6, 9]):
                kuf_phase = traci.trafficlight.getPhase("kuf")
                kuf_phase_name = traci.trafficlight.getPhaseName("kuf")
            phase_name = kuf_phase_name.split(" - ")
            for cell in cells:
                #print(cell)
                cell_vehicles = traci.lanearea.getLastStepVehicleNumber(cell)
                #print(cell_vehicles)
                occupancy = traci.lanearea.getLastStepOccupancy(cell)
                #print(occupancy)
                #if cell_vehicles != 0:
                cell_dict[cell] = (cell_vehicles,occupancy)
                #cell_dict.update(cell:(cell_vehicles,occupancy))
            old_kuf_phase = kuf_phase
            print(old_kuf_phase)

        if(len(cell_dict)>0):
            #help = phase_name[0], cell_dict
            #print(phase_name[0])
            #print(cell_list)
            #print(help)
            from_params = phase_name, cell_dict
            jaja, huhu = from_params
            print(jaja)
            print(huhu)
        cell_dict = {}
        step +=1
        traci.simulationStep()





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
