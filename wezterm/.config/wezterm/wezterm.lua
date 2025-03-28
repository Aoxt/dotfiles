-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- Configurando el esquema de color
config.color_scheme = 'Kasugano'

-- Configurando el shell predeterminado a bash
config.default_prog = { '/bin/bash', '-l' }

-- y finalmente, retorna la configuración a wezterm
return config