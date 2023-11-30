# Based on https://foto-jan-lorenz.de/2019/07/fujifilm-profile-fuer-alle/
# Original Github repository https://github.com/lichtzeichner/FujifilmCameraProfiles
# Python version

import xml.etree.ElementTree as ET

# 
camera = 'Sony ILCE-7CM2'

def generate_profile(name, path):
  global camera
  standard_profile = 'AdobeStandardXML/' + camera + ' Adobe Standard.xml'
  fuji_profile = 'FujiXML/' + path + '.xml'
  camera_profile = 'Output/' + camera + ' ' + name + '.xml'
  mytree = ET.parse(standard_profile)
  myroot = mytree.getroot()
  for item in myroot.iter('ProfileName'):
       item.text = name
  for item in myroot.iter('ProfileLookTableEncoding'):
       item.text = '1'
  for item in myroot.iter('DefaultBlackRender'):
       item.text = '1'
  elems_to_delete = [child for child in myroot if (child.tag == 'LookTable' or child.tag == 'ToneCurve')]
  for elem in elems_to_delete:
      myroot.remove(elem)
  src_tree = ET.parse(fuji_profile)
  src_tasks = src_tree.findall('.//LookTable')
  for src_element in src_tasks:
      myroot.append(src_element)
  src_tasks = src_tree.findall('.//ToneCurve')
  for src_element in src_tasks:
      myroot.append(src_element)  
  mytree.write(camera_profile)

generate_profile('Fujifilm Classic Chrome', 'classic_chrome')
generate_profile('Fujifilm Provia', 'provia')
generate_profile('Fujifilm Astia', 'astia')
generate_profile('Fujifilm Velvia', 'velvia')