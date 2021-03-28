#!/usr/bin/env python
# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy
from ariac_example import ariac_example


def main():

    rospy.init_node("ariac_example_node")
    
    competition = ariac_example.MyCompetition()
    ariac_example.connect_callbacks(competition)
    rospy.loginfo("Setup complete.")

    ariac_example.start_competition()

    if not competition.has_been_zeroed:
        competition.has_been_zeroed = True
        rospy.loginfo("Sending arm to zero joint positions...")
        competition.send_arm_to_state([0] * len(competition.arm_joint_names))

    rospy.spin()


if __name__ == '__main__':
    main()
