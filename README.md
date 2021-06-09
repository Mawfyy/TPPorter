

# Texture Pack Porter

A simple program to port any of your texture packs from high graphics to medium or low graphic, or from medium to low graphic(With a not so high quality and accuracy but good enough)

(You need to have the .plist/.fnt/.png files that you want to port in the same folder as the python script)

# Usage:

Usage command:

```
python3 porter.py [-l/--low]
```

(Your terminal/command prompt must also be pointing to the same folder as the tp you want to port)

Some usage examples:

![An example](https://cdn.discordapp.com/attachments/776630512327458837/848578495340871731/Screenshot_2021-05-30-22-04-43-450_com.termux.png)
![Another one but with the -l argument](https://cdn.discordapp.com/attachments/776630512327458837/848580274575900692/Screenshot_2021-05-30-22-14-41-757_com.termux.png)

A bit of warnings: As of v0.5, the accuracy for low ports is really low(unironcally), so don't expect the low ports to be always perfect (same as the medium ports though...)

(You also need to provide a .plist file for the .png sprite you want to port, since this porter just resizes the .png file to half)

# Requirements

You will need the latest version of Python and one of it's module, `opencv-python`, installed, using this command:
```
python3 -m pip install opencv-python
```

For Termux(Android's Terminal emulator) users, you can instead install the `opencv` package by these commands:
```
curl -LO https://its-pointless.github.io/setup-pointless-repo.sh
bash setup-pointless-repo.sh
pkg install opencv
```





