import os
import excel2flapjack.main as e2f


fj_url = "localhost:8000" #local
#fj_url = "flapjack.rudge-lab.org:8000" #Web Instance Rudge Lab
#fj_url = "198.59.83.73:8000" #Web Instance Genetic Logic Lab
fj_user = "Gonza10V"
fj_pass = "010101"

direct = __file__
test_file_path = os.path.join(os.path.split(os.path.split(direct)[0])[0],
                              'tests', 'test_files')
excel_path = os.path.join(test_file_path, "flapjack_excel_converter_v030.xlsx")

hash_map = e2f.flapjack_upload(fj_url, fj_user, fj_pass, excel_path, sbol_hash_map={},
                    add_sbol_uris=False, flapjack_override=True, print_progress=True)
print(hash_map)