from flapjack_object import flapjack_object

class signal(flapjack_object):
    def __init__(self, is_owner, name, description, color, molecule_type, sbol_object_type):
        self.is_owner = is_owner
        self.name = name
        self.description = description
        self.color = color
        self.molecule_type = molecule_type
        self.sbol_object_type = sbol_object_type

    def get_is_owner(self):
        return self.is_owner
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_color(self):
        return self.color

    def get_molecule_type(self):
        return self.molecule_type

    def get_sbol_object_type(self):
        return self.sbol_object_type

    def set_is_owner(self, is_owner):
        self.is_owner = is_owner
        
    def set_name(self, name):
        self.name = name

    def set_description(self, description):
            self.description = description

    def set_color(self, color):
        self.color = color

    def set_molecule_type(self, molecule_type):
        self.molecule_type = molecule_type

    def set_sbol_object_type(self, sbol_object_type):
        self.sbol_object_type = sbol_object_type