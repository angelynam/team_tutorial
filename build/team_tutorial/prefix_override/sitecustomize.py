import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/angelyna/roboracer_ws/src/team_tutorial/install/team_tutorial'
