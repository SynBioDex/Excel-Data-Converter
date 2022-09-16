from abc import ABC, abstractmethod

class sample(flapjack_object):
    def __init__(self, row, column, assay_id, sample_design_id, sbol_object_type):
        self.row = row
        self.column = column
        self.assay_id = assay_id
        self.sample_design_id = sample_design_id
        self.sbol_object_type = sbol_object_type

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_assay_id(self):
        return self.assay_id

    def get_sample_design_id(self):
        return self.sample_design_id

    def get_sbol_object_type(self):
        return self.sbol_object_type

    def set_row(self, row):
        self.row = row

    def set_column(self, column):
        self.column = column

    def set_assay_id(self, assay_id):
            self.assay_id = assay_id

    def set_sample_design_id(self, sample_design_id):
        self.sample_design_id = sample_design_id

    def set_sbol_object_type(self, sbol_object_type):
        self.sbol_object_type = sbol_object_type