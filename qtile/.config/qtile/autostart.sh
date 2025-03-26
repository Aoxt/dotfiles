#!/bin/sh
# =========================================================================== #
# Script de Autostart para Qtile                                              #
# ~/.config/qtile/autostart.sh                                                #
# Se ejecuta una vez al iniciar la sesión de Qtile.                          #
#                                                                             #
# Ubicación actual: Ciudad Guzmán, Jalisco, México                           #
# Fecha/Hora actual: Martes, 25 de Marzo de 2025, 6:38 PM CST                 #
# =========================================================================== #

# --- Función para ejecutar comando solo si no está ya corriendo ---
run() {
  if ! pgrep -f "$1" ;
  then
    "$@"&
  fi
}

# =========================================================================== #
# === CONFIGURACIÓN DE PANTALLAS (XRANDR) ===                             #
# =========================================================================== #
# Añade una pequeña pausa para dar tiempo a que el sistema esté listo.
sleep 1

# --- Configuración de Pantallas (XRANDR) ---
# Añade una pequeña pausa para dar tiempo a que el sistema esté listo.
sleep 1

echo "[Autostart] Aplicando configuración de xrandr..." >> ~/.config/qtile/autostart.log # Log (opcional)
# Configura DP-0 (144Hz, izquierda) y DP-2 (Primario, 239.76Hz, derecha)
xrandr --output DP-0 --mode 1920x1080 --rate 144.00 --pos 0x0 --output DP-2 --primary --mode 1920x1080 --rate 239.76 --pos 1920x0 &

echo "[Autostart] Aplicando configuración de xrandr..." >> ~/.config/qtile/autostart.log # Log (opcional)
# PEGA TU COMANDO XRANDR COMPLETO Y CORRECTO AQUÍ, TERMINANDO CON '&':
# Ejemplo:
# xrandr --output eDP-1 --primary --mode 1920x1080 --rate 60.00 --output HDMI-1 --off &



# =========================================================================== #
# === RESTO DE PROGRAMAS DE AUTOSTART ===                                   #
# =========================================================================== #

# --- Compositor (Para transparencias, sombras, etc.) ---
killall -q picom
while pgrep -u $UID -x picom >/dev/null; do sleep 1; done
picom -b --config ~/.config/picom/picom.conf &

# --- Establecer Fondo de Pantalla ---
WALLPAPER_PATH="/home/aoxt/Pictures/Wallpapers/ghibli.jpg"
if [ -f "$WALLPAPER_PATH" ]; then
  # Usa feh después de que xrandr haya configurado las pantallas
  (sleep 2 && feh --bg-scale "$WALLPAPER_PATH") &
else
  xsetroot -solid "#2E3440"
  echo "[Autostart] Wallpaper no encontrado en $WALLPAPER_PATH, se estableció color sólido." >> ~/.config/qtile/autostart.log
fi

# --- Servidor de Notificaciones ---
killall -q dunst
dunst &

# --- Applet de Network Manager ---
run nm-applet

# --- Icono/Control de Volumen en la bandeja del sistema ---
run volumeicon

# --- Agente de Autenticación Polkit ---
POLKIT_AGENT_GNOME="/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1"
POLKIT_AGENT_LXDE="/usr/bin/lxpolkit"
if [ -x "$POLKIT_AGENT_GNOME" ]; then
  run "$POLKIT_AGENT_GNOME"
elif [ -x "$POLKIT_AGENT_LXDE" ]; then
  run "$POLKIT_AGENT_LXDE"
else
  echo "[Autostart] Advertencia: No se encontró agente de Polkit (GNOME o LXDE)." >> ~/.config/qtile/autostart.log
fi

# --- Otros programas que desees iniciar automáticamente ---
run copyq
# run redshift-gtk &
# numlockx on &

# -----------------------------------------------------------
echo "[Autostart] Script completado." >> ~/.config/qtile/autostart.log
# notify-send "Qtile Autostart" "Programas iniciados" -i preferences-system

# ======================== FIN DEL SCRIPT ========================= #