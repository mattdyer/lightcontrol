import sys
import subprocess
import time
from pyHS100 import SmartBulb


if len(sys.argv) >= 3:
	idle_timeout = int(sys.argv[1])
	ips = sys.argv[2].split(",")
	
	dim_timeout = 1000
	
	idle = False
	
	office_lights = []
	
	for ip in ips:
		office_lights.append(SmartBulb(ip))
		
	print(office_lights)
	
	while True:
		
		idleargs = ["xprintidle"]
		
		current_idle_time = int(subprocess.check_output(idleargs))
		
		print(current_idle_time)
		
		if(current_idle_time > (idle_timeout - dim_timeout)):
			for light in office_lights:
				light.brightness = 50
		
		
		if(current_idle_time > idle_timeout):
			for light in office_lights:
				light.turn_off()
		else:
			for light in office_lights:
				light.turn_on()
				light.brightness = 100
		
		time.sleep(0.5)

else:
	print("requires timeout and IP list example: control.py 10000 192.168.1.10,192.168.1.11")
