

# Texture Pack Porter

A simple program to port any of your texture packs from high graphics to medium or low graphic, or from medium to low graphic(With a not so high quality and accuracy but good enough)

(You need to have the plist file and the relative png in the same folder as the python script)

Usage:

```porter.py -i [list of original .plist/.png files from a tp] -o [list of the output names for each file you input, respectively]```

Some usage examples:
![A funny example](https://cdn.discordapp.com/attachments/776630512327458837/845705289382625380/Screenshot_2021-05-22-23-47-59-580_com.termux.png)
![Another one](https://cdn.discordapp.com/attachments/776630512327458837/845705300447330324/Screenshot_2021-05-22-23-50-33-821_com.termux.png)


# Requirements

You will need the latest version of Python and one of it's module, `opencv-python`, installed.

For Termux users, you can instead install the `opencv` package by these commands:
```
curl -LO https://its-pointless.github.io/setup-pointless-repo.sh
bash setup-pointless-repo.sh
pkg install opencv
```





