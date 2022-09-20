import os
import excel2flapjack.main as e2f

fj_url = "localhost:8000"
fj_username = "saisam17"
fj_pass = "Flap123"

direct = __file__
test_file_path = os.path.join(os.path.split(os.path.split(direct)[0])[0],
                              'tests', 'test_files')
excel_path = os.path.join(test_file_path, "flapjack_excel_converter_v028.xlsx")

hash_map = e2f.flapjack_upload(fj_url, fj_username, fj_pass, excel_path)
print(hash_map)
