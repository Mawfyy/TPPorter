import re
import plistlib
import yaml
import os, sys
import cv2
import argparse
from math import floor
from math import ceil	

def divideLowFloor(value):
    return "{" + str(floor(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[0])/4)) +"," +str(floor(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[1])/4)) + "}"

def divideMediumFloor(value):
    return "{" + str(floor(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[0])/2)) +"," +str(floor(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[1])/2)) + "}"

def divideLowCeil(value):
    return "{" + str(ceil(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[0])/4)) +"," +str(ceil(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[1])/4)) + "}"

def divideMediumCeil(value):
    return "{" + str(ceil(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[0])/2)) +"," +str(ceil(int(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[1])/2)) + "}"

def divideFloatLow(value):
    return "{" + str((float(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[0])/4)) +"," +str((float(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[1])/4)) + "}"

def divideFloatMedium(value):
    return "{" + str((float(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[0])/2)) +"," +str((float(re.search("(?<={)(.*)(?=})",value).group(1).split(',')[1])/2)) + "}"

parser = argparse.ArgumentParser(description='A Texture Pack porter made by ItalianApkDownloader, forked by Weebify')
requiredNamed = parser.add_argument_group('Required named arguments')
requiredNamed.add_argument('-i', '--input', help='Input file name', required=True, nargs="+")
requiredNamed.add_argument('-o', '--output', help='Output file name', required=True, nargs="+")
args = parser.parse_args()


fileI = args.__dict__["input"]
fileO = args.__dict__["output"]

print("Files input: " + str(len(fileI)))
print("Getting there...")

if len(fileI) == len(fileO):

    for x in range(0,len(fileI)):

        filenameInput, file_extensionInput = os.path.splitext(fileI[x])
        filenameOutput, file_extensionOutput = os.path.splitext(fileO[x])

        if file_extensionInput == ".plist":
	
            if filenameInput[-3:] == "-hd":
                try:
                    with open(fileI[x], 'rb') as f:
                        plist_data = plistlib.load(f)
                except IndexError:
                    plist_file = '<stdin>'
                    plist_data = plistlib.loads(sys.stdin.buffer.read())
                    exit()
                
                print(plist_data)
                dictionary = plist_data.get("frames").items()
                for key in dictionary:
                    try:
                        value = key[1]["textureRect"]
                        key[1]["textureRect"] = "{{" + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[0])/2)) + "," + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[1])/2)) +"},{" + str(ceil(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[0])/2)) + "," + str(ceil(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[1])/2)) + "}}"
                        if  key[1]["spriteOffset"] != '' :
                            key[1]["spriteOffset"] = divideFloatMedium(key[1]["spriteOffset"])
                        if  key[1]["spriteSize"] != '':
                            key[1]["spriteSize"] = divideMediumFloor(key[1]["spriteSize"])
                        if  key[1]["spriteSourceSize"] != '':
                            key[1]["spriteSourceSize"] = divideMediumFloor(key[1]["spriteSourceSize"])
                    except Exception as e:
                        print(e)
                        print(key)

                plist_data["metadata"]["size"] = divideMediumCeil(plist_data["metadata"]["size"])
                plist_data["metadata"]["realTextureFileName"] = plist_data["metadata"]["realTextureFileName"].replace("-hd","")
                plist_data["metadata"]["textureFileName"] = plist_data["metadata"]["textureFileName"].replace("-hd","")


                f = open(fileO[x], 'wb')

                plistlib.dump(plist_data,f)
                print("Done!(" + str((x+1)) + "/" + str(len(fileI)) + ")")
        
            elif filenameInput[-3:] == "uhd" and filenameOutput[-2:] != "hd":
                try:
                    with open(fileI[x], 'rb') as f:
                        plist_data = plistlib.load(f)
                except IndexError:
                    plist_file = '<stdin>'
                    plist_data = plistlib.loads(sys.stdin.buffer.read())
                    exit()

                dictionary = plist_data.get("frames").items()
                for key in dictionary:
                    try:
                        value = key[1]["textureRect"]
                        key[1]["textureRect"] = "{{" + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[0])/4)) + "," + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[1])/4)) +"},{" + str(ceil(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[0])/4)) + "," + str(ceil(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[1])/4)) + "}}"
                        if  key[1]["spriteOffset"] != '' :
                            key[1]["spriteOffset"] = divideFloatLow(key[1]["spriteOffset"])
                        if  key[1]["spriteSize"] != '':
                            key[1]["spriteSize"] = divideLowFloor(key[1]["spriteSize"])
                        if  key[1]["spriteSourceSize"] != '':
                            key[1]["spriteSourceSize"] = divideLowFloor(key[1]["spriteSourceSize"])
                    except Exception as e:
                        print(e)
                        print(key)

                plist_data["metadata"]["size"] = divideLowCeil(plist_data["metadata"]["size"])
                plist_data["metadata"]["realTextureFileName"] = plist_data["metadata"]["realTextureFileName"].replace("-uhd","")
                plist_data["metadata"]["textureFileName"] = plist_data["metadata"]["textureFileName"].replace("-uhd","")


                f = open(fileO[x], 'wb')

                plistlib.dump(plist_data,f)
                print("Done!(" + str((x+1)) + "/" + str(len(fileI)) + ")")
        
            elif filenameInput[-3:] == "uhd" and filenameOutput[-2:] == "hd":
                try:
                    with open(fileI[x], 'rb') as f:
                        plist_data = plistlib.load(f)
                except IndexError:
                    plist_file = '<stdin>'
                    plist_data = plistlib.loads(sys.stdin.buffer.read())
                    exit()

                dictionary = plist_data.get("frames").items()
                for key in dictionary:
                    try:
                        value = key[1]["textureRect"]
                        key[1]["textureRect"] = "{{" + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[0])/2)) + "," + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[1])/2)) +"},{" + str(ceil(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[0])/2)) + "," + str(ceil(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[1])/2)) + "}}"
                        if  key[1]["spriteOffset"] != '' :
                            key[1]["spriteOffset"] = divideFloatMedium(key[1]["spriteOffset"])
                        if  key[1]["spriteSize"] != '':
                            key[1]["spriteSize"] = divideMediumFloor(key[1]["spriteSize"])
                        if  key[1]["spriteSourceSize"] != '':
                            key[1]["spriteSourceSize"] = divideMediumFloor(key[1]["spriteSourceSize"])
                    except Exception as e:
                        print(e)
                        print(key)

                plist_data["metadata"]["size"] = divideMediumCeil(plist_data["metadata"]["size"])
                plist_data["metadata"]["realTextureFileName"] = plist_data["metadata"]["realTextureFileName"].replace("uhd","hd")
                plist_data["metadata"]["textureFileName"] = plist_data["metadata"]["textureFileName"].replace("uhd","hd")


                f = open(fileO[x], 'wb')

                plistlib.dump(plist_data,f)
                print("Done!(" + str((x+1)) + "/" + str(len(fileI)) + ")")
                
            else:
            	print("Invalid file! Your input file should be in either high, medium graphic and have the correct name from the resource folder.")

        elif file_extensionInput == ".png":
	
            if filenameInput[-3:] == "uhd" and filenameOutput[-2:] != "hd":
                im = cv2.imread(filenameInput+".png",cv2.IMREAD_UNCHANGED)

                width = ceil(im.shape[1] / 4 )
                height = ceil(im.shape[0] / 4 )
                dim = (width, height)
                resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

                cv2.imwrite(filenameOutput + ".png",resized)
                print("Done!(" + str((x+1)) + "/" + str(len(fileI)) + ")")
        
            elif filenameInput[-3:] == "uhd" and filenameOutput[-2:] == "hd":
                im = cv2.imread(filenameInput+".png",cv2.IMREAD_UNCHANGED)

                width =  ceil(im.shape[1] / 2 )
                height = ceil(im.shape[0] / 2 )
                dim = (width, height)
                resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

                cv2.imwrite(filenameOutput + ".png",resized)
                print("Done!(" + str((x+1)) + "/" + str(len(fileI)) + ")")
        
            elif filenameInput[-3:] == "-hd":
                im = cv2.imread(filenameInput+".png",cv2.IMREAD_UNCHANGED)

                width = ceil(im.shape[1] / 2 )
                height = ceil(im.shape[0] / 2 )
                dim = (width, height)
                resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

                cv2.imwrite(filenameOutput + ".png",resized)
                print("Done!(" + str((x+1)) + "/" + str(len(fileI)) + ")")
        
            else:
            	print("Invalid file! Your input file should be in either high, medium graphic and have the correct name in the resource folder.")

        else:
            print("Invalid file! Your input file should be an either .plist or .png file.")

    print("Porting finished ")

else:
	print ("Invalid! The number of input and output files should be the same.")
    
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    