from abc import ABC, abstractmethod

class supplement(flapjack_object):
    def __init__(self, sample_id, is_owner, chemical_id, name, concentration, sbol_object_type):
        self.sample_id = sample_id
        self.is_owner = is_owner
        self.chemical_id = chemical_id
        self.name = name
        self.concentration = concentration
        self.sbol_object_type = sbol_object_type

    def get_sample_id(self):
        return self.sample_id

    def get_is_owner(self):
        return self.is_owner

    def get_chemical_id(self):
        return self.chemical_id

    def get_name(self):
        return self.name

    def get_concentration(self):
        return self.concentration

    def get_sbol_object_type(self):
        return self.sbol_object_type

    def set_sample_id(self, sample_id):
        self.sample_id = sample_id

    def set_is_owner(self, is_owner):
        self.is_owner = is_owner

    def set_chemical_id(self, chemical_id):
        self.chemical_id = chemical_id

    def set_name(self, name):
        self.name = name

    def set_concentration(self, concentration):
            self.concentration = concentration

    def set_sbol_object_type(self, sbol_object_type):
        self.sbol_object_type = sbol_object_type