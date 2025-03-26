# -*- coding: utf-8 -*-
# =========================================================================== #
# Configuración de Qtile                                                      #
# ~/.config/qtile/config.py                                                   #
# Basado en la configuración por defecto y modificaciones personalizadas.     #
#                                                                             #
# Ubicación actual: Ciudad Guzmán, Jalisco, México                           #
# Fecha/Hora actual: Martes, 25 de Marzo de 2025, 5:34 PM CST                  #
# =========================================================================== #

# --- Importaciones Necesarias ---
import os
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal # Ya no es necesario, definimos 'terminal' manualmente

# =========================================================================== #
# === AUTOSTART ===
# Ejecuta un script externo una vez al iniciar Qtile. Ideal para lanzar
# programas como picom, nitrogen/feh, dunst, nm-applet, etc.
# =========================================================================== #
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    try:
        subprocess.Popen([home])
    except FileNotFoundError:
        # Opcional: Manejo si no se encuentra el script
        print(f"Advertencia: No se encontró el script de autostart en {home}")
    except PermissionError:
        print(f"Advertencia: Permisos insuficientes para ejecutar {home}. ¿Hiciste 'chmod +x'?")


# =========================================================================== #
# === PALETA DE COLORES ===
# Define los colores que se usarán en la configuración (barra, bordes, etc.)
# Ejemplo: Paleta Nord (Puedes buscar otras o crear la tuya)
# =========================================================================== #
colors = {
    "bg":      "#2E3440", # Nord0  (Fondo principal)
    "fg":      "#D8DEE9", # Nord4  (Texto principal)
    "gray":    "#4C566A", # Nord3  (Gris oscuro, comentarios, inactivos)
    "white":   "#ECEFF4", # Nord6  (Blanco brillante)
    "red":     "#BF616A", # Nord11 (Rojo, errores, urgente)
    "orange":  "#D08770", # Nord12 (Naranja)
    "yellow":  "#EBCB8B", # Nord13 (Amarillo, advertencias)
    "green":   "#A3BE8C", # Nord14 (Verde, éxito)
    "magenta": "#B48EAD", # Nord15 (Magenta)
    "blue":    "#5E81AC", # Nord10 (Azul, selección, info)
    "cyan":    "#88C0D0", # Nord8  (Cyan, strings, nombres de ventana)
}

# =========================================================================== #
# === VARIABLES GLOBALES ===
# =========================================================================== #
mod = "mod4"        # Tecla Mod principal (Super/Windows)
terminal = "alacritty" # Tu terminal preferida

# =========================================================================== #
# === ATAJOS DE TECLADO (Keybindings) ===
# =========================================================================== #
keys = [
    # --- Movimiento y Foco de Ventanas (Estilo Vim/Flechas) ---
    Key([mod], "h", lazy.layout.left(), desc="Mover foco a la izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover foco a la derecha"),
    Key([mod], "j", lazy.layout.down(), desc="Mover foco hacia abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover foco hacia arriba"),
    Key([mod], "space", lazy.layout.next(), desc="Mover foco a la siguiente ventana"),

    # --- Mover Ventanas ---
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Mover ventana a la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Mover ventana a la derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Mover ventana hacia abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Mover ventana hacia arriba"),

    # --- Redimensionar Ventanas (Layouts Column/BSP) ---
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Crecer ventana a la izquierda"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Crecer ventana a la derecha"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Crecer ventana hacia abajo"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Crecer ventana hacia arriba"),
    Key([mod], "n", lazy.layout.normalize(), desc="Restablecer tamaños de ventana"),

    # --- Layouts ---
    Key([mod], "Tab", lazy.next_layout(), desc="Cambiar al siguiente layout"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(), # Útil en layout Columns
        desc="Alternar entre lados divididos/no divididos del stack",
    ),

    # --- Acciones de Ventana ---
    Key([mod], "w", lazy.window.kill(), desc="Cerrar ventana activa"),
    Key([mod],"f", lazy.window.toggle_fullscreen(), desc="Alternar pantalla completa"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Alternar ventana flotante"),

    # --- Control de Qtile ---
    Key([mod, "control"], "r", lazy.reload_config(), desc="Recargar configuración de Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Salir de Qtile"),

    # --- Lanzadores ---
    Key([mod], "Return", lazy.spawn(terminal), desc="Lanzar terminal"),
    # Modificado para usar dmenu
    # Modificado para usar dmenu
    # Key([mod], "d", lazy.spawn("dmenu_run -i -l 10 -p 'Lanzar:' -nb '#2E3440' -nf '#D8DEE9' -sb '#88C0D0' -sf '#2E3440' -fn 'monospace:size=11'"), desc="Launch dmenu (vertical)"),
    # Key([mod], "d", lazy.spawn("dmenu_run -i -l 10 -p 'Lanzar:' -nb '#2E3440' -nf '#D8DEE9' -sb '#88C0D0' -sf '#2E3440' -fn 'monospace:size=11' -b"), desc="Launch dmenu (vertical, bottom)"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Lanzar Rofi (modo drun)"),
    # Key([mod], "r", lazy.spawncmd(), desc="Lanzar prompt de Qtile (spawncmd)"), # Opcional: prompt básico en la barra

    # --- Control de Volumen (Ejemplo usando pamixer - instala pamixer) ---
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5"), desc="Subir volumen"),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5"), desc="Bajar volumen"),
    # Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"), desc="Silenciar/Desilenciar volumen"),

    # --- Control de Brillo (Ejemplo usando brightnessctl - instala brightnessctl) ---
    # Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Subir brillo"),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Bajar brillo"),
]


# =========================================================================== #
# === GRUPOS / ESPACIOS DE TRABAJO (Workspaces) ===
# =========================================================================== #
groups = [Group(i) for i in "123456789"] # Nombres simples 1-9

for i in groups:
    keys.extend(
        [
            # Mod + número = Cambiar al grupo
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Cambiar al grupo {i.name}",
            ),
            # Mod + Shift + número = Mover ventana activa al grupo (y cambiar a él)
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Mover ventana al grupo {i.name} y cambiar a él",
            ),
            # Alternativa: Mod + Shift + número = Mover ventana activa al grupo (SIN cambiar a él)
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="Mover ventana al grupo {}".format(i.name)),
        ]
    )

# =========================================================================== #
# === LAYOUTS (Distribuciones de Ventanas) ===
# =========================================================================== #
layouts = [
    layout.Columns(
        border_focus=colors["blue"],    # Color del borde de la ventana activa
        border_normal=colors["gray"],   # Color del borde de las ventanas inactivas
        border_width=2,                 # Grosor del borde
        margin=8,                       # Margen alrededor de las ventanas
        #border_focus_stack=["#d75f5f", "#8f3d3d"], # Colores alternativos si hay varias columnas
        #border_on_single=True          # Mostrar borde aunque solo haya una ventana
    ),
    layout.Max(
        border_focus=colors["blue"],
        border_normal=colors["gray"],
        border_width=0,                 # Sin borde en modo maximizado (opcional)
        margin=8                        # Margen
    ),
    # --- Otros Layouts para probar (descomenta y configura) ---
    # layout.Stack(num_stacks=2, border_width=2, margin=8, border_focus=colors["blue"], border_normal=colors["gray"]),
    # layout.MonadTall(border_width=2, margin=8, border_focus=colors["blue"], border_normal=colors["gray"]),
    # layout.Floating(border_width=2, border_focus=colors["blue"], border_normal=colors["gray"]), # Para ventanas flotantes explícitas
    # layout.TreeTab( ... ),
    # layout.Bsp( ... ),
    # layout.Matrix( ... ),
]

# =========================================================================== #
# === CONFIGURACIÓN POR DEFECTO DE WIDGETS ===
# Establece valores comunes para todos los widgets, se pueden sobrescribir individualmente.
# =========================================================================== #
widget_defaults = dict(
    font="JetBrainsMono Nerd Font", # Fuente principal para la barra (¡Asegúrate de tenerla!)
    fontsize=14,                  # Tamaño de la fuente
    padding=3,                    # Espaciado interno de los widgets
    foreground=colors["fg"]       # Color de texto por defecto
)
extension_defaults = widget_defaults.copy()

# =========================================================================== #
# === PANTALLAS y BARRA(S) ===
# Aquí se define qué barra y qué widgets aparecen en cada monitor.
# =========================================================================== #
screens = [
    Screen(
        # --- Definición de la Barra ---
        top=bar.Bar( # 'top' o 'bottom' para la posición
            [
                # --- Lado Izquierdo ---
                widget.Spacer(length=5),
                widget.GroupBox(
                    font="JetBrainsMono Nerd Font Bold", # Fuente específica para grupos
                    fontsize=14,
                    margin_y=3,                 # Margen vertical
                    margin_x=0,                 # Margen horizontal
                    padding_y=5,                # Relleno vertical
                    padding_x=5,                # Relleno horizontal
                    borderwidth=3,              # Grosor del borde
                    active=colors["fg"],        # Color texto grupos activos
                    inactive=colors["gray"],      # Color texto grupos inactivos
                    rounded=False,              # Bordes redondeados (True/False)
                    highlight_method="block",   # Método de resaltado: "block", "border", "text"
                    # Colores de resaltado (dependen de highlight_method)
                    this_current_screen_border=colors["blue"],    # Color para grupo actual en pantalla actual
                    this_screen_border=colors["gray"],            # Color para otros grupos en pantalla actual
                    other_current_screen_border=colors["bg"],     # Color si tienes multi-monitor
                    other_screen_border=colors["bg"],             # Color si tienes multi-monitor
                    foreground=colors["fg"],
                    background=colors["bg"]
                ),
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"]), # Separador
                widget.CurrentLayoutIcon(scale=0.65), # Icono del layout actual
                widget.CurrentLayout(foreground=colors["cyan"], padding = 5), # Nombre del layout actual
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"]),
                widget.WindowName(           # Nombre de la ventana activa
                    foreground=colors["cyan"],
                    format='{name}',
                    max_chars=40,             # Limitar longitud
                    empty_group_string="Escritorio" # Texto si no hay ventanas
                ),

                # --- Centro (widget separador que ocupa espacio) ---
                widget.Spacer(), # Empuja los siguientes widgets a la derecha

                # --- Lado Derecho (Widgets del Sistema) ---
                widget.Systray(padding=5), # Bandeja del sistema
                widget.Sep(linewidth=0, padding=10),

                # Widget de Actualizaciones (ejemplo para Arch)
                widget.CheckUpdates(
                    distro="Arch",               # O "Arch_checkupdates" si tienes checkupdates instalado
                    display_format=" {updates}", # Icono + número de actualizaciones (requiere Nerd Font)
                    no_update_string=" 0",       # Texto si no hay actualizaciones
                    colour_have_updates=colors["yellow"], # Color si hay actualizaciones
                    colour_no_updates=colors["green"],   # Color si no hay actualizaciones
                    update_interval=1800,         # Intervalo de chequeo (en segundos)
                    execute="alacritty -e sudo pacman -Syu", # Comando al hacer click (opcional)
                    padding=5
                ),
                widget.Sep(linewidth=0, padding=10),

                # Icono y % de CPU
                widget.TextBox(text="", foreground=colors["green"], fontsize=16, padding=0), # Icono
                widget.CPU(
                    format='{load_percent:.0f}%', # Formato: % de carga
                    foreground=colors["green"],
                    padding = 5
                ),
                widget.Sep(linewidth=0, padding=10),

                # Icono y Memoria Usada
                widget.TextBox(text="", foreground=colors["blue"], fontsize=16, padding=0), # Icono
                widget.Memory(
                    format='{MemUsed:.1f}{mm}', # Formato: Memoria usada con 1 decimal + unidad (G, M)
                    foreground=colors["blue"],
                    padding = 5,
                    measure_mem='G'           # Medir en Gigabytes
                ),
                widget.Sep(linewidth=0, padding=10),

                # Icono y Red (¡¡¡ CAMBIA 'wlan0' !!!)
                widget.TextBox(text="", foreground=colors["orange"], fontsize=16, padding=0), # Icono
                widget.Net(
                    interface="wlan0",        # <<< ¡¡¡ CAMBIA ESTO POR TU INTERFAZ !!! (ej: eth0, enp2s0, wlp3s0)
                    format='{down}↓↑{up}',    # Formato: Bajada / Subida
                    foreground=colors["orange"],
                    padding=5,
                    use_bits=True             # Opcional: Mostrar en bits en vez de Bytes
                ),
                widget.Sep(linewidth=0, padding=10),

                # Icono y Fecha
                widget.TextBox(text="", foreground=colors["magenta"], fontsize=16, padding=0), # Icono
                widget.Clock(
                    format="%d/%m/%Y",        # Formato: DD/MM/YYYY
                    foreground=colors["magenta"],
                    padding = 5
                ),
                # Icono y Hora
                widget.TextBox(text="", foreground=colors["magenta"], fontsize=16, padding=0), # Icono
                widget.Clock(
                    format="%H:%M",           # Formato: HH:MM (24h)
                    foreground=colors["magenta"],
                    padding = 5
                ),

                # Espacio final antes del borde
                widget.Spacer(length=5),

                # Opcional: Botón de Salir Rápido
                # widget.QuickExit(
                #    default_text='', # Icono de Power
                #    foreground=colors["red"],
                #    fontsize=16,
                #    countdown_format='[{}]'
                # ),
                # widget.Spacer(length=5),

            ],
            # --- Propiedades de la Barra ---
            26,                     # Altura de la barra en píxeles
            background=colors["bg"],# Color de fondo
            opacity=0.95            # Opacidad (0.0 a 1.0, necesita 'picom' corriendo)
            # border_width=[2, 0, 2, 0],  # Ancho de bordes: [Arriba, Derecha, Abajo, Izquierda]
            # border_color=["ff00ff", "000000", "ff00ff", "000000"] # Colores de los bordes
        ),
        # --- Fondo de pantalla para esta pantalla (opcional, si no usas feh/nitrogen) ---
        # wallpaper='~/Pictures/Wallpapers/ghibli.jpg',
        # wallpaper_mode='fill', # 'fill' o 'stretch'
    ),
]

# =========================================================================== #
# === RATÓN (Mouse Bindings) ===
# Comportamiento para ventanas flotantes principalmente.
# =========================================================================== #
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# =========================================================================== #
# === OTRAS CONFIGURACIONES ===
# =========================================================================== #
dgroups_key_binder = None       # No usar keybinder para dgroups
dgroups_app_rules = []          # Sin reglas específicas para aplicaciones y grupos al inicio
follow_mouse_focus = True       # El foco sigue al ratón al moverlo entre ventanas
bring_front_click = False       # Hacer click en una ventana no la trae al frente automáticamente
floats_kept_above = True        # Las ventanas flotantes permanecen sobre las de mosaico
cursor_warp = False             # El cursor no salta automáticamente a la ventana activa

floating_layout = layout.Floating( # Configuración del layout flotante por defecto
    border_focus=colors["magenta"], # Borde para ventanas flotantes activas
    border_normal=colors["gray"],   # Borde para ventanas flotantes inactivas
    border_width=2,
    float_rules=[
        # Reglas por defecto de Qtile para ventanas que DEBEN ser flotantes
        *layout.Floating.default_float_rules,
        # Añade reglas personalizadas si es necesario (usa 'xprop' para encontrar WM_CLASS o title)
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),      # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),     # gitk
        Match(title="pinentry"),         # GPG key password entry
        # Match(wm_class="tu_aplicacion_flotante"), # Ejemplo
    ]
)
auto_fullscreen = True             # Permitir que las aplicaciones se pongan en pantalla completa automáticamente
focus_on_window_activation = "smart" # Comportamiento del foco al activar ventanas ("smart", "focus", "never")
reconfigure_screens = True         # Intentar reconfigurar pantallas si cambian (ej. conectar monitor)

# Si algunas aplicaciones (ej. Steam) minimizan al perder foco, ¿respetarlo?
auto_minimize = True

# Configuración específica para Wayland (Ignorar si usas Xorg)
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

# Nombre interno del WM. Necesario para compatibilidad con algunas apps Java antiguas.
# No cambiar a menos que sepas lo que haces.
wmname = "LG3D"

# ======================== FIN DE LA CONFIGURACIÓN ========================= #