# Zigzag by Kofi
# show a zig zig animation
# Press ctrl-C to stop the program
import time
indentsize = 0 # how many spaces to indent
DELAY = 0.08
while True: # the main program loop
    # Zig to the right 30 times:
    B = 20

    for i in range(B):
        indentsize = indentsize + 1
        print(' ' * indentsize + '########')
        time.sleep(DELAY)# pause for milliseconds
    # Zag to th left 20 times:
    for i in range(B):
        indentsize = indentsize - 1
        print(' ' * indentsize + '########')
        time.sleep(DELAY)  # pause for milliseconds
