import cv2, numpy, time
from PIL import ImageGrab
from screeninfo import get_monitors

def take_screenshot(all=False):
    
    screenshot = ImageGrab.grab(all_screens=all)
    converted = numpy.array(screenshot)
    converted = cv2.cvtColor(converted, cv2.COLOR_BGR2RGB)
    t = cv2.selectROI(converted, False)
    x, y, w, h = t

    if x + y + w + h != 0:
        screenshot = screenshot.crop((x, y, x + w, y + h))
        cv2.destroyWindow('ROI selector')
        screenshot.show()
        screenshot.save(f'{Time}.png', 'PNG') 

    else:
        cv2.destroyWindow('ROI selector')
        time.sleep(0.2)
        take_screenshot(many_monitors)
        screenshot.save(f'{Time}.png', 'PNG') 

many_monitors = False
only_one_monitor = True
Time = time.strftime('%H-%M-%S')

if only_one_monitor:
    take_screenshot()   
else:
    if len(get_monitors()) == 1:
        take_screenshot()
    else:
        many_monitors = True
        take_screenshot(many_monitors)