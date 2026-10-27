import re,sys,subprocess,os
src,out=sys.argv[1],sys.argv[2]
L=os.environ.get('ASSET_DIR',os.path.join(os.path.dirname(__file__),'assets'))+'/'
import json
M=json.load(open(os.path.join(os.path.dirname(__file__),'blobmap.json'))) if os.path.exists(os.path.join(os.path.dirname(__file__),'blobmap.json')) else {}
h=open(src).read()
h=re.sub(r'/_blob/([0-9a-f]{32})',lambda m:'file://'+(M.get(m.group(1),'missing') if M.get(m.group(1),'').startswith('/') else L+M.get(m.group(1),'missing')),h)
h=h.replace('<script src="./support.js"></script>','')
h=re.sub(r'</?x-dc>|</?helmet>','',h)
h=re.sub(r'<script type="text/x-dc".*?</script>','',h,flags=re.S)
tmp=out+'.html';open(tmp,'w').write(h)
H=re.search(r'"height":(\d+)',open(src).read()).group(1)
CHROME=os.environ.get('CHROME','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
subprocess.run([CHROME,'--headless=new','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',
 f'--window-size=1242,{H}','--virtual-time-budget=6000',f'--screenshot={out}','file://'+tmp],capture_output=True)
print(out)
