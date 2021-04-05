### MODULES ##
import json
from os import system, name
import datetime

### CLASSES ###
class PoolTable: 
    def __init__(self, table_number): 
        self.table_number = table_number
        self.is_occupied = False
        self.start_time = None 
        self.end_time = None 
        self.total_time = None

    def dump(self):
        return {
                "number": self.table_number,
                "occupied": self.is_occupied,
                "startTime": self.start_time,
                "endTime": self.end_time,
                "totalTime": self.total_time
        }
#Encoder to change datetime to ISO when a datetime object is dumped to json
class DateTimeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()

        return super(DateTimeEncoder, self).default(obj)

### FUNCTIONS ###
file_name = datetime.datetime.now().strftime('%m-%d-%Y')#The lone variable, called by over half of the functions in utilities
#Screen clear function
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#Generates a JSON using the PoolTable class
def load_template():
    database = {}
    database['tables'] = []
    tables = []
    for index in range(1,13):
        pool_table = PoolTable(index)
        tables.append(pool_table)
        jsonStr = json.dumps([pool_table.dump() for pool_table in tables])
    data = json.loads(jsonStr)
    database['tables'] = data
    with open('%s.json' % file_name, 'w') as output:
        json.dump(database, output)

#Loads a JSON with the specified file name if one has been generated
def load_file():
    with open('%s.json' % file_name, 'r') as json_file:
        data = json.load(json_file)
    return data

def display_tables():#All tables
    load_file()
    print("-------------------------------------------------")
    for item in load_file()['tables']:
        print(f"Table Number: {item.get('number')}, Occupied: {item.get('occupied')}, Start Time: {item.get('startTime')}, End Time: {item.get('endTime')}, Total Time: {item.get('totalTime')}\n-------------------------------------------------")

def view_table(index):#Individual tables
    load_file()
    table = load_file()['tables'][index]
    print("-------------------------------------------------")
    for key, value in table.items():
        print(key, " ", value,"\n-------------------------------------------------")


def book_table(index):#Loads file, sets occupied to True, sets start date, and clears other dates.
    with open('%s.json' % file_name, 'r') as json_file:
        data = json.load(json_file)
    selection = index
    if data['tables'][selection]['occupied'] == True:
        print("Table is already occupied")
        return
    else:
        data['tables'][selection]['occupied'] = True
        data['tables'][selection]['startTime'] = datetime.datetime.now()
        data['tables'][selection]['endTime'] = None
        data['tables'][selection]['totalTime'] = None
    with open('%s.json' % file_name, 'w') as output:
        json.dump(data, output, cls=DateTimeEncoder)

def open_table(index):#Opens closed table, and calculates total time
    with open('%s.json' % file_name, 'r') as json_file:
        data = json.load(json_file)
    selection = index
    if data['tables'][selection]['occupied'] == False:
        print("Table is already open")
        return
    else:
        data['tables'][selection]['occupied'] = False
        data['tables'][selection]['endTime'] = datetime.datetime.now()
        raw_total_in = datetime.datetime.fromisoformat(data['tables'][selection]['startTime'])#Start time is in ISO format due to being pulled from the JSON
        temp_total_out = datetime.datetime.isoformat(data['tables'][selection]['endTime'])#End time is before the JSON dump and has to be converted
        raw_total_out = datetime.datetime.fromisoformat(temp_total_out)
        diff = raw_total_in - raw_total_out
        minutes = diff.total_seconds() / 60
        data['tables'][selection]['totalTime'] = (f"{minutes} minutes")
        with open('%s.json' % file_name, 'w') as output:
            json.dump(data, output, cls=DateTimeEncoder)