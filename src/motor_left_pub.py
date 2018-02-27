#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
import time


def main():
    rospy.init_node('motor_left_publisher')

    pub_motor_left = rospy.Publisher('motor/dps/left', Int16, queue_size=1)

    msg = Int16()
    # dps 35 low, max 460
    while(True):
        msg.data = int(input("speed: "))
        print(msg.data)
        pub_motor_left.publish(msg)

        time.sleep(0.5)


if __name__ == '__main__':
    main()