# usage: measure.sh file.dc.html -> prints content bottom
f=$1; png=${f%.dc.html}.png
python3 $(dirname $0)/render.py $f $png >/dev/null
python3 -c "
from PIL import Image
im=Image.open('$png').convert('RGB');w,h=im.size;px=im.load()
y=h-1
while y>0 and all(px[x,y]==(251,248,241) for x in range(0,w,6)): y-=1
print(y)"
