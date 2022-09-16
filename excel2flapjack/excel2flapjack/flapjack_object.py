from abc import ABC, abstractmethod

class flapjack_object(ABC):
    @abstractmethod
    def __init__(self, main_id, type_id, type):
        self.main_id = main_id
        self.type_id = type_id
        self.type = type

    @property
    def get_main_id(self):
        return self.main_id

    @property
    def get_type_id(self):
        return self.type_id

    @property
    def get_type(self):
        return self.type

    @get_main_id.setter
    def set_main_id(self, main_id):
        self.main_id = main_id

    @get_type_id.setter
    def set_type_id(self, type_id):
        self.type_id  = type_id

    @get_type.setter
    def set_type(self, type):
        self.type = type


