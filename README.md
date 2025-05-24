<!-- markdownlint-disable -->

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

A modern and customizable workspace navigation effect for [Hyprland](https://hyprland.org/).

## Description 📝

**hyprnav** provides smooth visual transitions when navigating between workspaces in [Hyprland](https://hyprland.org/). It enhances the user experience by adding polished animations and optional sound effects.

## Features ✨

- Beautiful and smooth visual transition effect between Hyprland workspaces
- Enable or disable optional sound for workspace transitions
- Easy configuration through YAML files
- Fully customizable with CSS
- Wayland native GUI with [Gtk4-Layer-Shell](https://github.com/wmww/gtk4-layer-shell)

## Installation 📦

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

## Usage ▶️

Start with default settings.

```bash
hyprnav
```

## Configuration ⚙️

**hyprnav** automatically creates configuration files in `~/.config/hyprnav` when first run. These files include:

- `config.yaml`: Main configuration file
- `style.css`: Customizable stylesheet for the application appearance

### Configuration Parameters

The `config.yaml` file contains the following configurable parameters:

### Configuration Parameters

The `config.yaml` file contains the following configurable parameters:

#### Main Window Settings

- **`width`**: Controls the width of the navigation window in pixels (default: 450)
- **`height`**: Controls the height of the navigation window in pixels (default: 70)
- **`duration`**: Sets the transition timeout duration in milliseconds (default: 300)
- **`spacing`**: Defines the vertical spacing between labels in pixels (default: 10)
- **`label`**: Customizes the text label displayed for workspace identification (default: "Workspace")

#### Sound Settings

- **`enabled`**: Boolean flag to enable or disable sound effects during workspace transitions (default: false)
- **`file`**: Absolute path to the audio file that will be played during transitions (default: "/home/user/Public/transition.wav")

#### Example Configuration

```yaml
main_window:
  width: 450
  height: 70
  duration: 300
  spacing: 10
  label: "Workspace"

sound:
  enabled: false
  file: "/home/user/Public/transition.wav"
```

**Note**: Make sure to update the sound file path to point to an existing audio file on your system if you want to enable sound effects.

### Customizing Appearance 🎨

You can customize the appearance of Hyprnav by editing the `~/.config/hyprnav/style.css` file. This file allows you to change colors, fonts, sizes, and other visual aspects of the application.

#### Stylesheet Elements

You can customize these elements to match your desktop theme:

- **`#main-window`**: The main container window with background color, border, border-radius, and padding properties
- **`#fixed-label`**: The "Workspace" text label with color, font-size, font-weight, and font-family styling
- **`#workspace-label`**: The workspace number/name label with color, font-size, and font-family properties

After making changes to the stylesheet, restart Hyprnav for the changes to take effect.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.
