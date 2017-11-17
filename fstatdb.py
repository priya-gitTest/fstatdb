"""fstatdb

Usage:
  fstatdb (start|remove) (update|verify) [<file>...]
  fstatdb (pause|resume) (update|verify) [<file>...]
  fstatdb processes
  fstatdb list

Options:
  -h --help  Show this screen.
  --version  Show version.
  start      Begin process of either updating or verifying specified files.
  remove     Forget process of either updating or verifying specified files.
  pause      Pause process for specified files.
  resume     Resume process for specified files.
  processes  Show processes.
  list       List files in the database.
"""

import logging

import docopt

def main(argv=None):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)-7s %(processName)-7s %(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S',
                        filename="fstatdb.log")

    arguments = docopt.docopt(__doc__, version="fstatdb 0.0.1", argv=argv)
    print(arguments)

if __name__ == '__main__':
    main()
