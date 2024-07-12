import os
import json



#Eliminar colores de pywal y poner wallpaper
os.system('/home/zayk/.local/scripts/set_wallpaper')

'''
########################
# Define colors ########
########################

#Pywal Colors
colors_ = []
cache='/home/zayk/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors_.append(file.readline().strip())
    colors_.append('#ffffff')
    lazy.reload()
load_colors(cache)
'''

########################
# Define colors ########
########################
#Pywal Colors

colors = os.path.expanduser('~/.cache/wal/colors.json')

colordict = json.load(open(colors))
ColorZ=(colordict['colors']['color0'])
ColorA=(colordict['colors']['color1'])
ColorB=(colordict['colors']['color2'])
ColorC=(colordict['colors']['color3'])
ColorD=(colordict['colors']['color4'])
ColorE=(colordict['colors']['color5'])
ColorF=(colordict['colors']['color6'])
ColorG=(colordict['colors']['color7'])
ColorH=(colordict['colors']['color8'])
ColorI=(colordict['colors']['color9'])

colors = [
    ["#1c2023", "#1c2023"],  # background 0
    ["#d8dee9", "#d8dee9"],  # foreground 1
    ["#3b4252", "#3b4252"],  # background lighter 2
    ["#bf616a", "#bf616a"],  # red 3
    ["#a3be8c", "#a3be8c"],  # green 4
    ["#ebcb8b", "#ebcb8b"],  # yellow 5
    ["#81a1c1", "#81a1c1"],  # blue 6
    ["#b48ead", "#b48ead"],  # magenta 7
    ["#88c0d0", "#88c0d0"],  # cyan 8
    ["#e5e9f0", "#e5e9f0"],  # white 9
    ["#4c566a", "#4c566a"],  # grey 10
    ["#d08770", "#d08770"],  # orange 11
    ["#8fbcbb", "#8fbcbb"],  # super cyan 12
    ["#5e81ac", "#5e81ac"],  # super blue 13
    ["#242831", "#242831"],  # super dark background 14
]
