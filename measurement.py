from abc import ABC, abstractmethod

class measurement(flapjack_object):
    def __init__(self, sample_id, signal, time, value):
        self.row = row
        self.column = column
        self.sample_id = sample_id
        self.sample_design_id = sample_design_id
        self.sbol_object_type = sbol_object_type

    def get_sample_id(self):
        return self.sample_id

    def get_signal(self):
        return self.signal

    def get_time(self):
        return self.time

    def get_value(self):
        return self.value

    def set_sample_id(self, sample_id):
            self.sample_id = sample_id

    def set_signal(self, signal):
        self.signal = signal

    def set_time(self, time):
        self.time = time

    def set_value(self, value):
        self.value = value