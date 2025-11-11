from cookiecutter.main import cookiecutter
from importlib import resources


def main():
    template_root = resources.files("gmod_binmod_template").joinpath("template")
    cookiecutter(str(template_root))
