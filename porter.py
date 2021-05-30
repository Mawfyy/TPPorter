import re
import plistlib
import os, sys
import cv2
import argparse
from math import floor, ceil
from os.path import isfile, join


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
parser.add_argument('-l', '--low', help='Optional argument. Use if you want to port your tp to low graphics', action='store_true')
args = parser.parse_args()


directory = os.path.dirname(os.path.realpath(__file__))
fileI = [f for f in os.listdir(directory) if isfile(join(directory, f))]


removal= []
for w in range(0,len(fileI)):
    filenameInput, file_extensionInput = os.path.splitext(fileI[w])
    
    if file_extensionInput != ".plist" and file_extensionInput != ".png" and file_extensionInput != ".fnt":
        removal.append(w)

removal.reverse()

for w in removal:
    fileI.pop(w)


print("Files input:%s(not including invalid files)" % str(len(fileI)))
print("Getting there...")

if True:
    for w in range(0,len(fileI)):

        filenameInput, file_extensionInput = os.path.splitext(fileI[w])
        
        if file_extensionInput == ".plist":
            try:
                with open(fileI[w], 'rb') as f:
                    plist_data = plistlib.load(f)
            except IndexError:
                plist_file = '<stdin>'
                plist_data = plistlib.loads(sys.stdin.buffer.read())
                exit()
            
            dictionary = plist_data.get("frames").items()
            
            if filenameInput[-3:] == "-hd":
                
                for key in dictionary:
                    try:
                        value = key[1]["textureRect"]
                        key[1]["textureRect"] = "{{" + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[0])/2)) + "," + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[1])/2)) +"},{" + str(floor(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[0])/2)) + "," + str(floor(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[1])/2)) + "}}"
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
                
                
                f = open(plist_data["metadata"]["textureFileName"].replace(".png",".plist"), 'wb')
                
                plistlib.dump(plist_data,f)
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
                
            elif filenameInput[-3:] == "uhd" and args.low:
                
                for key in dictionary:
                    try:
                        value = key[1]["textureRect"]
                        key[1]["textureRect"] = "{{" + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[0])/4)) + "," + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[1])/4)) +"},{" + str(floor(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[0])/4)) + "," + str(floor(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[1])/4)) + "}}"
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
                
                
                f = open(plist_data["metadata"]["textureFileName"].replace(".png",".plist"), 'wb')
                
                plistlib.dump(plist_data,f)
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
                
            elif filenameInput[-3:] == "uhd" and (not args.low):
                
                for key in dictionary:
                    try:
                        value = key[1]["textureRect"]
                        key[1]["textureRect"] = "{{" + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[0])/2)) + "," + str(ceil(int(re.search("(?<={{)(.*)(?=},)",value).group(1).split(',')[1])/2)) +"},{" + str(floor(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[0])/2)) + "," + str(floor(int(re.search("(?<=,{)(.*)(?=}})",value).group(1).split(',')[1])/2)) + "}}"
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
                
                
                f = open(plist_data["metadata"]["textureFileName"].replace(".png",".plist"), 'wb')
                
                plistlib.dump(plist_data,f)
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")                
                
            else:
                print("Invalid file(" + fileI[w] + ")! Your input file must be in either high, medium graphic and have the correct name from the resource folder.")
                
        elif file_extensionInput == ".fnt":
            with open(fileI[w]) as f:
                file=f.read()
            
            fnt_data=dict()
            
            fnt_data["info"]= re.search(r'info face=(?P<face>[\s\w"-]+) size=(?P<size>\w+) bold=(?P<bold>\w+) italic=(?P<italic>\w+) charset=(?P<charset>[\w"]+) unicode=(?P<unicode>\w+) stretchH=(?P<stretchH>\w+) smooth=(?P<smooth>\w+) aa=(?P<aa>\w+) padding=(?P<padding>[\w,-]+) spacing=(?P<spacing>[\w,-]+)', file).groupdict()
            fnt_data["common"]= re.search(r'common lineHeight=(?P<lineHeight>\w+) base=(?P<base>\w+) scaleW=(?P<scaleW>\w+) scaleH=(?P<scaleH>\w+) pages=(?P<pages>\w+) packed=(?P<packed>\w+)', file).groupdict()
            fnt_data["page"]= re.search(r'page id=(?P<id>\w+) file=(?P<file>[\w"-.]+)', file).groupdict()
            fnt_data["chars count"]= re.search('(?<=chars count=)(.*)(?=\nchar)', file).group()
            fnt_data["char"]=dict()
            
            f=open(fileI[w])
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            
            for xd in range(0,int(fnt_data["chars count"])):
                fCurrentLine=f.readline()
                fnt_data["char"]["char " + str(xd)]= re.search(r'char[ ]+id=(?P<id>\w+)[ ]+x=(?P<x>\w+)[ ]+y=(?P<y>\w+)[ ]+width=(?P<width>\w+)[ ]+height=(?P<height>\w+)[ ]+xoffset=(?P<xoffset>[\w-]+)[ ]+yoffset=(?P<yoffset>[\w-]+)[ ]+xadvance=(?P<xadvance>[\w-]+)[ ]+page=(?P<page>\w+)[ ]+chnl=(?P<chnl>\w+)', fCurrentLine).groupdict()
                
            fnt_data["kernings count"]= re.search('(?<=kernings count=)(.*)(?=\nkerning)', file).group()
            fnt_data["kerning"]=dict()
            
            f.readline()
            for xd in range(0,int(fnt_data["kernings count"])):
                fCurrentLine=f.readline()
                fnt_data["kerning"]["kerning " + str(xd)]= re.search(r'[ ]+first=(?P<first>\w+)[ ]+second=(?P<second>\w+)[ ]+amount=(?P<amount>[\w-]+)', fCurrentLine).groupdict()
            
            
            if filenameInput[-3:]=="-hd":
                
                fnt_data["info"]["size"]= str(ceil(int(fnt_data["info"]["size"]) / 2))
                fnt_data["common"]["lineHeight"]= str(ceil(int(fnt_data["common"]["lineHeight"])/2)+2)
                fnt_data["common"]["base"]= str(ceil(int(fnt_data["common"]["base"]) / 2))
                fnt_data["common"]["scaleW"]= str(ceil(int(fnt_data["common"]["scaleW"]) / 2))
                fnt_data["common"]["scaleH"]= str(ceil(int(fnt_data["common"]["scaleH"]) / 2))
                fnt_data["page"]["file"]=fnt_data["page"]["file"].replace("-hd", "")
                
                dictChar = fnt_data.get("char").items()
                dictKern = fnt_data.get("kerning").items()
                
                for key in dictChar:
                    key[1]["x"]=str(ceil(int(key[1]["x"])/2))
                    key[1]["y"]=str(ceil(int(key[1]["y"])/2))
                    key[1]["width"]=str(floor(int(key[1]["width"])/2))
                    key[1]["height"]=str(floor(int(key[1]["height"])/2))
                    key[1]["xoffset"]=str(ceil(int(key[1]["xoffset"])/2))
                    key[1]["yoffset"]=str(ceil(int(key[1]["yoffset"])/2))
                    key[1]["xadvance"]=str(ceil(int(key[1]["xadvance"])/2))
                for key in dictKern:
                    key[1]["amount"]=str(ceil(int(key[1]["amount"])/2))
                
                
                f.close()
                f = open(fnt_data["page"]["file"].replace('"',''),'wt')
                
                f.write('info face=%s size=%s bold=%s italic=%s charset=%s unicode=%s stretchH=%s smooth=%s aa=%s padding=%s spacing=%s' % (fnt_data["info"]["face"], fnt_data["info"]["size"], fnt_data["info"]["bold"], fnt_data["info"]["italic"], fnt_data["info"]["charset"], fnt_data["info"]["unicode"], fnt_data["info"]["stretchH"], fnt_data["info"]["smooth"], fnt_data["info"]["aa"], fnt_data["info"]["padding"], fnt_data["info"]["spacing"]))
                f.write('\ncommon lineHeight=%s base=%s scaleW=%s scaleH=%s pages=%s packed=%s' % (fnt_data["common"]["lineHeight"], fnt_data["common"]["base"], fnt_data["common"]["scaleW"], fnt_data["common"]["scaleH"], fnt_data["common"]["pages"], fnt_data["common"]["packed"]))
                f.write('\npage id=%s file=%s' % (fnt_data["page"]["id"], fnt_data["page"]["file"]))
                f.write('\nchars count=%s' % (fnt_data["chars count"]))
                for key in dictChar:
                    f.write('\nchar id=%s     x=%s   y=%s   width=%s   height=%s   xoffset=%s   yoffset=%s   xadvance=%s   page=%s   chnl=%s' % (key[1]["id"], key[1]["x"], key[1]["y"], key[1]["width"], key[1]["height"], key[1]["xoffset"], key[1]["yoffset"], key[1]["xadvance"], key[1]["page"], key[1]["chnl"]))
                f.write('\nkernings count=%s' % (fnt_data["kernings count"]))
                for key in dictKern:
                    f.write('\nkerning first=%s second=%s amount=%s' % (key[1]["first"], key[1]["second"], key[1]["amount"]))
                
                
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
                
            elif filenameInput[-3:]=="uhd" and (not args.low):
                
                fnt_data["info"]["size"]= str(ceil(int(fnt_data["info"]["size"]) / 2))
                fnt_data["common"]["lineHeight"]= str(ceil(int(fnt_data["common"]["lineHeight"])/2)+2)
                fnt_data["common"]["base"]= str(ceil(int(fnt_data["common"]["base"]) / 2))
                fnt_data["common"]["scaleW"]= str(ceil(int(fnt_data["common"]["scaleW"]) / 2))
                fnt_data["common"]["scaleH"]= str(ceil(int(fnt_data["common"]["scaleH"]) / 2))
                fnt_data["page"]["file"]=fnt_data["page"]["file"].replace("uhd", "hd")
                
                dictChar = fnt_data.get("char").items()
                dictKern = fnt_data.get("kerning").items()
                
                for key in dictChar:
                    key[1]["x"]=str(ceil(int(key[1]["x"])/2))
                    key[1]["y"]=str(ceil(int(key[1]["y"])/2))
                    key[1]["width"]=str(floor(int(key[1]["width"])/2))
                    key[1]["height"]=str(floor(int(key[1]["height"])/2))
                    key[1]["xoffset"]=str(ceil(int(key[1]["xoffset"])/2))
                    key[1]["yoffset"]=str(ceil(int(key[1]["yoffset"])/2))
                    key[1]["xadvance"]=str(ceil(int(key[1]["xadvance"])/2))
                for key in dictKern:
                    key[1]["amount"]=str(ceil(int(key[1]["amount"])/2))
            
            
                f.close()
                f = open(fnt_data["page"]["file"].replace('"',''),'wt')
            
                f.write('info face=%s size=%s bold=%s italic=%s charset=%s unicode=%s stretchH=%s smooth=%s aa=%s padding=%s spacing=%s' % (fnt_data["info"]["face"], fnt_data["info"]["size"], fnt_data["info"]["bold"], fnt_data["info"]["italic"], fnt_data["info"]["charset"], fnt_data["info"]["unicode"], fnt_data["info"]["stretchH"], fnt_data["info"]["smooth"], fnt_data["info"]["aa"], fnt_data["info"]["padding"], fnt_data["info"]["spacing"]))
                f.write('\ncommon lineHeight=%s base=%s scaleW=%s scaleH=%s pages=%s packed=%s' % (fnt_data["common"]["lineHeight"], fnt_data["common"]["base"], fnt_data["common"]["scaleW"], fnt_data["common"]["scaleH"], fnt_data["common"]["pages"], fnt_data["common"]["packed"]))
                f.write('\npage id=%s file=%s' % (fnt_data["page"]["id"], fnt_data["page"]["file"]))
                f.write('\nchars count=%s' % (fnt_data["chars count"]))
                for key in dictChar:
                    f.write('\nchar id=%s     x=%s   y=%s   width=%s   height=%s   xoffset=%s   yoffset=%s   xadvance=%s   page=%s   chnl=%s' % (key[1]["id"], key[1]["x"], key[1]["y"], key[1]["width"], key[1]["height"], key[1]["xoffset"], key[1]["yoffset"], key[1]["xadvance"], key[1]["page"], key[1]["chnl"]))
                f.write('\nkernings count=%s' % (fnt_data["kernings count"]))
                for key in dictKern:
                    f.write('\nkerning first=%s second=%s amount=%s' % (key[1]["first"], key[1]["second"], key[1]["amount"]))
                
                
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
                
            elif filenameInput[-3:]=="uhd" and args.low:
                fnt_data["info"]["size"]= str(ceil(int(fnt_data["info"]["size"]) / 4))
                fnt_data["common"]["lineHeight"]= str(ceil(int(fnt_data["common"]["lineHeight"])/4)+2)
                fnt_data["common"]["base"]= str(ceil(int(fnt_data["common"]["base"]) / 4))
                fnt_data["common"]["scaleW"]= str(ceil(int(fnt_data["common"]["scaleW"]) / 4))
                fnt_data["common"]["scaleH"]= str(ceil(int(fnt_data["common"]["scaleH"]) / 4))
                fnt_data["page"]["file"]=fnt_data["page"]["file"].replace("-hd", "")
                
                dictChar = fnt_data.get("char").items()
                dictKern = fnt_data.get("kerning").items()
                
                for key in dictChar:
                    key[1]["x"]=str(ceil(int(key[1]["x"])/4))
                    key[1]["y"]=str(ceil(int(key[1]["y"])/4))
                    key[1]["width"]=str(floor(int(key[1]["width"])/4))
                    key[1]["height"]=str(floor(int(key[1]["height"])/4))
                    key[1]["xoffset"]=str(ceil(int(key[1]["xoffset"])/4))
                    key[1]["yoffset"]=str(ceil(int(key[1]["yoffset"])/4))
                    key[1]["xadvance"]=str(ceil(int(key[1]["xadvance"])/2))
                for key in dictKern:
                    key[1]["amount"]=str(ceil(int(key[1]["amount"])/4))
            
            
                f.close()
                f = open(fnt_data["page"]["file"].replace('"',''),'wt')
            
                f.write('info face=%s size=%s bold=%s italic=%s charset=%s unicode=%s stretchH=%s smooth=%s aa=%s padding=%s spacing=%s' % (fnt_data["info"]["face"], fnt_data["info"]["size"], fnt_data["info"]["bold"], fnt_data["info"]["italic"], fnt_data["info"]["charset"], fnt_data["info"]["unicode"], fnt_data["info"]["stretchH"], fnt_data["info"]["smooth"], fnt_data["info"]["aa"], fnt_data["info"]["padding"], fnt_data["info"]["spacing"]))
                f.write('\ncommon lineHeight=%s base=%s scaleW=%s scaleH=%s pages=%s packed=%s' % (fnt_data["common"]["lineHeight"], fnt_data["common"]["base"], fnt_data["common"]["scaleW"], fnt_data["common"]["scaleH"], fnt_data["common"]["pages"], fnt_data["common"]["packed"]))
                f.write('\npage id=%s file=%s' % (fnt_data["page"]["id"], fnt_data["page"]["file"]))
                f.write('\nchars count=%s' % (fnt_data["chars count"]))
                for key in dictChar:
                    f.write('\nchar id=%s     x=%s   y=%s   width=%s   height=%s   xoffset=%s   yoffset=%s   xadvance=%s   page=%s   chnl=%s' % (key[1]["id"], key[1]["x"], key[1]["y"], key[1]["width"], key[1]["height"], key[1]["xoffset"], key[1]["yoffset"], key[1]["xadvance"], key[1]["page"], key[1]["chnl"]))
                f.write('\nkernings count=%s' % (fnt_data["kernings count"]))
                for key in dictKern:
                    f.write('\nkerning first=%s second=%s amount=%s' % (key[1]["first"], key[1]["second"], key[1]["amount"]))
                
                
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
                
            else:
                print("Invalid file(" + fileI[w] + ")! Your input file must be in either high, medium graphic and have the correct name from the resource folder.")
                
        elif file_extensionInput == ".png":

            if filenameInput[-3:] == "uhd" and args.low:
                im = cv2.imread(filenameInput+".png",cv2.IMREAD_UNCHANGED)

                width = ceil(im.shape[1] / 4 )
                height = ceil(im.shape[0] / 4 )
                dim = (width, height)
                resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

                cv2.imwrite(filenameInput.replace("-uhd","") + ".png",resized)
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
        
            elif filenameInput[-3:] == "uhd" and (not args.low):
                im = cv2.imread(filenameInput+".png",cv2.IMREAD_UNCHANGED)

                width =  ceil(im.shape[1] / 2 )
                height = ceil(im.shape[0] / 2 )
                dim = (width, height)
                resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

                cv2.imwrite(filenameInput.replace("uhd","hd") + ".png",resized)
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
      
            elif filenameInput[-3:] == "-hd":
                im = cv2.imread(filenameInput+".png",cv2.IMREAD_UNCHANGED)

                width = ceil(im.shape[1] / 2 )
                height = ceil(im.shape[0] / 2 )
                dim = (width, height)
                resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

                cv2.imwrite(filenameInput.replace("-hd","") + ".png",resized)
                print("Done!(" + str((w+1)) + "/" + str(len(fileI)) + ")")
                if (w+1) == len(fileI):
                    print("Porting finished.")
                
            else:
                print("Invalid file(" + fileI[w] + ")! Your input file must be in either high, medium graphic and have the correct name from the resource folder.")

        else:
            print("WHAT THE FUCK HOW DID THIS FUCKING FILE(%s) GET PASS MY TRASH FILES REMOVAL SYSTEM LOL" % fileI[w])

else:
    print ("BRO I DONT FUCKING WANT TO DELETE 350 INDENTATIONS LOL")
