# pdf2mp3
The idea behind this project is to avoid paying for audiobooks. 
I built this project with the inspiration of [Programming Hero's Video](https://www.youtube.com/watch?v=kyZ_5cvrXJI). You can find a link to his original project [here](https://github.com/ProgrammingHero1/audiobook). The only real difference between the one his project and mine is that mine generates a .mp3 file instead of reading it out.

# Requirements
For me, I found that MacOS offers the best text-to-speech voices. With that said, this script is specifically targeted to MacOS.
Some modifications would be needed to make it work with GNU/Linux or Windows. 

I believe any version of Python 3 /should/ work, but don't quote me on that.

# Installation
    pip3 -r requirements.txt

# Usage
    pdf2mp3.py [-h] [-i (--pdf) <your_pdf.pdf>] [-o (--mp3) <output_file.mp3>] [-p (--start) <page # to start saving at>]
