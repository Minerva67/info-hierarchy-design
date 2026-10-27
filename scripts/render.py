import re,sys,subprocess,os
src,out=sys.argv[1],sys.argv[2]
L=os.path.expanduser('~/CC/knock-templates/partner-longimg/logos/')
M={'4192caf932bf6a48f9bbe8ca55bb36af':'knock-horizontal.svg','737a46701b63fa27c861fed0648c1cdf':'knock-mark.svg',
'4024d47dae99e03b43d2198d118e8b82':'bytedance.svg','698b0dec5988ef13761a697a4f85f906':'tencent.svg','139913b588e7aaefe9aaf3031be1cd77':'baidu.svg',
'89c6dffc51e810dbe25da12475dd0bad':'amazon.svg','3d0b47d22450691340f977053f728fa0':'google.svg','fdd189b01e62de056840e168a6618adc':'jd_explore.png',
'4689d4efea254a560f3bbd8f430b9a31':'netease.png','cff4108dd016ebab032cf2f48250ad56':'kuaikan.png','ff9f73ceece8e083622b7c1929168a19':'walmart.svg',
'db3b08596ef608b788c8f3bf79a12389':'jpmc.svg','83c625b5267dec3644161bc6200ecbe0':'goldman.svg','606545aefc7324a6222bdefbcd20f218':'mckinsey.svg',
'5f18faebc9ed28cbb06093309e4c3d08':'kimi.svg','6f5c45bae3bbbbcbe35cf8516825b1bf':'zhipu_z.png','e1b61b2364db0d9fba26f09254e5201e':'tripo_dark.png',
'5d9e81673a2593010179308d9b207511':'heygen.svg','f91feff0b73b68c799e57ec765150bd4':'pku.svg','e138393c237e1f32a8566347a2e80294':'geekbang.png','a3e3caae3e0f7e6fd3759011d278f76b':'opc_tonghang.png','1012eafbce4cd049321dcbac6dff790c':'qupengtou.png','0c637a0d8aa7617cdd8f586a18f8042a':os.path.expanduser('~/Desktop/Knock品牌/Knock-brand-kit/logo/horizontal-dark.svg')}
h=open(src).read()
h=re.sub(r'/_blob/([0-9a-f]{32})',lambda m:'file://'+(M.get(m.group(1),'missing') if M.get(m.group(1),'').startswith('/') else L+M.get(m.group(1),'missing')),h)
h=h.replace('<script src="./support.js"></script>','')
h=re.sub(r'</?x-dc>|</?helmet>','',h)
h=re.sub(r'<script type="text/x-dc".*?</script>','',h,flags=re.S)
tmp=out+'.html';open(tmp,'w').write(h)
H=re.search(r'"height":(\d+)',open(src).read()).group(1)
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless=new','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',
 f'--window-size=1242,{H}','--virtual-time-budget=6000',f'--screenshot={out}','file://'+tmp],capture_output=True)
print(out)
