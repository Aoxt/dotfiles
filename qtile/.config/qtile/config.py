# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal

#Imports extra fuera de la configuracion inicial----------------------------

import os 
import subprocess
from libqtile import hook,config
from src import variables,themes
#---------------------------------------------------------------------------

#---------------------------------Codigo para iniciar el script autostart 
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/src/autostart.sh')
    try:
        # Asegúrate de que Popen recibe una lista si el comando tiene argumentos,
        # pero para un script simple, solo el path es suficiente.
        # También puedes usar ['sh', autostart_script] si prefieres
        subprocess.Popen([home]) 
        # subprocess.Popen([autostart_script]) #Ruta relativa
    except Exception as e:
        # Es buena idea registrar errores si algo sale mal
        # Puedes usar el logger de Qtile o simplemente imprimir
        print(f"Error al ejecutar autostart script: {e}")

# Variables utilizadas definidas por el archivo variables.py que esta en src
mod = variables.mod
terminal = variables.terminal
#================================================================================

# -------------------------------------------------------------------
# Importa el módulo de temas desde src/themes.py y selecciona el tema
# -------------------------------------------------------------------
try:
    # ¡Cambio aquí! Importa el módulo 'themes' desde el paquete 'src'
    from src import themes
except ImportError:
    print("Advertencia: No se encontró el módulo 'src/themes.py'. Usando colores por defecto.")
    # Define un tema básico por defecto si falla la importación
    themes = type('obj', (object,), { # Simula el módulo 'themes'
        'default_theme': {
            'foreground': '#ffffff', 'background': '#000000', 'alt_background': '#222222',
            'disabled': '#555555', 'accent': '#0077cc', 'red': '#ff0000', 'green': '#00ff00',
            'yellow': '#ffff00', 'blue': '#0000ff', 'magenta': '#ff00ff', 'cyan': '#00ffff',
            'white': '#ffffff', 'name': 'Default Fallback'
        }
    })()
    active_theme_name = 'default_theme'


# --- ¡¡¡ AQUÍ SELECCIONAS EL TEMA QUE QUIERES USAR !!! ---
# Cambia esta variable al nombre del diccionario definido en src/themes.py
# active_theme_name = "catppuccin_mocha"
active_theme_name = "tokyo_night_storm"
# active_theme_name = "rose_pine"
# ----------------------------------------------------------

# Carga el diccionario del tema seleccionado desde el módulo importado 'themes'
try:
    # ¡Cambio aquí! Accede a los diccionarios a través del módulo 'themes' importado
    theme = getattr(themes, active_theme_name)
    print(f"Tema cargado: {theme.get('name', active_theme_name)}")
except AttributeError:
    print(f"Error: El tema '{active_theme_name}' no está definido en src/themes.py.")
    # Intenta usar el primer tema definido o el fallback si todo falla
    try:
        # Accede al primer atributo del módulo 'themes' importado
        first_theme_name = next(attr for attr in dir(themes) if not attr.startswith('_') and isinstance(getattr(themes, attr), dict))
        theme = getattr(themes, first_theme_name)
        print(f"Usando el primer tema encontrado como fallback: {first_theme_name}")
    except (StopIteration, AttributeError, NameError): # NameError si la importación falló
         # Si incluso el fallback de importación falló, usa uno super básico
        theme = {
            'foreground': '#ffffff', 'background': '#000000', 'alt_background': '#222222',
            'disabled': '#555555', 'accent': '#0077cc', 'red': '#ff0000', 'green': '#00ff00',
            'yellow': '#ffff00', 'blue': '#0000ff', 'magenta': '#ff00ff', 'cyan': '#00ffff',
            'white': '#ffffff', 'name': 'Super Fallback'
        }
        print("Error crítico cargando temas. Usando colores básicos.")

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    #==========================================Keys Personalizadas==============================
    Key([mod],"d",lazy.spawn("rofi -show run"),desc="Apareve el lanzadore de apliaciones rofi")
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Key(
            #     [mod, "shift"],
            #     i.name,
            #     lazy.window.togroup(i.name, switch_group=True),
            #     desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

theme_border_width = theme.get('border_width_layout', 2) # Grosor desde tema o 2 por defecto
theme_border_normal = theme.get('border_normal_layout', theme['alt_background']) # Color normal desde tema/fallback

layouts = [
    layout.Columns(
        border_focus_stack=[
            theme['focus_stack_main'],
            theme['focus_stack_alt']
        ],
        border_focus=theme['accent'],        # Color enfocado = acento del tema
        border_normal=theme_border_normal,   # Color normal = desde tema/fallback
        border_width=theme_border_width,     # Grosor = desde tema/fallback
        margin=theme.get('layout_margin', 5) # Margen desde tema/fallback
    ),
    layout.Max(
        border_focus=theme['accent'],        # Aplica también a Max
        border_normal=theme_border_normal,
        border_width=theme_border_width,
        margin=theme.get('layout_margin', 5) # Margen en Max si lo quieres
    ),
    # --- ¡Aplica estos parámetros de borde a TODOS tus layouts! ---
]

widget_defaults = dict(
    font=theme.get('font_main', 'JetBrainsMono Nerd Font'), # Fuente principal del tema o fallback
    fontsize=theme.get('font_size_main', 12),        # Tamaño principal del tema o fallback
    padding=theme.get('widget_padding', 3),          # Padding del tema o fallback
    background=theme['background'],                  # Fondo por defecto de los widgets (OBLIGATORIO en tema)
    foreground=theme['foreground']                   # Color de texto por defecto (OBLIGATORIO en tema)
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                
                widget.GroupBox(
                    active=theme['foreground'],          # Color texto grupo activo
                    inactive=theme['disabled'],          # Color texto grupo inactivo
                    highlight_method='block',            # Método de resaltado ('block', 'border', 'text')
                    # Colores para el método 'block' o 'border':
                    this_current_screen_border=theme['accent'],  # Color del resaltado principal
                    other_screen_border=theme['alt_background'], # Color resaltado en otras pantallas
                    this_screen_border=theme['alt_background'],  # Color resaltado inactivo en esta pantalla
                    other_current_screen_border=theme['accent'],
                    urgent_border=theme['red'],              # Color para alertas urgentes
                    urgent_text=theme['red'],                # Texto urgente (opcional)
                    # Configuración del bloque/borde:
                    borderwidth=theme.get('groupbox_borderwidth', 10), # Grosor del resaltado
                    padding_y=theme.get('groupbox_padding_y', 5), # Padding vertical
                    margin_y=theme.get('groupbox_margin_y', 3),  # Margen vertical
                    rounded=theme.get('groupbox_rounded', True), # Bordes redondeados en el bloque/borde
                    # background=theme['alt_background'] # Opcional: Fondo para toda la caja de grupos si es diferente al de la barra
                ),
                widget.Sep(
                linewidth=0, # Sin línea visible
                padding=30   # 10 píxeles de espacio horizontal
                ),
                widget.Prompt(
                    foreground=theme['foreground'], # Color del texto
                    prompt=theme.get('prompt_text', '$ ') # Texto del prompt (opcional)
                ),
                widget.Sep(
                linewidth=0, # Sin línea visible
                padding=30  # 10 píxeles de espacio horizontal
                ),
                widget.CurrentLayout(
                    foreground=theme['foreground'] # Color del texto
                ),
                widget.Sep(
                linewidth=0, # Sin línea visible
                padding=30
                ),
                widget.WindowName(
                    foreground=theme['accent'], # Usar acento para el nombre de la ventana
                    format='{name}'             # Formato del texto
                ),
                widget.Sep(
                linewidth=0, # Sin línea visible
                padding=30
                ),
                widget.Chord(
                    chords_colors={
                        # Usa colores del tema para los modos de Chord
                        "launch": (theme['red'], theme['foreground']),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Sep(
                linewidth=0, # Sin línea visible
                padding=30
                ),
                # Puedes eliminar estos TextBoxes o tematizarlos si los necesitas:
                # widget.TextBox("default config", name="default", foreground=theme['disabled']),
                # widget.TextBox("Press <M-r>", foreground=theme['yellow']), # Ejemplo: usar amarillo

                # Es importante a veces ponerle fondo explícito al systray
                widget.Systray(background=theme['background'],padding=10,icon_size=20),

                widget.Sep(
                linewidth=0, # Sin línea visible
                padding=30
                ),

                widget.Clock(
                    format="%d-%m-%Y %a %I:%M %p",
                    foreground=theme['foreground'] # Color del texto del reloj
                ),
                widget.Sep(
                linewidth=1,
                padding=30,
                foreground=theme['disabled'] # Línea de color gris
                ),
                widget.QuickExit(
                    default_text='[X]',
                    countdown_format='[{}]',
                    foreground=theme['red'],
                     # Usar rojo para el botón de salir
                ),
                widget.Sep(
                linewidth=1,
                padding=30,
                foreground=theme['disabled'] # Línea de color gris
                ),
                # Puedes añadir más widgets aquí, ejemplo:
                # widget.CPU(
                #     format='CPU {load_percent}%',
                #     foreground=theme['green'],
                #     background=theme['alt_background'], # Fondo diferente para destacar
                #     padding=5
                #  ),
                # widget.Memory(
                #     format='{MemUsed: .0f}{mm}',
                #     foreground = theme['blue'],
                #     background = theme['alt_background'],
                #     padding = 5
                # ),
            ],
            35,
            background=theme['background'],
            margin=[5, 10, 0, 10],
            #border_width=[1, 1, 1, 1],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    # --- Aplica el tema a los bordes flotantes ---
    border_focus=theme['accent'],  # Borde enfocado usa color de acento
    border_normal=theme.get('border_normal_layout', theme['alt_background']), # Borde normal
    border_width=theme.get('border_width_floating', theme.get('border_width_layout', 2)) # Ancho del borde
    # ---------------------------------------------
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

