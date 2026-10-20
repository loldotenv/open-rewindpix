# PS135 App 圖示（minimal）：米白底，一格黑色底片畫格、上下各四個齒孔，中間一個橘色圓
# 用法：python scripts/make-icon.py app/APP   → 輸出 icon-180/192/512.png（需要 Pillow）
import sys
from PIL import Image, ImageDraw
S = 4096; U = S / 1024        # 以 1024 為設計座標，4 倍超取樣後縮小，邊緣才平滑
def R(*v): return [x * U for x in v]
CREAM, INK, ORANGE = (0xF4, 0xEE, 0xE4), (0x1D, 0x1B, 0x1A), (0xD0, 0x65, 0x2C)
im = Image.new("RGB", (S, S), CREAM); d = ImageDraw.Draw(im)
d.rounded_rectangle(R(212, 302, 812, 722), radius=44 * U, fill=INK)
for i in range(4):
    x = 292 + i * 128
    for y in (330, 664):
        d.rounded_rectangle(R(x, y, x + 56, y + 30), radius=8 * U, fill=CREAM)
d.ellipse(R(512 - 104, 512 - 104, 512 + 104, 512 + 104), fill=ORANGE)
out = sys.argv[1] if len(sys.argv) > 1 else "."
for size in (180, 192, 512):
    im.resize((size, size), Image.LANCZOS).save("%s/icon-%d.png" % (out, size), optimize=True)
