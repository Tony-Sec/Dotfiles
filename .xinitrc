#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then

    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then

    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

vmware-user-suid-wrapper &

xrandr --output Virtual1 --mode 3840x2400  2>/dev/null  &
xrdb -merge .Xresources 
#xdotool key super+F5

# Compositores
#xcompmgr & #Simple y rapido

exec picom & #Complejo y un poco mas pesado

# Wallpapers
/home/zayk/.local/scripts/newlook &

# DWM
dwmblocks &
exec dwm
