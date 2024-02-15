import os
import pandas as pd
from flapjack import Flapjack

""" Questions:
    1. what is the hash_map used for?
        - it says "for linking to chemicals" but linking what to chemicals?

"""



# class definition
class inputData:

    """ 
        inputData retrives information from input XDC excel template, connects to fj, and formats and uploads data
        includes: 
            - class definition
            - initialization method
            - class attributes
            - instance attributes
            - methods
        

        Instance Attributes
        ----------
        xls : pandas unparsed ExcelFile class
            gotten using xls = pd.ExcelFile(excel_path)

        fj : flapjack.flapjack.Flapjack object
            fj case that contains the connection to specific fj account

        xdc_data : pd.DataFrame
            df containing all the information from the excel sheet
    """
    # list of all the sheet names in XDC excel file
    # each will define an fj object with data extracted from the excel sheet
    # use self.types to access this class attribute
    types = ['Chemical', 'DNA', 'Supplement', 'Vector', 'Strain', 'Media',
            'Signal', 'Study', 'Assay', 'Sample', 'Measurement', 'Sample Design']


    def __init__(self, 
                 xls, 
                 fj_url, 
                 fj_user, 
                 fj_pass):
        self.xls = xls
        # fj url has to include 8000 port
        if not fj_url.endswith(":8000"):
            fj_url = fj_url + ":8000"

        self.fj = Flapjack(url_base=fj_url)
        self.fj.log_in(username = fj_user, password = fj_pass)
        self.xdc_data = pd.DataFrame()


    def create_df(self):
        # parse FlapjackCols sheet from XDC fil
        fj_conv_sht = self.xls.parse('FlapjackCols', skiprows=0)

        for obj in self.types:
            # read in the conversion sheet for xdc col name to flapjack name 
                # for current obj
            fj_conv_sht_obj = fj_conv_sht.loc[(fj_conv_sht['Sheet Name'] == obj)]
            fj_conv_sht_obj = fj_conv_sht_obj.set_index('ColName').to_dict('index')

            # read in current obj sheet
            obj_df = self.xls.parse(obj, skiprows=0, index_col=f'{obj} ID')
            cols = list(obj_df.columns)

            # drop cols not used by fj and rename ones that are
            new_cols = []
            drop_cols = []
            for col in cols:
                if col in fj_conv_sht_obj.keys():
                    new_cols.append(fj_conv_sht_obj[col]['FlapjackName'])
                else:
                    drop_cols.append(col)
            
            obj_df = obj_df.drop(columns=drop_cols)
            obj_df.columns = new_cols
            obj_df['object'] = obj
            obj_df['flapjackid'] = ''

            self.xdc_data = self.xdc_data.append(obj_df)



# will use self.fj.create to create and upload data as fj objects in create_Type methods


