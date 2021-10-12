#!/usr/bin/env python
# //==============================================================================
# /*
#     Software License Agreement (BSD License)
#     Copyright (c) 2020-2021 Johns Hopkins University (JHU), Worcester Polytechnic Institute (WPI) All Rights Reserved.


#     All rights reserved.

#     Redistribution and use in source and binary forms, with or without
#     modification, are permitted provided that the following conditions
#     are met:

#     * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.

#     * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.

#     * Neither the name of authors nor the names of its contributors may
#     be used to endorse or promote products derived from this software
#     without specific prior written permission.

#     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#     "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#     LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#     FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#     COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#     INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#     BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#     LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#     CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#     LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#     ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#     POSSIBILITY OF SUCH DAMAGE.


#     \author    <amunawar@jhu.edu>
#     \author    Adnan Munawar
#     \version   1.0
# */
# //==============================================================================

from surgical_robotics_challenge.ecm_arm import ECM
import time
import sys
from ambf_client import Client
from surgical_robotics_challenge.utils.jnt_control_gui import JointGUI


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


c = Client('ecm_test')
c.connect()
time.sleep(0.5)

ecm = ECM(c, 'CameraFrame')
gui = JointGUI("ECM JOINTS", 4, ["j0", "j1", "j2", "j3"], resolution=0.00001)
dt = 0.005
while True:
    try:
        gui.App.update()
        ecm.servo_jp(gui.jnt_cmds)
        time.sleep(dt)
    except KeyboardInterrupt:
        print("Bye")
        sys.exit()