import sys
import subprocess
import time

if len(sys.argv) >= 2:
	idle_timeout = sys.argv[1]
	
	for i in range(1,5):
		
		wargs = ["w"]
		
		result = subprocess.check_output(wargs)
		
		print(result)
		print("")
		
		time.sleep(20)
		
	
else:
	print("usage: One argument required lightcontrol.py [idle_timeout]")