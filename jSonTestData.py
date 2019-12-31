""" This is Test Data file for jSon & SQl """

import json
from datetime import date


dates = date.today()
print (dates)

json_String = json.dumps(str(dates))

print (type(json_String))