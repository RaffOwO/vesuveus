# You are in the directory: vesuveus/files

Here you can fine all the files that are used in the project, plus a build on how to build a vesuveus urself.

## Directory structure
- /`code`: This directory contains the code.py to use along kmk firmware.
    ---
- /`media`: This directory contains the images used in the README.md(s) file.
    ---
- /`printables`: This directory contains the printable STL/3MFs.
    ---
- /`production`: This directory contains the files used to produce the keyboard.
    ---
- /`README.md`: This file.
    ---

# How to build your own Vesuveus (WIP)

In the alternative-versions folder you can find some OLD versions and other revisions made by the community, always appreciated!

Note that this guide refers to the current version that you can find in 'files/printables' directory!

Also this section is a work in progress, I will update it as soon as I can. Next time I will build another one of this beauty I will take more pictures and videos to make the guide more complete.

### BOM (Bill of Materials)
What you need:

- 42 switches
   - any MX style switch will work

- 42 keycaps
    - any MX style keycap will work 

- 42 diodes
    - I used 1N4148 diodes, you can find them easily on Amazon or Aliexpress 

- 20 magnetic disks 8x2cm
    - I used [these](https://www.amazon.it/gp/product/B07Z5QZQZQ/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) but you can use any other magnetic disk you want as long as they are 8cm in diameter and 2cm in height (or less)

- 1 MCU
    - I used a waveshare RP 2040 Zero, but you can use any other MCU you want as long is compatible with KMK and has at least 14 GPIO pins.

- the plate and the base (3D printed)
    - you can find the STL/3MF files in the 'files/printables' directory

- soldering equipment
    - a soldering iron, community alwasy suggest [pinecil](https://www.pine64.org/pinecil/), I always used a cheap one from Amazon and it worked just fine

    - soldering tin, I use 0.5mm tin but you can use any other tin you want

    - wires, I use 22 AWG wires but as always you can use any other wire you want

- strong glue
    - I used [this](https://www.amazon.it/gp/product/B07Z5QZQZQ/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) but you can use any other glue you want as long as it's strong enough to keep the magnetic disks in place
    
- a lot of patience, love and passion (but if you are here you already have that 🤍)

# Build guide

## 1. Download the files
Clone the repository or download the zip file.

## 2. Print the case and plate
From the printables directory, print the case and the plate. 
I suggest you to use 3MF files, because I used the free version of Shapr3D to design the keyboard, and the 3MF files are more accurate than the STL files.

## 3. Clean the case and plate (optional)
Clean the case and plate from imperfections, i suggest to use some fine sandpaper.

## 4. Glue the magnets
Glue the magnets in the case and plate in the circular spots, the magnets should be flush with the surface.

**Tip:** Let the glue dry, don't try to put the plate and the case before the glue is dry, work with single part at a time.

## 5. Put the switches on the plate
Put the switches on the plate. the pins should face down, and the switch should be flush with the plate.

## 6. Prepare the diodes
Using a pair of tweezers, bend the diodes legs to make a circle and cut off the excess, then position the pin of the switch in the circle.

## 7. Prepare the pins
Solder a bit of soldering tin on the pins of the switches, this will help you to solder the diodes & wires.

## 8. Solder the diodes
Solder the diodes to the pins of the switches, make sure that the diodes are in the right direction, the black band should face the top.

## 9. Prepare the wires
Take the wires and cut them to the right length, then strip the ends of the wires.

## 10. Solder the wires
First, tin the wires, then solder them to the diodes, and the left pin of the switches.
The diodes are wired in rows, so the wires should be soldered in the same row of the diodes.
The switches left pin are wired in columns, so the wires should be soldered in the same column of the switches.

## 11. Prepare & Solder the MCU
Tin a bit the MCU pins, then solder the wires to the MCU.

## 12. Flash the MCU
Flash the MCU with the firmware of your choice, i suggest you to use KMK firmware with my keymap.

## 13. Finishing touches
Now you just need to put the plate and case together, also you can put some rubber feet on the case, and dont forget to put the keycaps on the switches.

## 14. Type your satisfaction
Now you can type your satisfaction, and enjoy your new keyboard.
    

### Video Guide (WIP)

[Vesuveus Build Guide!](https:/youtube.com/)

