from PIL import Image  # TASK 1
import numpy as np


def m_more_contrasting(img_path, new_name):
    img = Image.open(img_path)
    data = np.array(img)
    updated_data = ((data-data.min())/(data.max()-data.min())*255).astype(np.uint8)
    res_img = Image.fromarray(updated_data)
    res_img.save("lunar_images/"+new_name)


m_more_contrasting("lunar_images/lunar01_raw.jpg", "lunar01_updt.jpg")
m_more_contrasting("lunar_images/lunar02_raw.jpg", "lunar02_updt.jpg")
m_more_contrasting("lunar_images/lunar03_raw.jpg", "lunar03_updt.jpg")