# senior_design_26-kirby

After connecting the Pi to the Flight Controller through USB C, run this in /Downloads folder:

    mavproxy.py --master=/dev/ttyACM0 --baudrate 115200

To verify the connection and open MAVProxy

To run the colordetection.py: 

    ros2 launch realsense2_camera rs_launch.py

On a separate terminal: 

    ros2 run kirbyros colordetection
    
