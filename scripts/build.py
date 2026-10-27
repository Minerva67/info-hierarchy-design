import sys,importlib
sys.path.insert(0,__file__.rsplit('/',1)[0])
from common import page
out=sys.argv[1]
for arg in sys.argv[2:]:
    name,mod,H=arg.split(':')
    m=importlib.import_module(mod); body,bg,font=m.build()
    open(f'{out}/{name}.dc.html','w').write(page(name,1242,int(H),bg,body,font))
