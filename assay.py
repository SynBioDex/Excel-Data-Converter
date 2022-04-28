from abc import ABC, abstractmethod

class assay(flapjack_object):
    def __init__(self, name, machine, description, temperature, study_id, sbol_object_type):
        self.name = name
        self.machine = machine
        self.description = description
        self.temperature = temperature
        self.study_id = study_id
        self.sbol_object_type = sbol_object_type

    def get_name(self):
        return self.name

    def get_machine(self):
        return self.machine

    def get_description(self):
        return self.description

    def get_temperature(self):
        return self.temperature

    def get_study_id(self):
        return self.study_id

    def get_sbol_object_type(self):
        return self.sbol_object_type

    def set_name(self, name):
        self.name = name

    def set_machine(self, machine):
        self.machine = machine

    def set_description(self, description):
            self.description = description

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_study_id(self, study_id):
        self.study_id = study_id

    def set_sbol_object_type(self, sbol_object_type):
        self.sbol_object_type = sbol_object_type