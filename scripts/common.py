import random
LOGO='/_blob/4192caf932bf6a48f9bbe8ca55bb36af'; MARK='/_blob/737a46701b63fa27c861fed0648c1cdf'
Y='#fae36b'; O='#ef6a2f'; INK='#151716'
HERO=['报名一百人，像客户的有几个，','开场前没人知道。']
INTRO=['你办 meetup、沙龙、workshop 是为了拿线索。','从发布到跟进五步，每一步都在漏，','漏到哪一步、漏了多少，没有一个环节能回答。']
STAGES=['社群发布活动','活动报名审核','活动开始','线索跟进','商机']
# id, stage index, pain, stat, stat label
LEAKS=[('①',0,'缺乏曝光渠道','$112–200','每条线索的成本'),
       ('②',1,'画像看不清','?','像客户的有几个'),
       ('③',2,'到场率低','52–70%','到场率'),
       ('④',3,'跟进没有重点','85–92%','线索流失率')]
END='有几个，算不出。'
NOTE='行业基准，不是我们的数据。你的每一场，大概率就在这个区间里。'
CALC='以 100 人报名为例，按行业基准推算'
# title, leak ids, before stats, solutions, result
FIXES=[('缺乏曝光渠道',['①'],[('$112–200','每条线索的成本')],['人脉网络精准触达','合作社群 + 自有账号联合分发'],'曝光扩大'),
       ('画像看不清，跟进没有重点',['②','④'],[('?','像客户的有几个'),('85–92%','线索流失率')],['会前生成线索画像','按目的与诉求排出跟进优先级与话术'],'先找谁，一目了然'),
       ('到场率低',['③'],[('52–70%','到场率')],['会前匹配，参会者赴约而来'],'到场率 +50%')]
PARTNERS=['极客邦','贵客松','[合作社区 3]','[合作社区 4]']
TODO_K='你要做的：'; TODO='审核报名，把名单交给我们。流程不改，同事不多做事。'
OFFER_T='首批商家免费测试'; OFFER=['一到两场活动。加入 waitlist，下一场活动就能用。','留下公司名和下一场活动的日期。']
CTA='加入 waitlist'; CTA_URL='https://knockknock.example/waitlist'
CONTACT=['WhatsApp · [号码]','[邮箱]']
SLOGAN="Knock knock, who's there?"
WORST='85–92%'
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
