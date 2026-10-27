# usage: fit.sh outdir Name:module  -> builds at 9000 w/o grain, measures, rebuilds at fitted height, renders png
D=$(cd $(dirname $0) && pwd); out=$1; spec=$2; name=${spec%%:*}
NOGRAIN=1 python3 $D/build.py $out $spec:9000
python3 - "$out/$name.dc.html" <<'PY'
import sys,re
f=sys.argv[1];h=open(f).read()
open(f,'w').write(h.replace('background:#','background:#',1))
PY
y=$(bash $D/measure.sh $PWD/$out/$name.dc.html 2>/dev/null)
# measure.sh checks bg (251,248,241); use generic: last row differing from bottom row color
y=$(python3 -c "
from PIL import Image
im=Image.open('$out/$name.png').convert('RGB');w,h=im.size;px=im.load();bg=px[w//2,h-1]
y=h-1
while y>0 and all(px[x,y]==bg for x in range(0,w,4)): y-=1
print(y+1)")
python3 $D/build.py $out $spec:$y
python3 $D/render.py $PWD/$out/$name.dc.html $PWD/$out/$name.png >/dev/null
echo $name $y
