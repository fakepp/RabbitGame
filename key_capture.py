from msvcrt import getch


class KeyCapture:
    def __init__(self):
        return

    def input(self):
        key = ord(getch())
        if key == 3:
            return 'ESC'
        if key >= 48 and key <= 57:
            return str(key-48)
        if key == 27: #ESC
            return 'ESC'
            #exit()
        elif key == 13: #Enter
            return 'GO'
        elif key == 32: #Space
            return 'S'
        elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
            key = ord(getch())
            if key == 80: #Down arrow
                return 'D'
            elif key == 72: #Up arrow
                return 'U'
            elif key == 75: #Left arrow
                return 'L'
            elif key == 77: #Right arrow
                return 'R'
            elif key == 83: #Right arrow
                return 'DEL'
        #print('done')



if __name__ == "__main__":
    keyc = KeyCapture()
    keyc.input()