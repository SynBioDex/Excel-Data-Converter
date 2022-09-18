import os
import numpy as np
import pandas as pd
from flapjack import Flapjack


fj_url = "localhost:8000"
fj_username = "saisam17"
fj_pass = "Flap123"

direct = __file__
test_file_path = os.path.join(os.path.split(os.path.split(direct)[0])[0], 'tests', 'test_files')
excel_path = os.path.join(test_file_path, "test_version7_flapjack_compiler_sbol3_v0022.xlsx")


def flapjack_upload(fj_url, fj_user, fj_pass, excel_path):
    # hash_map = {}

    # # log in to flapjack instance
    # fj = Flapjack(url_base=fj_url) #Local Instance
    # fj.log_in(username=fj_user, password=fj_pass)

    # # read in Excel Data
    # xls = pd.ExcelFile(excel_path)

    # chemical_df = xls.parse('Chemical', skiprows=18, index_col='Chemical ID')
    # # chemical_id = chemical_df.to_dict('records')
    # chemical_dict = chemical_df.to_dict('index')

    # for id in chemical_dict:
    #     name = chemical_dict[id]['Chemical Name']
    #     print(name)
    #     flapjack_id = fj.create(chemical_dict[id]['Chemical Name'], chemical_dict[id]['Chemical Description'])
    #     hash_map[id] = flapjack_id

    # for key in chemical_dict:
    #     flapjack_chemical_id = fj.create('chemical', name=chemical_dict[key]['Chemical Name'], description=chemical_dict[key]['Chemical Description'])
    #     hash_map[key] = flapjack_chemical_id.id[0]

    # supplement_df = xls.parse('Supplement', skiprows=18, index_col='Supplement ID')
    # # supplement_id = supplement_df.to_dict('records')
    # supplement_dict = supplement_df.to_dict('index')

    for sup_key in supplement_dict:
        chemical_name = supplement_dict[key]['Chemical ID']
        chemical_key = hash_map[chemical_name]
        sup_name = supplement_dict[sup_key]['Supplement Name']
        sup_conc = supplement_dict[sup_key]['Concentration']
        flapjack_supplement_id = fj.create('supplement', name=sup_name, chemical=chemical_key, concentration=sup_conc)
        hash_map[key] = flapjack_supplement_id.id[0]

    ################################
    vector_df = xls.parse('Vector', skiprows=18, index_col='Vector ID')
    # vector_id = vector_df.to_dict('records')
    vector_dict = vector_df.to_dict('index')

    for vec_key in vector_dict:
        dna_name = vector_dict[vec_key]['DNA ID']
        dna_key = hash_map[dna_name]
        vec_name = vector_dict[vec_key]['Vector Name']
        flapjack_vector_id = fj.create('vector', name=vec_name, dnas=dna_key)
        hash_map[key] = flapjack_vector_id.id[0]

    # strain_df = xls.parse('Strain', skiprows=18, index_col='Strain ID')
    # # strain_id = strain_df.to_dict('records')
    # strain_dict = strain_df.to_dict('index')

    # for id in strain_dict:
    #     name = strain_dict[id]['Strain Name']
    #     flapjack_id = fj.create(chemical_dict[id]['Chemical Name'], chemical_dict[id]['Chemical Description'])
    #     hash_map[id] = flapjack_id

    for key in strain_dict:
        flapjack_strain_id = fj.create('strain', name=strain_dict[key]['Strain Name'], description=strain_dict[key]['Strain Description'])
        hash_map[key] = flapjack_strain_id.id[0]

    media_df = xls.parse('Media', skiprows=10, index_col='Media ID')
    # media_id = media_df.to_dict('records')
    media_dict = media_df.to_dict('index')



    for key in media_dict:
        flapjack_media_id = fj.create('media', name=media_dict[key]['Media Name'], description=media_dict[key]['Media Description'])
        hash_map[key] = flapjack_media_id.id[0]
        # print(hash_map)

    signal_df = xls.parse('Signal', skiprows=10, index_col='Signal ID')
    # signal_id = signal_df.to_dict('records')
    signal_dict = signal_df.to_dict('index')

    for id in signal_dict:
        name = signal_dict[id]['Signal Name']
        flapjack_id = fj.create(chemical_dict[id]['Chemical Name'], chemical_dict[id]['Chemical Description'])
        hash_map[id] = flapjack_id

    for key in signal_dict:
        flapjack_signal_id = fj.create('signal', name=signal_dict[key]['Signal Name'], description=signal_dict[key]['SignalDescription'], color=signal_dict[key]['Signal Color'])
        hash_map[key] = flapjack_signal_id.id[0]
        #print(hash_map)


    #Place keys and matched flapjack_ids for Signal, Media, Supplement and Chemical into
    #one output file 'Media Designs'

    #Place keys and matched flapjack_ids for Strain, Vector, and DNAs into
    #one output file 'Sample Designs'