import time
import os
import sys
import subprocess

objects = '["elmers_washable_no_run_school_glue","expo_dry_erase_board_eraser","laugh_out_loud_joke_book","crayola_24_ct"]'

for i in range(15):
  input("Press to take picture {}".format(i));
  bashcommand = 'rosservice call /save_images {} 0 {}'.format(objects, i)
  print(bashcommand.split());
  p = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
  o,e = p.communicate()
  print(o, e)
  
  
