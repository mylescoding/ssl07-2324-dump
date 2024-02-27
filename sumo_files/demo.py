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
    run()