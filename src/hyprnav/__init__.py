import os


def main() -> None:
    try:
        del os.environ["QT_STYLE_OVERRIDE"]
    except KeyError as e:
        print(f"KeyError: {e}")
    # from .listen import listen
    # listen()
    from .click import cli

    cli()
