from abc import ABC, abstractmethod


class chemical(flapjack_object):
    def __init__(self, name, description, pubchem_id, molecule_type):
        self.name = name
        self.description = description
        self.pubchem_id = pubchem_id
        self.molecule_type = molecule_type

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_pubchem_id(self):
        return self.pubchem_id

    def get_molecule_type(self):
        return self.molecule_type

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_pubchem_id(self, pubchem_id):
        self.pubchem_id = pubchem_id

    def set_molecule_type(self, molecule_type):
        self.molecule_type = molecule_type