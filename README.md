# Muse-Player
Cli Music Player made inside python

## Install Binaries
Download Latest Binaries From github - `wget https://github.com/Dunn-Dev8/Muse-Player/releases/download/0.1.22/museplayer`

Make file Executable - `chmod +x museplayer`

## Build With pyinstaller
Cone Git Repo - `https://github.com/Dunn-Dev8/Muse-Player`

Move to the Muse-Player Directory - `Cd Muse-Player`

Make sure pip is installed
Debian - `apt install python3-pip`

Arch - `sudo pacman -S python-pip`
[If your Linux Distro is not mentioned here than search how to install pip for python3 on your appropriate Distro]

Download Pip installer - `pip install pyinstaller`

Make Binary with pyinstaller - `pyinstaller museplayer.py --onefile`

go to directory with binary inside it - `cd dist/`

execute museplayer - `./museplayer`

## Make Museplayer executable anywhere
move museplayer to the Bin folder (so you can execute command anywhere)
`sudo mv ./museplayer /bin/`


## Command Usage
NOTE: the most recent version of museplayer 0.1.22 currently only has support for queuing 2 songs at a time
BEFORE USING: make sure you follow the steps inside **Make Museplayer execute anywhere** before following steps below

Play one song - `museplayer /Location/of/song/`

queue song (2 is the limit as of v0.1.22) - `museplayer /Location/of/first/song/ /Location/of/second/song/`

