from xml.etree import ElementTree as et

with open('ghIDA.kbxml', 'r') as stream:
    data = stream.read()

with open('ghIDA.kbxml', 'w') as stream:
    stream.write(et.canonicalize(data))
