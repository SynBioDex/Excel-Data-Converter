from abc import ABC, abstractmethod


class media(flapjack_object):
    def __init__(self, is_owner, name, description, role, sbol_object_type):
        self.is_owner = is_owner
        self.name = name
        self.description = description
        self.role = role
        self.sbol_object_type = sbol_object_type

    def get_is_owner(self):
        return self.is_owner

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_role(self):
        return self.role

    def get_sbol_object_type(self):
        return self.sbol_object_type

    def set_is_owner(self, is_owner):
        self.is_owner = is_owner

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_role(self, role):
        self.role = role

    def set_sbol_object_type(self, sbol_object_type):
        self.sbol_object_type = sbol_object_type