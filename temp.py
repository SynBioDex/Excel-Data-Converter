import random
import pandas as pd
from flapjack import Flapjack
import getpass

sbol_ids = ["1", "2", "3"]

hash_map = {}

user = input()
passwd = getpass.getpass()
#fj = Flapjack('flapjack.rudge-lab.org:8000') #Web Instance
fj = Flapjack(url_base='localhost:8000') #Local Instance
fj.log_in(username=user, password=passwd)

chemical_df = pd.read_excel('/Users/gonzalovidal/Documents/GitHub/FlapjackUploadMeasurements-master/tests/test_files/test_version7_flapjack_compiler_sbol3_v0022.xlsx',
     sheet_name="Chemical",
     skiprows=18, engine='openpyxl')
chemical_dict = chemical_df.to_dict('index')
print(chemical_dict)

def get_flapjack(id):
    return fj.create(chemical_dict[id]['Chemical Name'], chemical_dict[id]['Chemical Description'])
 

for id in chemical_dict:
    name = chemical_dict[id]['Chemical Name']
    print(name)
    flapjack_id = get_flapjack(id)
    hash_map[id] = flapjack_id
    print(hash_map)
