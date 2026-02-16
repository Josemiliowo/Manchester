import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/emilio/ManchesterRobotics/ch1_ws/src/install/challenge1'
