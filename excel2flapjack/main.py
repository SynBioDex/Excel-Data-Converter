import pandas as pd
from flapjack import Flapjack
from data import Data

#user = input()
#passwd = getpass.getpass()
fj = Flapjack('flapjack.rudge-lab.org:8000')  # Web Instance

def main():
    print("starting program")
    fj.log_in(username='saisam17', password='Il0vem$her')
    xls = pd.ExcelFile(r"C:\Users\saisa\FlapjackUploadMeasurements\tests\test_files\test_version7_flapjack_compiler_sbol3_v0022.xlsx")
    fj_data = Data(xls)

    hashmap = {}
    parse_chemical_fj_ids(hashmap, fj_data.chemical_df_dict)


def parse_chemical_fj_ids(hashmap, chemical_dict):
    for chem_id in chemical_dict:
        name = chemical_dict[chem_id]['Chemical Name']

        print(name)
        flapjack_id = get_flapjack(chemical_dict, chem_id)
        hashmap[chem_id] = flapjack_id
        print(hashmap)


def get_flapjack(chemical_dict, chem_id):
    return fj.create(chemical_dict[chem_id]['Chemical Name'], chemical_dict[chem_id]['Chemical Description'])
    # return fj.get(chemical_dict[id]['Chemical Description'])


if __name__ == "__main__":
    main()

"""fj = Flapjack(url_base='local-host:8000')
fj.log_in(username=saisam17, password=Flap123)

xls = pd.ExcelFile(r"/tests/test_files/test_version7_flapjack_compiler_sbol3_v0022.xlsx")

fj = Flapjack(url_base='localhost:8000')
fj.log_in(username=saisam17, password=Flap123)

for x in chemical_df.chemical_id:
    flapjack_post_chemical_name_request(x)
    # chemical = fj.create('chemical', name=x., description='This is a test')



hash_map ={}
for x in chemical_df.chemical_id:
    flapjack_post_chemical_name_request(x)
    flapjack_id = getrequest(x)
    hash_map[x] = flapjack_id
    #chemical = fj.create('chemical', name=x., description='This is a test')



#{'Chemical ID': 'Chemical2', 'Chemical Owner': True, 'Chemical Name': 'ATC', 'Chemical Description': 'ChemicalB', 'Pubchem ID': 'ID1', 'SBOL Object Type': 'ComponentDefinition', 'Molecule Type': 'SmallMolecule'}
#dict_keys(['Chemical ID', 'Chemical Owner', 'Chemical Name', 'Chemical Description', 'Pubchem ID', 'SBOL Object Type', 'Molecule Type'])
"""
