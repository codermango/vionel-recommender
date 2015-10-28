import json
import time

with open('/test.txt') as f:
	j = json.loads(f.read())
	print json.dumps(j, indent = 4)
	time.sleep(60)