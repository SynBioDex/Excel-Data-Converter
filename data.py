import csv
import sys
import numpy as np
import pandas as pd
import argparse as argp
import configparser as conp
from flapjack import Flapjack

fj = Flapjack(url_base='local-host:8000')
fj.log_in(username=saisam17, password=Flap123)

xls = pd.ExcelFile(r"/tests/test_files/test_version7_flapjack_compiler_sbol3_v0022.xlsx")

#read in skip rows from init sheet 

dna_df = xls.parse('DNAs', skiprows=18)
dna_id = dna_df.to_dict('records')
#print(dna_id[0])
#print(dna_id[0].keys())

chemical_df = xls.parse('Chemical', skiprows=18)
chemical_id = chemical_df.to_dict('records')
print (chemical_df)
#print(chemical_id[1])
#print(chemical_id[0].keys())

for x in chemical_df.chemical_id:
    flapjack_post_chemical_name_request(x)
    #chemical = fj.create('chemical', name=x., description='This is a test')

#{'Chemical ID': 'Chemical2', 'Chemical Owner': True, 'Chemical Name': 'ATC', 'Chemical Description': 'ChemicalB', 'Pubchem ID': 'ID1', 'SBOL Object Type': 'ComponentDefinition', 'Molecule Type': 'SmallMolecule'}
#dict_keys(['Chemical ID', 'Chemical Owner', 'Chemical Name', 'Chemical Description', 'Pubchem ID', 'SBOL Object Type', 'Molecule Type'])

signal_df = xls.parse('Signal', skiprows=10)
signal_id = signal_df.to_dict('records')
#print(signal_id[1])
#print(signal_id[0].keys())

#add flapjack dna id from post request to vector dictionary
vector_df = xls.parse('Vector', skiprows=18)
vector_id = vector_df.to_dict('records')
#print(vector_id[0])
#print(vector_id[0].keys())

#add flapjack chemical id from post request to supplement dictionary
supplement_df = xls.parse('Supplement', skiprows=18)
supplement_id = supplement_df.to_dict('records')
#print(supplement_id[0])
#print(supplement_id[0].keys())

strain_df = xls.parse('Strain', skiprows=18)
strain_id = strain_df.to_dict('records')
#print(strain_id[0])
#print(strain_id[0].keys())

media_df = xls.parse('Media', skiprows=10)
media_id = media_df.to_dict('records')
#print(media_id[0])
#print(media_id[0].keys())

measurement_df = xls.parse('Measurement', skiprows=18)
measurement_id = measurement_df.to_dict('records')
#print(measurement_id[0])
#print(measurement_id[0].keys())

#add sample design

sample_df = xls.parse('Sample', skiprows=18)
sample_id = sample_df.to_dict('records')
#print(sample_id[0]['Study Name'])
#print(sample_id[0].keys())

assay_df = xls.parse('Assay', skiprows=18)
assay_id = assay_df.to_dict('records')
#print(assay_id[0])
#print(assay_id[0].keys())

study_df = xls.parse('Study', skiprows=18)
study_id = study_df.to_dict('records')
print(study_id[0])
print(study_id[0].keys())

#samples = df.iloc[1,1]
#put Sample Column ID from dataframe into list
#Create dictionary and upload all Sample Column IDs as keys into dictionary
#Use for loop to iterate over list of Sample IDs
#For each sample ID in list, send a post request with create sample endpoint
#Parse json for the returned sample flapjack ID
#Assign Sample Flapjack ID as value to the Sample Column ID Key
#Key: ID from the Spreadsheet (Chemical1, etc)
#Value: Flapjack ID (number)

# Replace the Keys with the Flapjack IDs
# Just use one map
# Only need one map because the keys are all unique

#print("\n1st column as a Set:\n")
#print(samples)

#signals = []

