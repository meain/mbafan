from __future__ import print_function
from time import sleep

base_dir = '/sys/devices/platform/applesmc.768/'

# set fan control to manual mode
if open(base_dir+'fan1_manual').read()[0] is not '1':
    open(base_dir+'fan1_manual', 'w').write('1')

while (1):
    # There are other temp vales which I have no clue what to do,
    # this is what I hope we will need.
    avg_temp = 0
    core1_temp = open(base_dir+'temp8_input').read()
    core2_temp = open(base_dir+'temp9_input').read()
    avg_temp = int((float(core1_temp) + float(core2_temp))/2)

    # print(avg_temp)

    # get the correct fan speed (hopefully correct)
    fan_speed = '2000'
    if avg_temp > 60000:
        fan_speed = '6000'
    elif avg_temp < 60000 and avg_temp > 55000:
        fan_speed = '4500'
    elif avg_temp > 50000 and avg_temp < 55000:
        fan_speed = '3500'
    elif avg_temp > 45000 and avg_temp < 50000:
        fan_speed = '2000'
    else:
        fan_speed = '1500'

    # set fan speed
    open(base_dir+'fan1_output', 'w').write(fan_speed)
    sleep(10)
