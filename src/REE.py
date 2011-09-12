#!/usr/bin/env python

import os
import signal
import sys
import time


def ttywidth():

  f = os.popen('tput cols', 'r')
  width = int(f.read())
  f.close()
  return width


def update_width(signum, frame):
  
  global width
  
  width = ttywidth()


def sigexit(signum, frame):

  sys.stdout.write('\033[?25h')
  os.system('stty echo')


def main():

  global width

  width = ttywidth()
  signal.signal(signal.SIGWINCH, update_width)

  x = 1
  d = 1
  REE = ['>_>', 'v_v', '<_<', '^_^']
  sys.stdout.write('\033[?25l')
  os.system('stty -echo')
  while True:
    ree = REE.pop(0)
    REE.append(ree)
    sys.stdout.write("\033[2K\033[%dG%s" % (x, ree))
    sys.stdout.flush()
    x += d
    if x <= 1 or x >= width - 2:
      d *= -1
      if x > 1:
        x = width - 2
    time.sleep(0.25)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
  except Exception, e:
    sigexit(None, None)
    raise e
  sigexit(None, None)
