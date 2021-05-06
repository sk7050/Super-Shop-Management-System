
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
def make_qr(content):
        qrcode_img = qrcode.make(content)
        canvas = Image.new('RGB', (450, 450), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{content}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        return canvas,buffer,fname 