# HyprNav

![HyprNav Demo](gif/hyprnav-show.gif)

A modern window navigator for Hyprland with advanced navigation capabilities.

## Features

- Fast window switching
- Customizable keybindings
- Intuitive interface
- Low resource consumption

## Installation

Add the following rule to your Hyprland configuration file hyprland.conf

```bash
# Rule for hyprnav
windowrulev2 = float,class:hyprnav
```

```bash
# Clone the repository

pip install hyprnav

# or if using uv
uv venv
source .venv/bin/activate
uv pip install hyprnav
```

## Usage

```bash
# Basic usage
hyprnav
```

## Configuration

Configuration is done through a YAML file located at `~/.config/hyprnav/config.yaml`.

## Development

```bash
# Setup development environment
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

## License

MIT
