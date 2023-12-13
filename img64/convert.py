import io
import base64
import numpy as np
from PIL import Image
from typing import Union, Literal

def image_to_base64(img: Union[Image.Image, np.ndarray]) -> str :
    if isinstance(img, np.ndarray) :
        img = Image.fromarray(img)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")

    img_bytes = buffer.getvalue()
    img_b64 = base64.b64encode(img_bytes)
    img_b64_utf8 = img_b64.decode("utf-8")

    return img_b64_utf8

def base64_to_image(img_b64_utf8: str, type: Literal["pil", "numpy"]) -> Union[Image.Image, np.ndarray] :
    assert type in ["pil", "numpy"], "Expected type 'pil' or 'numpy'"
    img_bytes = base64.b64decode(img_b64_utf8)
    buffer = io.BytesIO(img_bytes)
    img = Image.open(buffer)

    if type == 'numpy' :
        img = np.array(img)

    return img