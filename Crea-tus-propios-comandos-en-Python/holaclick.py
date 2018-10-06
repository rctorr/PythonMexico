#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.argument("tunombre")
def hola(tunombre):
    """ Script que hace el holaclick.py TUNOMBRE """
    print("Hola {} desde click!".format(tunombre))


if __name__ == "__main__":
    hola()
