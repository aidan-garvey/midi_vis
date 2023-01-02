import time

import mido

mido.set_backend('mido.backends.rtmidi')

inport: mido.ports.BaseInput = None
for dev in mido.get_input_names():
    if dev.lower().find('t-8') >= 0:
        inport = mido.open_input(dev)

if inport is None:
    print('Error: MIDI input device not found')
    exit()
else:
    print(inport)

outport: mido.ports.BaseOutput = None
for dev in mido.get_output_names():
    if dev.lower().find('t-8') >= 0:
        outport = mido.open_output(dev)

if outport is None:
    print('Error: MIDO output device not found')
    exit()
else:
    print(outport)

active_sense = mido.Message('active_sensing')

outport.send(mido.Message('start'))

try:
    while True:
        msg = inport.poll()
        if msg is not None:
            print(msg)
        outport.send(active_sense)
        time.sleep(0.1)
        
except:
    print('Bye!')
