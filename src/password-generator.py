#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lucas'


import sys

from workflow import Workflow


def main(wf):
    from subprocess import check_output

    # Do stuff here ...
    out_bytes = check_output('/usr/local/bin/sf-pwgen -c 10', shell=True)

    for line in str(out_bytes).split('\n'):
        wf.add_item(title=line,
                    arg=line,
                    valid=True,
                    )

    # Send output to Alfred
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
