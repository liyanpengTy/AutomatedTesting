# -*- coding: utf-8 -*-
# @File    :screenshot
# @Date    :2023/3/28 8:32
# @Name    :LYP

import os
import time
from PIL import ImageGrab
from Common.initPath import screen_dir

def screenshot(name, fileName):
    """ 封装截图 """
    _today = time.strftime("%Y%m%d")
    _screen_path = os.path.join(screen_dir, _today + "_" + fileName)
    t = time.time()
    png = ImageGrab.grab()
    if not os.path.exists(_screen_path):
        os.makedirs(_screen_path)
    image_name = os.path.join(_screen_path, name)
    png.save('%s_%s.png' % (image_name, str(round(t * 1000))))


# screenshot("name", "fileName")