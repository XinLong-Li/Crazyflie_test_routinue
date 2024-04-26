#!/usr/bin/env python3
"""
This script shows a simple scripted flight path using the MotionCommander class.

Simple example that connects to the crazyflie at `URI` and runs a
sequence. Change the URI variable to your Crazyflie configuration.
"""

# To run this script, type "python3 crazyflie_test.py" in the terminal

import logging
import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M/E7E7E7E701' 

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        # We take off when the commander is created
        with MotionCommander(scf) as mc:
            print('Taking off!')
            time.sleep(1)

            # There is a set of functions that move a specific distance
            # We can move in all directions

            print('Moving up 0.2m')
            mc.up(0.2)
            # Wait a bit
            time.sleep(1)
            
            # mc.move_distance(0.5, 0.5, 0.0, 0.2)
            # print('Moving distance: 0.5, 0.5, 0.0')
            # time.sleep(1)

            print('Moving down 0.2m')
            mc.down(0.2)
            # Wait a bit
            time.sleep(1)

            # We land when the MotionCommander goes out of scope
            print('Landing!')
