# hyprnav

![hyprnav](gif/hyprnav-show.gif)

<div align="center">
  <span>
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/hyprnav">
    <img alt="AUR Version" src="https://img.shields.io/aur/version/hyprnav">
    <img alt="Python Version from PEP 621 TOML" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fantrax2024%2Fhyprnav%2Frefs%2Fheads%2Fmain%2Fpyproject.toml">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/antrax2024/hyprnav">
    <img alt="GitHub License" src="https://img.shields.io/github/license/antrax2024/hyprnav">
  </span>
</div>

A modern and customizable workspace navigation effect for Hyprland.

## Description

hyprnav provides smooth visual transitions when navigating between workspaces in Hyprland. It enhances the user experience by adding polished animations and optional sound effects.

## Features

- Beautiful and smooth visual transition effect between Hyprland workspaces
- Enable or disable optional sound for workspace transitions
- Easy configuration through YAML files

## Installation

### From PyPI

```bash
pip install hyprnav # if you use pip
uv pip install hyprnav # or with uv
```

### Arch Linux (AUR)

```bash
yay -S hyprnav # with yay
paru -S hyprnav # with paru
```

## Usage

Start with default settings.

```bash
hyprnav
```

## Configuration

Hyprnav automatically creates configuration files in `~/.config/hyprnav` when first run. These files include:

- `config.yaml`: Main configuration file
- `style.css`: Customizable stylesheet for the application appearance

### Configuration Parameters

The `config.yaml` file contains the following configurable parameters:

#### Main Window

```yaml
main_window:
  width: 450 # Width of the transition window in pixels
  height: 70 # Height of the transition window in pixels
  duration: 400 # Duration of transition animation in milliseconds
```

- `width`: Controls the horizontal size of the animation window (default: 450px)
- `height`: Controls the vertical size of the animation window (default: 70px)
- `duration`: Sets how long the transition animation plays (default: 400ms)

#### Sound Settings

```yaml
sound:
  enabled: false # Set to true to enable sound effects
  file: "/path/to/your/sound/file.wav" # Path to the sound file
```

- `enabled`: Toggle sound effects on/off (default: false)
- `file`: Absolute path to the sound file that will play during transitions (WAV format recommended)

### Customizing Appearance

You can customize the appearance of Hyprnav by editing the `~/.config/hyprnav/style.css` file. This file allows you to change colors, fonts, sizes, and other visual aspects of the application.

#### Default Stylesheet Elements

```css
/* Main window styling - controls the background */
#MainWindow,
#centralWidget {
  background-color: rgba(0, 0, 0, 0.849); /* Dark transparent background */
}

/* Fixed label styling - used for application title */
#fixedLabel {
  color: #00ffd0; /* Teal/cyan color */
  font-size: 36px;
  font-weight: bold;
  font-family: "Hack Nerd Font Propo", monospace;
}

/* Workspace label styling - displays workspace information */
#workspaceLabel {
  color: #00ffd0; /* Teal/cyan color */
  font-size: 26px;
  font-family: "Hack Nerd Font Propo", monospace;
}
```

You can customize these elements to match your desktop theme:

- Change the background transparency by adjusting the alpha value in `rgba(0, 0, 0, 0.849)`
- Modify text colors by changing the color values (e.g., `#00ffd0`)
- Adjust font sizes and families to your preference
- Add additional CSS rules to further customize the appearance

After making changes to the stylesheet, restart Hyprnav for the changes to take effect.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
