
git clone https://github.com/MikeySoftNL/powerline-shell-segments.git

# Fonts
The Powerline leverages Glyphs from Nerd Font, to be able to see them install a Nerd Font using the following methods.

For Windows / WSL, make sure you install, configure and use the Windows Terminal from the Windows App Store to connect to the WSL environment.


# MacOS
```console
brew tap homebrew/cask-fonts
brew cask install font-hack-nerd-font
```

# Windows
```Powershell
# In Powershell (as Administrator)
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Go-Mono.zip -OutFile Go-Mono.zip
Expand-Archive .\Go-Mono.zip -DestinationPath Go-Mono
```
Install Fonts by double clicking each, or go to Settings → Fonts and drag and drop

#### Configure Windows Terminal

```json
{
   "name": "Ubuntu-18.04",
   "fontFace": "GoMono Nerd Font"
}
```

# Powerline
```console
pip install powerline-shell \
mkdir -p ~/.config/powerline-shell && \
powerline-shell --generate-config > ~/.config/powerline-shell/config.json

#Edit config with editor of choice
Code ~/.config/powerline-shell/config.json
```

```json
example config
{
  "theme": "default",
  "segments": [
    "distri",
    "virtual_env",
    "terraform_version",
    "keybase",
    "eks",
    "environment",
    "aws_credentials",
    "azure_profile",
    "aws_profile",
    "ssh",
    "hg",
    "cwd",
    "git",
    "newline",
    "time",
    "root"
  ],
  "cwd": {
    "full_cwd": true
  },
  "vcs": {
    "show_symbol": true
  }
}
```

# Copy custom segments

Get the location of your installed pip package

```console
#pip show powerline-shell | grep Location
#Copy the custom segments (*.py) from this repo to

cp - powerline-shell-segments/*.py "$(pip show powerline-shell |  grep -oP '(?<=Location: ).*')/powerline_shell/segments"

cp -v powerline-shell-segments/themes/*.py "$(pip3 show powerline-shell | grep Location | awk -F ": " '{print $2}')/powerline_shell/themes/"
```



# Activate Powerline
```console
#Edit ~/.bashrc with editor of choice

Code ~/.bashrc

## Powerline_shell
function _update_ps1() {
    PS1=$(powerline-shell $?)
}

if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
fi
```

Or in Fish-Shell
```console
Code ~/.config/fish/config.fish

#Powerline-shell
function fish_prompt
    powerline-shell --shell bare $status
end

```

re-login
