import csv
import sys
import numpy as np
import pandas as pd
import argparse as argp
import configparser as conp
from flapjack import Flapjack
import getpass

hash_map = {}

#fj = Flapjack('flapjack.rudge-lab.org:8000') #Web Instance
fj = Flapjack(url_base='localhost:8000') #Local Instance
fj.log_in(username="saisam17", password="Flap123")

xls = pd.ExcelFile(r"C:\Users\saisa\FlapjackUploadMeasurements\tests\test_files\test_version7_flapjack_compiler_sbol3_v0022.xlsx")

chemical_df = xls.parse('Chemical', skiprows=18, index_col='Chemical ID')
chemical_id = chemical_df.to_dict('records')
chemical_dict = chemical_df.to_dict('index')

def create_flapjack_chemical(key):
    return fj.create('chemical', name=chemical_dict[key]['Chemical Name'], description=chemical_dict[key]['Chemical Description'])#, pubchemid=chemical_dict[id]['Pubchem ID'])

#chemical_df = pd.read_excel(r"C:\Users\saisa\FlapjackUploadMeasurements\tests\test_files\test_version7_flapjack_compiler_sbol3_v0022.xlsx",
     #sheet_name="Chemical",
     #skiprows=18, engine='openpyxl')
#chemical_dict = chemical_df.to_dict('index')
#print(chemical_dict)

def get_flapjack(id):
    return fj.create(chemical_dict[id]['Chemical Name'], chemical_dict[id]['Chemical Description'])

for id in chemical_dict:
    name = chemical_dict[id]['Chemical Name']
    print(name)
    flapjack_id = get_flapjack(id)
    hash_map[id] = flapjack_id
    #print(hash_map)

for key in chemical_dict:
    flapjack_chemical_id = create_flapjack_chemical(key) #.id[0]
    hash_map[key] = flapjack_chemical_id.id[0]
    # print(hash_map)

supplement_df = xls.parse('Supplement', skiprows=18, index_col='Supplement ID')
supplement_id = supplement_df.to_dict('records')
supplement_dict = supplement_df.to_dict('index')

def create_flapjack_supplement(supplement_key, chemical_key):
    sup_name = supplement_dict[supplement_key]['Supplement Name']
    sup_conc = supplement_dict[supplement_key]['Concentration']
    return fj.create('supplement', name=sup_name, chemical=chemical_key, concentration=sup_conc)#, pubchemid=chemical_dict[id]['Pubchem ID'])

for key in supplement_dict:
    chemical_name = supplement_dict[key]['Chemical ID']
    chemical_key = hash_map[chemical_name]
    flapjack_supplement_id = create_flapjack_supplement(key, chemical_key) #.id[0]
    hash_map[key] = flapjack_supplement_id.id[0]

print(hash_map)

#print(hash_map)

#dna_df = xls.parse('DNAs', skiprows=18)
#dna_id = dna_df.to_dict('records')
#dna_dict = dna_df.to_dict('index')

#def create_flapjack_dna(dna_key):
    #dna_name = dna_dict[dna_key]['DNA Name']
    #return fj.create('dna', name=dna_name)

#for key in dna_dict:
    #flapjack_dna_id = create_flapjack_dna(key) #.id[0]
    #hash_map[key] = flapjack_dna_id.id[0]

vector_df = xls.parse('Vector', skiprows=18, index_col='Vector ID')
vector_id = vector_df.to_dict('records')
vector_dict = vector_df.to_dict('index')

def create_flapjack_vector(vector_key, dna_key):
    vec_name = vector_dict[vector_key]['Vector Name']
    return fj.create('vector', name=vec_name, dnas=dna_key)

for key in vector_dict:
    dna_name = vector_dict[key]['DNA ID']
    dna_key = hash_map[dna_name]
    flapjack_vector_id = create_flapjack_vector(key, dna_key)
    hash_map[key] = flapjack_vector_id.id[0]

#print(hash_map)

strain_df = xls.parse('Strain', skiprows=18, index_col='Strain ID')
strain_id = strain_df.to_dict('records')
strain_dict = strain_df.to_dict('index')

def create_flapjack_strain(key):
    return fj.create('strain', name=strain_dict[key]['Strain Name'], description=strain_dict[key]['Strain Description'])

for id in strain_dict:
    name = strain_dict[id]['Strain Name']
    flapjack_id = get_flapjack(id)
    hash_map[id] = flapjack_id
    #print(hash_map)

for key in strain_dict:
    flapjack_strain_id = create_flapjack_strain(key)
    hash_map[key] = flapjack_strain_id.id[0]
    # print(hash_map)

media_df = xls.parse('Media', skiprows=10, index_col='Media ID')
media_id = media_df.to_dict('records')
media_dict = media_df.to_dict('index')

def create_flapjack_media(key):
    return fj.create('media', name=media_dict[key]['Media Name'], description=media_dict[key]['Media Description'])

for id in media_dict:
    name = media_dict[id]['Media Name']
    flapjack_id = get_flapjack(id)
    hash_map[id] = flapjack_id
    #print(hash_map)

for key in media_dict:
    flapjack_media_id = create_flapjack_media(key)
    hash_map[key] = flapjack_media_id.id[0]
    # print(hash_map)

signal_df = xls.parse('Signal', skiprows=10, index_col='Signal ID')
signal_id = signal_df.to_dict('records')
signal_dict = signal_df.to_dict('index')

def create_flapjack_media(key):
    return fj.create('signal', name=signal_dict[key]['Signal Name'], description=signal_dict[key]['SignalDescription'], color=signal_dict[key]['Signal Color'])

for id in signal_dict:
    name = signal_dict[id]['Signal Name']
    flapjack_id = get_flapjack(id)
    hash_map[id] = flapjack_id
    #print(hash_map)

for key in signal_dict:
    flapjack_signal_id = create_flapjack_signal(key)
    hash_map[key] = flapjack_signal_id.id[0]
    #print(hash_map)

signal_df = xls.parse('Signal', skiprows=10, index_col='Signal ID')
signal_id = signal_df.to_dict('records')
signal_dict = signal_df.to_dict('index')

def create_flapjack_media(key):
    return fj.create('signal', name=signal_dict[key]['Signal Name'], description=signal_dict[key]['SignalDescription'], color=signal_dict[key]['Signal Color'])

for id in signal_dict:
    name = signal_dict[id]['Signal Name']
    flapjack_id = get_flapjack(id)
    hash_map[id] = flapjack_id
    #print(hash_map)

for key in signal_dict:
    flapjack_signal_id = create_flapjack_signal(key)
    hash_map[key] = flapjack_signal_id.id[0]
    print(hash_map)
#Place keys and matched flapjack_ids for Signal, Media, Supplement and Chemical into
#one output file 'Media Designs'

#Place keys and matched flapjack_ids for Strain, Vector, and DNAs into
#one output file 'Sample Designs'