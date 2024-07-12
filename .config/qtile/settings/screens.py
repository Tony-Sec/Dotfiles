from libqtile.config import Screen
from libqtile import widget ,qtile, bar
from .colors import colors,ColorA,ColorB,ColorC,ColorD,ColorE,ColorF,ColorG,ColorH,ColorI,ColorZ






### Mouse_callback functions
def open_pavu():
    qtile.cmd_spawn("pavucontrol")

def open_instantsettings():
    qtile.cmd_spawn("xdotool key super+r")


##### Funciones para la barra
# Separador 
def separador_bar():
    return widget.Sep(
        linewidth=2,
        foreground=ColorC,
        background=ColorC,
        padding=10,
        size_percent=40,
        )
def separador_icon():
    return widget.Sep(
                linewidth=3,
                foreground=ColorZ,
                background=ColorC,
                padding=5,
                size_percent=100,
            )
def separador_Z():
    return widget.Sep(
                linewidth=0,
                foreground=ColorZ,
                background=ColorZ,
                padding=10,
                size_percent=50,
            )
def icono_difuminado():
    return widget.TextBox(
                text = "█▓▒░",
                font = "feather", #"feather"
                fontsize = 64,
                background = ColorZ,
                foreground = ColorC,
                padding = 0
                )

# Boton Rofi
def boton_rofi():
    return widget.TextBox(
                text="󰣇",
                foreground =ColorZ,
                background=ColorC,
                font = "Iosevka Nerd Font",
                fontsize = 65,
                padding = 45,
                mouse_callbacks = {"Button1": open_instantsettings},
            )
# Workspaces
def group_box():
    return widget.GroupBox(
                active = 'ffffff', # ColorG
                background = ColorC,
                foreground = 'ffffff', # Blanco 'ffffff'
                font='Iosevka Nerd Font', #Ubuntu Mono Nerd Font
                fontsize=50,
                margin_y=3,
                margin_x=0,
                padding_y=0,
                padding_x=0,
                borderwidth = 3.5,
                disable_drag=True,
                #rounded=False,
                #highlight_method='text',
                urgent_alert_method='block',            
                inactive=ColorZ,
                urgent_border='ff5555', #colors[3][0] red 
                this_current_screen_border=ColorG,
                this_screen_border=ColorH,
                #other_current_screen_border=colors[14][0],# dark
                #other_screen_border=colors[14][0],
            )

# Blocks
def update_block(ColorD,ColorF,ColorZ):
    return [
        widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 57,
                       background = ColorF,
                       foreground = ColorZ,
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 57,
                       background = ColorZ,
                       foreground = ColorD,
                       padding = 0
                       ),             
                widget.TextBox(
                       text = "󰁪 ",
                       font = "Iosevka Nerd Font",
                       fontsize = 45,
                       foreground = ColorZ,
                       background = ColorD,
                       padding = 0,
                       ),
                widget.CheckUpdates (
                    display_format = '{updates}',
                    colour_have_updates = colors[5][0],
                    colour_no_updates = ColorD,
                    no_update_string = '0',
                    update_interval = 1800,
                    foreground=ColorZ,
                    background=ColorD,
                )
    ]
def net_block(ColorG, ColorI, ColorZ, interface="ens33"):
    return [
        widget.TextBox(
            text="",
            font="Iosevka Nerd Font",
            fontsize=60,
            background=ColorZ,
            foreground=ColorI,
            padding=0
        ),
        widget.TextBox(
            text="",
            font="Iosevka Nerd Font",
            fontsize=60,
            background=ColorI,
            foreground=ColorG,
            padding=0
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=45,
            background=ColorG,
            foreground=ColorZ,
            padding=0
        ),
        widget.Net(
            background=ColorG,
            foreground=ColorZ,
            padding=5,
            interface=interface,
            format='↓{down}'
        )
    ]
def mem_block(ColorF,ColorG,ColorZ):
    return [
                widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorG,
                       foreground = ColorZ,
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorZ,
                       foreground = ColorF,
                       padding = 0
                       ),              
                widget.TextBox(
                       text = " ",
                       font = "Iosevka Nerd Font",
                       fontsize = 45,
                       background = ColorF,
                       foreground = ColorZ,
                       padding = 0,
                       ),
                widget.Memory(
                        background=ColorF,
                        foreground=ColorZ,
                        format='{MemUsed: .0f} MB ',
                        )
    ]
def cpu_block(ColorD,ColorF,ColorZ):
    return [
        widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorF,
                       foreground = ColorZ,
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorZ,
                       foreground = ColorD,
                       padding = 0
                       ),             
                widget.TextBox(
                       text = " ",
                       font = "Iosevka Nerd Font",
                       fontsize = 45,
                       foreground = ColorZ,
                       background = ColorD,
                       padding = 0
                       ),
                widget.CPU (
                    foreground=ColorZ,
                    background=ColorD,
                )
    ]
def date_blocks(ColorB,ColorD,ColorZ):
    return [
                widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorD,
                       foreground = ColorZ,
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorZ,
                       foreground = ColorB,
                       padding = 0
                       ),       
                widget.TextBox(
                    text="󰃮 ",
                    font = "Iosevka Nerd Font",
                    fontsize = 45,
                    foreground=ColorZ,  
                    background=ColorB,
                ),
                widget.Clock(
                    format = '%a %d-%m-%y',
                    background=ColorB,
                    foreground=ColorZ,
                )
    ]
def clock_blocks(ColorB,ColorH,ColorZ):
    return [
        widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorB,
                       foreground = ColorZ,
                       padding = 0
                       ),      
                widget.TextBox(
                       text = "",
                       font = "Iosevka Nerd Font",
                       fontsize = 60,
                       background = ColorZ,
                       foreground = ColorH,
                       padding = 0
                ),                      
                widget.TextBox(
                    text = " ",
                    font = "Iosevka Nerd Font",
                    fontsize = 45,
                    background = ColorH,
                    foreground = ColorZ,
                    padding = 0
                ),
                widget.Clock(
                    background=ColorH,
                    format = '%I:%M',
                    foreground = ColorZ,
                    icons_size=20,
                    padding=8
                ),
                widget.Sep(
                    padding = 6,
                    linewidth = 0,
                    background = ColorH,
                    foreground = ColorH,
                )
    ]

update_widgets = update_block(ColorD,ColorF,ColorZ)
net_widgets = net_block(ColorG, ColorI, ColorZ)
mem_widgets = mem_block(ColorF,ColorG,ColorZ)
cpu_widgets = cpu_block(ColorD,ColorF,ColorZ)
date_widgets = date_blocks(ColorB,ColorD,ColorZ)
clock_widgets = clock_blocks(ColorB,ColorH,ColorZ)

screens = [
    Screen(
        top=bar.Bar(
            [
                boton_rofi(),
                separador_icon(),
                separador_icon(),
                group_box(),
                icono_difuminado(),
                #separador_Z(),
                widget.Spacer(background = ColorZ),
                #separador_Z(),

                #*update_widgets,
                *net_widgets,
                *mem_widgets,
                *cpu_widgets,
                *date_widgets,
                *clock_widgets,
                

                widget.Systray(),
                #widget.QuickExit(
                #background=ColorZ,
                #),
            ],
            74,
            margin=[0, 0, 5, 0],
            opacity=0.85,
        ),
        bottom=bar.Gap(18),
        left=bar.Gap(18),
        right=bar.Gap(18),
    ),
]
