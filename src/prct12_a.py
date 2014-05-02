#!/src/bin/python
#!ecoding: UTF-8

import os
import platform

def softwareinfo(): 
  softinfo={} 
  
  so=platform.platform()
  softinfo['S.O']=so
  
  pv=platform.python_version()
  softinfo['Python version']=pv
  
  pol=platform.python_build()
  softinfo['Python date']=pol[1]
  
  return softinfo

def CPUinfo():
# infofile on Linux machines:
  infofile = '/proc/cpuinfo'
  cpuinfo = {}
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
	name, value = [w.strip() for w in line.split(':')]
      except:
	continue
      if name == 'model name':
	cpuinfo['CPU type'] = value
      elif name == 'cache size':
	cpuinfo['cache size'] = value
      elif name == 'cpu MHz':
	cpuinfo['CPU speed'] = value + 'Hz'
      elif name == 'vendor_id':
	cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo

def savetofile(fn,d1,d2):
  f=open(fn,'w')
  f.write('Hardware\n')
  f.write('======\n')
  for clave in d1:
    f.write(str(clave))
    f.write('\t')
    f.write(str(d1[clave]))
    f.write('\n')
  f.write('\nsoftware\n')
  f.write('======\n')
  for clave in d2:
    f.write(str(clave))
    f.write('\t')
    f.write(str(d2[clave]))
    f.write('\n')
  f.close()
  return savetofile
    
  
if __name__ == '__main__':
  cpui=CPUinfo()
  si=softwareinfo()
  print cpui
  print si
  filename='InfoPortatil.txt'
  savetofile(filename,cpui,si)
  print'Información guardada en el fichero',filename

