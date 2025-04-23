# Hyprnav

<p align="center">
<img src="https://github.com/antrax2024/hyprnav/blob/main/gif/hyprnav-show.gif?raw=true" alt="Hyprnav Logo">
</p>

<div align="center">
  <span>
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/dockmate">
    <img alt="AUR Version" src="https://img.shields.io/aur/version/dockmate">
    <img src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fantrax2024%2Fdockmate%2Frefs%2Fheads%2Fmain%2Fpyproject.toml" alt="Python Version" />
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/antrax2024/dockmate">
    <img alt="PyPI - License" src="https://img.shields.io/pypi/l/dockmate">
  </span>
</div>

A modern and customizable workspace navigation effect for Hyprland.

## Description

Hyprnav provides smooth visual transitions when navigating between workspaces in Hyprland. It enhances the user experience by adding polished animations and optional sound effects.

## Features

- Smooth workspace transition animations
- Customizable visual effects
- Optional sound effects for workspace transitions
- Easy configuration through YAML files

## Installation

### From PyPI

```bash
pip install hyprnav
```

### From Source

```bash
git clone https://github.com/antrax2024/hyprnav.git
cd hyprnav
uv venv
uv pip install -e .
```

### Arch Linux (AUR)

Using yay:

```bash
yay -S hyprnav
```

Using paru:

```bash
paru -S hyprnav
```

## Configuration

Hyprnav automatically creates configuration files in `~/.config/hyprnav` when first run. These files include:

- `config.yaml`: Main configuration file
- `themes/`: Directory containing theme configurations

### Enabling Sound Effects

To enable sound effects for workspace transitions, edit your `~/.config/hyprnav/config.yaml` file:

```yaml
sound:
  enabled: true
  volume: 0.5 # Range from 0.0 to 1.0
```

## Usage

```bash
hyprnav --help  # Show all available options
hyprnav         # Start with default settings
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/antrax2024/hyprnav).

To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
