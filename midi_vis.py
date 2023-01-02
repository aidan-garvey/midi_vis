
import mido

mido.set_backend('mido.backends.rtmidi')

inport: mido.ports.BaseInput = None
for dev in mido.get_input_names():
    if dev.lower().find('t-8') >= 0:
        inport = mido.open_input(dev)

if inport is None:
    print('Error: MIDI input device not found')
    exit()

try:
    while True:
        msg = inport.receive()
        print(msg)
except:
    print('Bye!')
