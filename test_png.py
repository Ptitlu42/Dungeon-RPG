from PIL import Image
import os
import Constant as cst

dir_path = 'sprites/floor'

for filename in os.listdir(dir_path):
    if filename.endswith('.png'):
        file_path = os.path.join(dir_path, filename)
        try:
            with Image.open(file_path) as img:
                img.verify()
                print(f'{img} : Verified')
        except Exception as e:
            print(f"Erreur dans le fichier {file_path}: {e}")