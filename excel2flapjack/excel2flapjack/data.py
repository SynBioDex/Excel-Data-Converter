import pandas as pd

class Data:
    def __init__(self, data_file_name):
        self._hashmap = {}
        self._xls = pd.ExcelFile(data_file_name) #validation
        self._dna_df_dict = self._xls.parse('DNAs', skiprows=18).to_dict('index')
        self._chemical_df_dict = self._xls.parse('Chemical', skiprows=18).to_dict('index')
        self._signal_df_dict = self._xls.parse('Signal', skiprows=10).to_dict('index')
        self._vector_df_dict = self._xls.parse('Vector', skiprows=18).to_dict('index')
        self._supplement_df_dict = self._xls.parse('Supplement', skiprows=18).to_dict('index')
        self._strain_df_dict = self._xls.parse('Strain', skiprows=18).to_dict('index')
        self._media_df_dict = self._xls.parse('Media', skiprows=10).to_dict('index')
        self._measurement_df_dict = self._xls.parse('Measurement', skiprows=18).to_dict('index')
        self._sample_df_dict = self._xls.parse('Sample', skiprows=18).to_dict('index')
        self._assay_df_dict = self._xls.parse('Assay', skiprows=18).to_dict('index')
        self._study_df_dict = self._xls.parse('Study', skiprows=18).to_dict('index')

    @property
    def dna_df_dict(self):
        return self._dna_df_dict

    @dna_df_dict.setter
    def dna_df_dict(self, dna_dict):
        self._dna_df_dict = dna_dict

    @property
    def chemical_df_dict(self):
        return self._chemical_df_dict

    @chemical_df_dict.setter
    def chemical_df_dict(self, chemical_dict):
        self._chemical_df_dict = chemical_dict

    @property
    def signal_df_dict(self):
        return self._signal_df_dict

    @signal_df_dict.setter
    def signal_df_dict(self, signal_dict):
        self._signal_df_dict = signal_dict

    @property
    def vector_df_dict(self):
        return self._vector_df_dict

    @vector_df_dict.setter
    def vector_df_dict(self, vector_dict):
        self._vector_df_dict = vector_dict

    @property
    def supplement_df_dict(self):
        return self._supplement_df_dict

    @supplement_df_dict.setter
    def supplement_df_dict(self, supplement_dict):
        self._supplement_df_dict = supplement_dict

    @property
    def strain_df_dict(self):
        return self._strain_df_dict

    @strain_df_dict.setter
    def strain_df_dict(self, strain_dict):
        self._strain_df_dict = strain_dict

    @property
    def media_df_dict(self):
        return self._media_df_dict

    @media_df_dict.setter
    def media_df_dict(self, media_dict):
        self._media_df_dict = media_dict

    @property
    def measurement_df_dict(self):
        return self._measurement_df_dict

    @measurement_df_dict.setter
    def measurement_df_dict(self, measurement_dict):
        self._measurement_df_dict = measurement_dict

    @property
    def sample_df_dict(self):
        return self._sample_df_dict

    @sample_df_dict.setter
    def sample_df_dict(self, sample_dict):
        self._sample_df_dict = sample_dict

    @property
    def assay_df_dict(self):
        return self._assay_df_dict

    @assay_df_dict.setter
    def assay_df_dict(self, assay_dict):
        self._assay_df_dict = assay_dict

    @property
    def study_df_dict(self):
        return self._study_df_dict

    @study_df_dict.setter
    def study_df_dict(self, study_dict):
        self._study_df_dict = study_dict

    def create_flapjack_dna(self, fj):
       # print(self._dna_df_dict)
        for key in self._dna_df_dict.values():
            dna_name = key['DNA Name']
            flapjack_dna_id = fj.create('dna', name=dna_name)
            self._hashmap[dna_name] = flapjack_dna_id.id[0]
        return self._hashmap