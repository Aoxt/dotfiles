# ~/.config/qtile/src/themes.py

"""
Colección de paletas de colores para Qtile.
Cada diccionario debe tener (al menos) las claves:
'foreground', 'background', 'alt_background', 'disabled', 'accent',
'focus_stack_main', 'focus_stack_alt',
'layout_margin', 'border_width_layout'
"""

catppuccin_mocha = {
    'name': 'Catppuccin Mocha',
    'foreground': '#cdd6f4',
    'background': '#1e1e2e',
    'alt_background': '#181825',
    'disabled': '#494a66',
    'accent': '#89b4fA', # Blue
    'red': '#f38ba8',
    'green': '#a6e3a1',
    'yellow': '#f9e2af',
    'blue': '#89b4fa',
    'magenta': '#f5c2e7',
    'cyan': '#89dceb',
    'white': '#a6adc8',
    # --- Claves para border_focus_stack ---
    'focus_stack_main': '#89b4fA',
    'focus_stack_alt': '#f38ba8',
    # ------------------------------------
    # --- Tamaños de Layout ---
    'layout_margin': 8,           # Espaciado entre ventanas
    'border_width_layout': 2,     # Grosor del borde de ventana
    # ------------------------
}

catppuccin_macchiato = {
    'name': 'Catppuccin Macchiato',
    'foreground': '#cad3f5',
    'background': '#24273a',
    'alt_background': '#1e2030',
    'disabled': '#4c5065',
    'accent': '#8aadf4', # Blue
    'red': '#ed8796',
    'green': '#a6da95',
    'yellow': '#eed49f',
    'blue': '#8aadf4',
    'magenta': '#f5bde6',
    'cyan': '#8bd5ca',
    'white': '#b8c0e0',
    # --- Claves para border_focus_stack ---
    'focus_stack_main': '#8aadf4',
    'focus_stack_alt': '#ed8796',
    # ------------------------------------
    # --- Tamaños de Layout ---
    'layout_margin': 8,
    'border_width_layout': 2,
    # ------------------------
}

catppuccin_frappe = {
    'name': 'Catppuccin Frappe',
    'foreground': '#c6d0f5',
    'background': '#303446',
    'alt_background': '#292c3c',
    'disabled': '#51576d',
    'accent': '#8caaee', # Blue
    'red': '#e78284',
    'green': '#a6d189',
    'yellow': '#e5c890',
    'blue': '#8caaee',
    'magenta': '#f4b8e4',
    'cyan': '#81c8be',
    'white': '#a5adce',
    # --- Claves para border_focus_stack ---
    'focus_stack_main': '#8caaee',
    'focus_stack_alt': '#e78284',
    # ------------------------------------
    # --- Tamaños de Layout ---
    'layout_margin': 8,
    'border_width_layout': 2,
    # ------------------------
}

tokyo_night_night = {
    'name': 'Tokyo Night - Night',
    'foreground': '#c0caf5',
    'background': '#1a1b26',
    'alt_background': '#15161e',
    'disabled': '#414868',
    'accent': '#7aa2f7', # Blue
    'red': '#f7768e',
    'green': '#9ece6a',
    'yellow': '#e0af68',
    'blue': '#7aa2f7',
    'magenta': '#bb9af7',
    'cyan': '#7dcfff',
    'white': '#a9b1d6',
    # --- Claves para border_focus_stack ---
    'focus_stack_main': '#7aa2f7',
    'focus_stack_alt': '#bb9af7',
    # ------------------------------------
    # --- Tamaños de Layout ---
    'layout_margin': 8,
    'border_width_layout': 2,
    # ------------------------
}

tokyo_night_storm = {
    'name': 'Tokyo Night - Storm',
    'foreground': '#c0caf5',
    'background': '#24283b',
    'alt_background': '#1d202f',
    'disabled': '#414868',
    'accent': '#7aa2f7', # Blue
    'red': '#f7768e',
    'green': '#9ece6a',
    'yellow': '#e0af68',
    'blue': '#7aa2f7',
    'magenta': '#bb9af7',
    'cyan': '#7dcfff',
    'white': '#a9b1d6',
    # --- Claves para border_focus_stack ---
    'focus_stack_main': '#7aa2f7',
    'focus_stack_alt': '#bb9af7',
    # ------------------------------------
    # --- Tamaños de Layout ---
    'layout_margin': 8,
    'border_width_layout': 2,
    # ------------------------
}

tokyo_night_moon = {
    'name': 'Tokyo Night - Moon',
    'foreground': '#c8d3f5',
    'background': '#222436',
    'alt_background': '#1b1d2b',
    'disabled': '#444a73',
    'accent': '#82aaff', # Blue
    'red': '#f7768e',
    'green': '#9ece6a',
    'yellow': '#e0af68',
    'blue': '#82aaff',
    'magenta': '#bb9af7',
    'cyan': '#7dcfff',
    'white': '#c8d3f5',
    # --- Claves para border_focus_stack ---
    'focus_stack_main': '#82aaff',
    'focus_stack_alt': '#bb9af7',
    # ------------------------------------
    # --- Tamaños de Layout ---
    'layout_margin': 8,
    'border_width_layout': 2,
    # ------------------------
}

rose_pine = {
    'name': 'Rosé Pine',
    'foreground': '#e0def4',
    'background': '#191724',
    'alt_background': '#1f1d2e',
    'disabled': '#6e6a86',
    'accent': '#c4a7e7', # Purple
    'red': '#eb6f92',   # Love
    'green': '#9ccfd8', # Pine
    'yellow': '#f6c177', # Gold
    'blue': '#31748f',   # Foam
    'magenta': '#c4a7e7', # Iris (mismo que accent)
    'cyan': '#ebbcba',   # Rose
    'white': '#e0def4',   # Text
    # --- Claves para border_focus_stack ---
    'focus_stack_main': '#c4a7e7',
    'focus_stack_alt': '#eb6f92',
    # ------------------------------------
    # --- Tamaños de Layout ---
    'layout_margin': 8,
    'border_width_layout': 2,
    # ------------------------
}

# --- Puedes añadir más temas aquí ---