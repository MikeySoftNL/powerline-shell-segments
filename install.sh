#!/bin/bash

# exit upon failure
set -e
# colors
RED="\033[1;91m"
CYAN="\033[1;36m"
GREEN="\033[1;32m"
WHITE="\033[1;38;5;231m"
RESET="\n\033[0m"

# functions
log_std() { echo -e "${CYAN}==> ${WHITE}${1}${RESET}"; }
log_err() { echo -e "${RED}==> ${WHITE}${1}${RESET}"; }

#Segments
log_std "Copying ${GREEN}custom segments"
cp -v *.py $(pip3 show powerline-shell | grep Location | awk -F ": " '{print $2}')/powerline_shell/segments --force

#Themes
echo
log_std "Copying ${GREEN}custom themes"
cp -v themes/*.py $(pip3 show powerline-shell | grep Location | awk -F ": " '{print $2}')/powerline_shell/themes --force

#Config
echo
log_std "${GREEN} configuration"
config="$HOME/.config/powerline-shell/config.json"
if test -f "$config"; then
    read -p "Do you want to replace current configuration file? (Y/n): " replace_config
    if [ "$replace_config" == "Y" ]; then
        log_std "Creating backup of current config \n    ${GREEN}($config) \n    to ${CYAN}($config.bck)";
        mv $config $config.bck --force
        log_std "Copying ${GREEN}config.json ${WHITE}to $config"
        cp ./config.json $config --force
    fi
fi

log_std "$GREEN Done."
