import json
import os

def append_record(record):
    with open('my_file', 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)

# demonstrate a program writing multiple records
for i in range(10):
    my_dict = {'number':i}
    print(my_dict)
    append_record(my_dict)