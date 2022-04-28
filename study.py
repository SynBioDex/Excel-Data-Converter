from abc import ABC, abstractmethod

class study(flapjack_object):
    def __init__(self, name, description, doi, is_owner, is_public, sbol_object_type):
        self.name = name
        self.description = description
        self.doi = doi
        self.is_owner = is_owner
        self.is_public = is_public
        self.sbol_object_type = sbol_object_type

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_doi(self):
        return self.doi

    def get_is_owner(self):
        return self.is_owner

    def get_is_public(self):
        return self.is_public

    def get_sbol_object_type(self):
        return self.sbol_object_type

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
            self.description = description

    def set_doi(self, doi):
        self.doi = doi

    def set_is_owner(self, is_owner):
        self.is_owner = is_owner

    def set_is_public(self, is_public):
        self.is_public = is_public

    def set_sbol_object_type(self, sbol_object_type):
        self.sbol_object_type = sbol_object_type