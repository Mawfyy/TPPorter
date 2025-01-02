import argparse
import os

parser = argparse.ArgumentParser(description="Portea tus iconos de high a medium")
parser.add_argument("folder_path", help="Ruta de la carpeta donde estan los archivos .png")
args = parser.parse_args()

print(f"Porteando....")

def port(folder_path):
    png_files = get_png_files(folder_path)

def get_png_files(folder_path):
    files = []
    for filename in os.listdir(folder_path):
        if "uhd.png" in filename or "uhd.plist" in filename:
            files.append(filename)
    return files

port(args.folder_path)