#!/bin/sh

# setxkbmap es

# xwinwrap -fs -fdt -ni -b -nf -un -o 1.0 -debug -- mpv -wid WID --loop --no-audio ~/Imágenes/video.mp4 &
vmware-user-suid-wrapper &
picom --no-vsync &

