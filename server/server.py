import pyautogui, cloudlink, configparser, time

def clNewPacket(packet):
    if packet['cmd'] == 'gvar':
        if packet['name'] == 'keydown':
            pyautogui.keyDown(packet['val'])
        if packet['name'] == 'keyup':
            pyautogui.keyUp(packet['val'])
    if packet['cmd'] == 'ulist':
        if 'admin' in packet['val'].split(';'):
            cl.sendPacket({'cmd': 'gvar', 'val': int(config.get('VideoSettings', 'Width')) / int(config.get('VideoSettings', 'Accuracy')), 'name': 'w'})
            cl.sendPacket({'cmd': 'gvar', 'val': int(config.get('VideoSettings', 'Height')) / int(config.get('VideoSettings', 'Accuracy')), 'name': 'h'})
            
def clConnect():
    cl.sendPacket({'cmd': 'setid', 'val': 'server'})
    cl.sendPacket({'cmd': 'gvar', 'val': 'hello world', 'name': 'message'})
        


def clError(error):
    print(error)

def make2Chars(string):
    return '%s%s' % ('0' if len(string) == 1 else '', string)


def createOutput(w, h, x, y, a):
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    screenshot = screenshot.convert('RGB')

    colours = []

    for cx in range(w):
        if cx % a == 0:
            for cy in range(h):
                if cy % a == 0:
                    rgb = screenshot.getpixel((cx, cy))
                    colours.append(make2Chars(str(hex(rgb[0]))[2:]) + make2Chars(str(hex(rgb[1]))[2:]) + make2Chars(str(hex(rgb[2]))[2:]))
                    # Converts the red, green and blue to hexidecimals, converts the hex to a string, makes sure the hex is 2 characters long and combines them to make a hex code
    
    return ''.join(colours)

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == '__main__':
    cl = cloudlink.CloudLink()
    try:
        cl.client(config.get('ServerSettings', 'IP'),
                  on_new_packet = clNewPacket,
                  on_connect = clConnect,
                  on_error = clError)

        while cl.mode == 2: # Some other spaghetti code to keep the script running while the connection is live
            startTime = time.time()
            image = createOutput(
                int(config.get('VideoSettings', 'Width')),
                int(config.get('VideoSettings', 'Height')),
                int(config.get('VideoSettings', 'X')),
                int(config.get('VideoSettings', 'Y')),
                int(config.get('VideoSettings', 'Accuracy'))
            )
            cl.sendPacket({'cmd': 'gvar', 'val': image, 'name': 'image'})
            sleepTime = 0.5 - (time.time() - startTime)
            if sleepTime > 0:
                # time.sleep(sleepTime)
                pass
    except KeyboardInterrupt:
        cl.stop()



