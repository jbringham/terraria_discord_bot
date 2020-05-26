import subprocess
import re

def check_online():
	output = subprocess.run(["screen", "-ls"], stdout=subprocess.PIPE)
	return re.search("terraria_server", str(output)) != None
#output = sp.check_output(["screen", "-ls"]).decode("utf-8")
#print(output)

print(str(check_online()))

