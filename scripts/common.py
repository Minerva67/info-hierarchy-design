"""共享外壳：配色、字体、纸纹、字母抖动、Claude Design 画板骨架。
默认强调色是一组「黄 / 橙 / 墨黑」，换成你的品牌色即可。"""
import random
Y = '#fae36b'    # 主强调色（大色块、结果条）
O = '#ef6a2f'    # 唯一的高亮色（最大的漏点、编号）
INK = '#151716'  # 文字与线条
FONTS='<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,700;1,6..72,300;1,6..72,400&family=Noto+Serif+SC:wght@300;400;500;700;900&family=Outfit:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700;900&family=Special+Elite&family=Courier+Prime:wght@400;700&family=Sofia+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600&family=Inter:wght@400;500;600;700&family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
def grain(op=.35,freq=.9,seed=3):
    import os
    if os.environ.get('NOGRAIN'): return ''
    return (f'<svg aria-hidden="true" width="100%" height="100%" style="position:absolute;inset:0;pointer-events:none;opacity:{op};mix-blend-mode:multiply;">'
            f'<filter id="g{seed}"><feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="2" seed="{seed}"/><feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.3  0 0 0 0 0.22  0 0 0 .55 0"/></filter>'
            f'<rect width="100%" height="100%" filter="url(#g{seed})"/></svg>')
def jitter(text,seed=1,amp=.08,rot=1.6):
    r=random.Random(seed); out=''
    for ch in text:
        if ch==' ': out+=' '; continue
        dy=r.uniform(-amp,amp); a=r.uniform(-rot,rot); op=r.choice([1,1,1,1,.86])
        out+=f'<span style="display:inline-block;transform:translateY({dy:.3f}em) rotate({a:.1f}deg);opacity:{op};">{ch}</span>'
    return out
def page(title,W,H,bg,body,font):
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
{FONTS}
<style>
body{{margin:0;background:{bg}}}
a{{color:#151716}}a:hover{{color:#ef6a2f}}
</style>
</helmet>
<div style="position:relative;width:{W}px;height:{H}px;box-sizing:border-box;background:{bg};color:{INK};font-family:{font};overflow:hidden;">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
