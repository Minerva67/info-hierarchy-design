from common import LOGO, MARK, Y, O, INK, page
import os
BG='#f3f0ee'; BODY='#262627'; MUTE='#696969'; HAIR='#d1cdc7'
F="'Sofia Sans', 'PingFang SC', 'Noto Sans SC', sans-serif"
P=56
DARKLOGO='/_blob/0c637a0d8aa7617cdd8f586a18f8042a'
MEMBERS=[l.strip().split('|') for l in open(os.path.join(os.path.dirname(__file__),'members.txt'))]
SIZE={'快看':60,'智谱':48,'HeyGen':56,'北京大学':66,'京东探索研究院':36,'VAST Tripo':34,'高盛':46,'百度':44,'Google':44,'亚马逊':40,'Kimi 月之暗面':46}
# ---------- copy (formal) ----------
HERO=['Meet right people','in every event']
INTRO=['企业举办 meetup、沙龙与 workshop，目的是获取销售线索。','从发布到跟进共五个环节，每个环节都存在流失，','但流失发生在哪一环、规模多大，目前缺少依据。']
# stage, pain, stat, stat label, bar fill (None=no bar), bar label
STAGES=[('社群发布活动','缺少曝光渠道',None,None,None,''),
        ('活动报名审核','报名者画像不明确','?','潜在客户占比',1.0,'全部报名'),
        ('活动开始','到场率偏低','52%','到场率',0.52,'到场 52%'),
        ('线索跟进','跟进缺乏优先级','85%','线索流失率',0.15,'留存 15%'),
        ('有效商机','有效商机数量无法预估',None,None,None,'')]
WORST='85%'
# solutions per stage: (stage idx, before stat, before label, items, result)
SOL=[(0,'缺少','曝光渠道',[('精准推送','面向参加过 Knock〃 活动的社区成员，按您的目标画像定向推送。'),('社群联合分发','Knock〃 自有账号与多个合作社群同步发布，首发即覆盖数千次曝光。')],'曝光覆盖扩大'),
     (1,'?','潜在客户占比',[('线索画像','会前为每位报名者生成画像：行业、角色、参会目的。')],'会前明确约 50% 潜在客户'),
     (2,'52%','到场率',[('会前匹配','按双方诉求提前匹配约见，参会者带着明确目的到场。')],'到场率提升约 50%'),
     (3,'85%','线索流失率',[('跟进排序','按参会目的与需求排出跟进优先级，标注每位线索的核心诉求，便于您分配精力、匹配方案。')],'明确跟进重点与客户需求')]
PARTNERS=[('极客邦','/_blob/e138393c237e1f32a8566347a2e80294'),('黑客松',None)]
TODO=('您需要做的：','审核报名并共享名单。现有流程不变，无需增加人力。')
OFFER_T='首批合作商家免费试用'; OFFER=['覆盖一至两场活动。加入 waitlist 后，下一场活动即可使用。','请留下公司名称与下一场活动日期。']
# ---------- components ----------
def eyebrow(t,c=INK): return f'<span style="display:inline-flex;align-items:center;gap:12px;font-size:24px;font-weight:700;letter-spacing:.06em;color:{c};white-space:nowrap;"><span style="width:12px;height:12px;border-radius:999px;background:{O};"></span>{t}</span>'
def h2(t,c=INK): return f'<h2 style="margin:0;font-size:72px;font-weight:500;line-height:1.1;letter-spacing:-.02em;color:{c};white-space:nowrap;">{t}</h2>'
def badge(t,bg=INK,c='#fff',d=48,fs=22): return f'<span style="flex:0 0 auto;width:{d}px;height:{d}px;border-radius:999px;background:{bg};color:{c};display:inline-flex;align-items:center;justify-content:center;font-size:{fs}px;font-weight:700;">{t}</span>'
def bench(): return f'<span style="align-self:flex-start;font-size:16px;font-weight:700;letter-spacing:.06em;color:{MUTE};border:1.5px solid {HAIR};border-radius:999px;padding:3px 10px;white-space:nowrap;">行业基准</span>'
def unk(): return f'<span style="font-size:16px;font-weight:700;color:{MUTE};">开场前无法得知</span>'
def funnel():
    BW=440; rows=''
    for i,(st,pain,s,sl,fill,blab) in enumerate(STAGES):
        worst = s==WORST
        if i==0:
            bar=f'<div style="width:{BW}px;height:64px;border-radius:999px;border:3px dashed #b9b4ae;box-sizing:border-box;display:flex;align-items:center;"></div>'
        elif fill is None:
            bar=f'<div style="width:64px;height:64px;border-radius:999px;background:{Y};display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:700;">?</div>'
        else:
            w=max(64,int(BW*fill)); inside=fill>0.4
            bar=(f'<div style="position:relative;width:{BW}px;height:64px;border-radius:999px;background:{BG};">'
                 f'<div style="position:absolute;left:0;top:0;width:{w}px;height:64px;border-radius:999px;background:{O if worst else (INK if i==1 else Y)};"></div>'
                 f'<span style="position:absolute;left:{26 if inside else w+18}px;top:0;height:64px;display:flex;align-items:center;font-size:22px;font-weight:700;color:{"#fff" if i==1 else INK};white-space:nowrap;">{blab}</span></div>')
        if s:
            right=(f'<div style="display:flex;flex-direction:column;gap:8px;"><span style="font-size:26px;font-weight:700;white-space:nowrap;">{pain}</span>'
                   f'<div style="display:flex;align-items:baseline;gap:12px;"><span style="font-size:{60 if s!="?" else 60}px;font-weight:700;line-height:1;letter-spacing:-.03em;color:{O if worst else INK};white-space:nowrap;">{s}</span><span style="font-size:20px;color:{MUTE};white-space:nowrap;">{sl}</span></div>'
                   f'{bench() if s!="?" else unk()}</div>')
        else:
            right=f'<span style="font-size:26px;font-weight:700;white-space:nowrap;">{pain}</span>'
        rows+=(f'<div style="display:grid;grid-template-columns:230px {BW}px 1fr;column-gap:40px;align-items:center;padding:30px 0;{"border-top:1.5px solid "+HAIR+";" if i else ""}">'
               f'<div style="display:flex;align-items:center;gap:16px;">{badge("0"+str(i+1),O if worst else (Y if i==4 else INK),INK if i==4 else "#fff",44,18)}<span style="font-size:28px;font-weight:600;white-space:nowrap;">{st}</span></div>{bar}{right}</div>')
    return f'<div style="background:#fff;border-radius:48px;padding:20px 48px;">{rows}</div>'
def logo_wall():
    cells=''.join(f'<div style="height:104px;display:flex;align-items:center;justify-content:center;background:#fff;border-radius:24px;"><img src="{s}" alt="{a}" style="height:{SIZE.get(a,int(h)-4)}px;max-width:78%;object-fit:contain;"></div>' for s,a,h in MEMBERS)
    cells+=f'<div style="height:104px;display:flex;align-items:center;justify-content:center;background:#fff;border-radius:24px;font-size:36px;color:{MUTE};">…</div>'
    return cells
def partner_logos():
    cell='height:96px;background:#fff;border-radius:24px;display:flex;align-items:center;justify-content:center;'
    out=''
    for n,src in PARTNERS:
        out+=(f'<div style="{cell}"><img src="{src}" alt="{n}" style="height:44px;max-width:78%;object-fit:contain;"></div>' if src
              else f'<div style="{cell}border:2px dashed #b9b4ae;font-size:22px;font-weight:600;color:{MUTE};">{n} logo</div>')
    return out+f'<div style="{cell}font-size:36px;color:{MUTE};">…</div>'
def solutions():
    out=''
    for k,(si,bs,bl,items,res) in enumerate(SOL):
        st,pain=STAGES[si][0],STAGES[si][1]; worst=bs==WORST
        circ=(f'<div style="width:220px;height:220px;border-radius:999px;background:{BG};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;">'
              f'<span style="font-size:{60 if len(bs)<4 else 52}px;font-weight:700;letter-spacing:-.03em;color:{O if worst else BODY};white-space:nowrap;">{bs}</span><span style="font-size:18px;color:{MUTE};white-space:nowrap;">{bl}</span></div>')
        li=''.join(f'<div style="display:flex;flex-direction:column;gap:6px;"><span style="font-size:28px;font-weight:700;">{t}</span><span style="font-size:25px;line-height:1.55;color:{BODY};">{d}</span></div>' for t,d in items)
        extra=''
        if si==0:
            extra=(f'<div style="background:{BG};border-radius:40px;padding:36px;display:flex;flex-direction:column;gap:22px;">'
                   f'<div style="display:flex;justify-content:space-between;align-items:baseline;"><span style="font-size:26px;font-weight:700;">推送对象：社区成员来自</span><span style="font-size:20px;color:{MUTE};">创业者 · 投资人 · 开发者 · OPC</span></div>'
                   f'<div style="display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;">{logo_wall()}</div>'
                   f'<span style="font-size:26px;font-weight:700;margin-top:10px;">合作社群</span>'
                   f'<div style="display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;">{partner_logos()}</div></div>')
        out+=(f'<div style="background:#fff;border-radius:48px;padding:44px 48px;display:flex;flex-direction:column;gap:32px;">'
              f'<div style="display:flex;align-items:center;gap:16px;">{badge("0"+str(si+1),O if worst else INK,"#fff",44,18)}<span style="font-size:22px;font-weight:700;letter-spacing:.04em;color:{MUTE};white-space:nowrap;">{st}</span><span style="font-size:36px;font-weight:600;white-space:nowrap;">{pain}</span></div>'
              f'<div style="display:grid;grid-template-columns:auto 1fr;gap:44px;align-items:center;">'
              f'<div style="display:flex;flex-direction:column;gap:12px;align-items:center;"><span style="font-size:18px;font-weight:700;letter-spacing:.06em;color:{MUTE};">现状</span>{circ}</div>'
              f'<div style="display:flex;flex-direction:column;gap:22px;border-left:3px solid {O};padding-left:40px;"><span style="font-size:18px;font-weight:700;letter-spacing:.06em;color:{MUTE};">KNOCK〃 方案</span>{li}</div></div>'
              f'{extra}'
              f'<div style="background:{Y};border-radius:999px;padding:24px 40px;display:flex;justify-content:space-between;align-items:center;"><span style="font-size:22px;font-weight:700;letter-spacing:.06em;">结果</span><span style="font-size:42px;font-weight:700;letter-spacing:-.02em;white-space:nowrap;">{res}</span></div></div>')
    return f'<div style="display:flex;flex-direction:column;gap:28px;">{out}</div>'
def build():
    PTS=[('触达目标人群','活动定向推送给符合画像的 AI 创业者、投资人、开发者与 OPC。'),
         ('会前锁定潜在客户','开场前拿到报名者画像，约 50% 潜在客户提前明确。'),
         ('约好的人如期到场','会前按双方诉求匹配约见，到场率提升约 50%。'),
         ('会后跟进有的放矢','知道先跟进谁、对方需要什么，方案匹配更准。')]
    results=''.join(f'<div style="background:#fff;border-radius:36px;padding:32px 30px;display:flex;flex-direction:column;gap:14px;">{badge("0"+str(i+1),INK,"#fff",36,15)}<span style="font-size:30px;font-weight:700;line-height:1.25;white-space:nowrap;">{t}</span><span style="font-size:22px;line-height:1.55;color:{BODY};">{d}</span></div>' for i,(t,d) in enumerate(PTS))
    body=f'''<div style="position:relative;padding:0 {P}px;display:flex;flex-direction:column;gap:130px;">
  <section style="position:relative;padding-top:56px;display:flex;flex-direction:column;gap:44px;">
    <div style="display:flex;justify-content:space-between;align-items:center;"><img src="{LOGO}" alt="Knock〃" style="height:80px;width:auto;display:block;"><span style="font-size:24px;font-weight:600;background:#fff;border-radius:999px;padding:14px 30px;">商家合作</span></div>
    <div style="position:relative;height:480px;">
      <div style="position:absolute;right:20px;top:0;width:440px;height:440px;border-radius:999px;background:{Y};display:flex;align-items:center;justify-content:center;"><img src="{MARK}" alt="" aria-hidden="true" style="width:220px;height:auto;display:block;"></div>
      <div style="position:absolute;right:420px;top:300px;width:150px;height:150px;border-radius:999px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700;letter-spacing:.06em;text-align:center;line-height:1.3;">FOR B2B<br>EVENT<br>HOSTS</div>
      <svg width="1130" height="480" viewBox="0 0 1130 480" aria-hidden="true" style="position:absolute;inset:0;"><path d="M-20 440 C 260 520, 520 110, 900 30" fill="none" stroke="{O}" stroke-width="3"/></svg>
    </div>
    <h1 style="margin:-30px 0 0;font-size:112px;font-weight:500;line-height:1.0;letter-spacing:-.03em;white-space:nowrap;">{HERO[0]}<br>{HERO[1]}</h1>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:12px;">{results}</div>
  </section>
  <section style="display:flex;flex-direction:column;gap:40px;">{eyebrow("01 · 现状")}{h2("活动转化漏斗")}{funnel()}</section>
  <section style="display:flex;flex-direction:column;gap:40px;">{eyebrow("02 · 方案")}{h2("各环节解决方案")}{solutions()}</section>
  <section style="margin:0 -{P}px;background:{INK};color:#fff;border-radius:80px 80px 0 0;padding:96px {P}px 56px;display:flex;flex-direction:column;gap:30px;position:relative;overflow:hidden;">
    <div aria-hidden="true" style="position:absolute;right:-120px;top:-120px;width:420px;height:420px;border-radius:999px;background:{Y};"></div>
    <div style="position:relative;">{eyebrow("03 · WAITLIST","#fff")}</div>
    <h2 style="position:relative;margin:0;font-size:84px;font-weight:500;line-height:1.05;letter-spacing:-.02em;white-space:nowrap;">{OFFER_T}</h2>
    <p style="position:relative;margin:0;font-size:29px;line-height:1.7;color:#d6d3cf;">{"<br>".join(OFFER)}</p>
    <div style="position:relative;display:flex;align-items:center;gap:36px;margin-top:16px;">
      <a href="https://knockknock.example/waitlist" style="display:inline-flex;align-items:center;height:92px;padding:0 56px;border-radius:20px;background:{Y};color:{INK};font-size:30px;font-weight:700;text-decoration:none;">加入 waitlist</a>
      <div style="display:flex;flex-direction:column;gap:8px;font-size:24px;color:#d6d3cf;"><span>WhatsApp · [号码]</span><span>[邮箱]</span></div>
      <div style="margin-left:auto;width:170px;height:170px;border-radius:40px;background:#fff;color:{MUTE};display:flex;align-items:center;justify-content:center;font-size:20px;">[二维码]</div>
    </div>
    <div style="position:relative;margin-top:56px;border-top:1.5px solid #3a3b3a;padding-top:30px;display:flex;justify-content:space-between;align-items:center;"><img src="{DARKLOGO}" alt="Knock〃" style="height:60px;width:auto;display:block;"><span style="font-size:24px;color:#d6d3cf;">Knock knock, who's there?</span></div>
  </section>
</div>'''
    return body,BG,F
