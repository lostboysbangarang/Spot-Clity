#!/usr/bin/env python3

from cli.spotify import cli
def boo(bees):
    bs = ''
    for i in range(bees):
        bs = f'\b' + bs;
    return bs;
print(f'\tVersion\t\tSpot-Clity\v{boo(22)}v0.69', end = None)

if __name__ == '__main__':
    cli()