from common import LOGO, MARK, Y, O, INK, grain
import th_v3 as V
BG='#f3ebdd'; SURF='#fbf6ec'; STONE='#ddd1bb'; DROP='#c9bda5'; BODY='#2a2620'; MUTE='#6b6258'
F="'Outfit', 'PingFang SC', 'Noto Sans SC', sans-serif"
P=64
SOL=[(0,'¥800','单条线索成本',[('精准推送','面向参加过 Knock〃 活动的社区成员，按您的目标画像定向推送。'),('社群联合分发','Knock〃 自有账号与多个合作社群同步发布，首发即覆盖数千次曝光。')],'精准触达目标人群'),
     (1,'?','潜在客户占比',[('线索画像','会前为每位报名者生成画像：行业、角色、参会目的。')],'开场前明确潜在客户'),
     (2,'52%','到场率',[('会前匹配','按双方诉求提前匹配约见，参会者带着明确目的到场。')],'到场率提升约 50%'),
     (3,'85%','线索流失率',[('跟进排序','按参会目的与需求排出跟进优先级，明确当下该在谁身上投入精力。'),('转化依据','汇总每位线索的诉求与关注点，为后续转化提供信息，便于您有针对性地介绍方案。')],'跟进有重点，介绍方案更精准')]
FINAL='7.8%'
def meta(t,c=MUTE,s=20): return f'<span style="font-size:{s}px;font-weight:600;letter-spacing:.16em;color:{c};white-space:nowrap;">{t}</span>'
def sechead(n,en,zh):
    return (f'<div style="display:grid;grid-template-columns:200px 1fr;align-items:end;border-top:2px solid {INK};padding-top:28px;">'
            f'<span style="font-size:140px;font-weight:700;line-height:.8;letter-spacing:-.04em;color:{O};">{n}</span>'
            f'<div style="display:flex;flex-direction:column;gap:14px;">{meta(en)}<h2 style="margin:0;font-size:60px;font-weight:700;line-height:1.1;letter-spacing:-.01em;white-space:nowrap;">{zh}</h2></div></div>')
def dots(l,t,d,op=.5): return f'<div aria-hidden="true" style="position:absolute;left:{l}px;top:{t}px;width:{d}px;height:{d}px;border-radius:50%;background-image:radial-gradient({O} 2.4px, transparent 2.8px);background-size:15px 15px;opacity:{op};pointer-events:none;"></div>'
def tagd(t): return f'<span style="align-self:flex-start;font-size:16px;font-weight:600;letter-spacing:.08em;color:#bdb5a8;border:1.5px solid #bdb5a8;padding:2px 8px;white-space:nowrap;">{t}</span>'
def tag(t): return f'<span style="align-self:flex-start;font-size:16px;font-weight:600;letter-spacing:.08em;color:{MUTE};border:1.5px solid {MUTE};padding:2px 8px;white-space:nowrap;">{t}</span>'
def band(x0,a0,b0,x1,a1,b1,fill):
    xm=(x0+x1)/2
    return f'<path d="M{x0} {a0} C{xm} {a0} {xm} {a1} {x1} {a1} L{x1} {b1} C{xm} {b1} {xm} {b0} {x0} {b0} Z" fill="{fill}"/>'
def sankey():
    W=1050; H=760; top=150; S=3.2; drop=70; nw=14
    xA,xB,xC,xD=250,570,860,975
    hA=100*S; hB=52*S; hC=hB*0.15
    s=[f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" aria-hidden="true" style="position:absolute;left:0;top:0;">']
    s.append(f'<rect x="1" y="{top}" width="{xA-12}" height="{hA}" fill="none" stroke="{MUTE}" stroke-width="2" stroke-dasharray="8 8"/>')
    s.append(band(xA+nw,top,top+hB,xB,top,top+hB,Y))
    s.append(band(xB+nw,top,top+hC,xC,top,top+hC,Y))
    s.append(band(xC+nw,top,top+hC,xD-30,top+70,top+70+hC,Y))
    s.append(band(xA+nw,top+hB,top+hA,xB-50,top+hA+drop,top+hA+drop+(hA-hB),DROP))
    s.append(band(xB+nw,top+hC,top+hB,xC-40,top+hA+drop,top+hA+drop+(hB-hC),O))
    for x,h in [(xA,hA),(xB,hB),(xC,hC)]: s.append(f'<rect x="{x}" y="{top}" width="{nw}" height="{h}" fill="{INK}"/>')
    s.append('</svg>')
    T=lambda x,y,w,html,al='left': f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;text-align:{al};">{html}</div>'
    node=lambda n,st,v: f'{meta(n+" "+st,INK,18)}<div style="font-size:34px;font-weight:700;letter-spacing:-.02em;margin-top:6px;white-space:nowrap;">{v}</div>'
    ann=[T(xA-6,top-60,300,meta('02 活动报名审核',INK,18)),
         T(xB-6,top-96,280,node('03','活动开始','到场 52%')),
         T(xC-6,top-96,200,node('04','线索跟进','跟进后 '+FINAL)),
         T(24,top+28,xA-60,f'{meta("01 社群发布活动",INK,18)}<div style="font-size:24px;font-weight:700;margin-top:14px;line-height:1.3;white-space:nowrap;">① 缺少曝光渠道</div>'),
         T(xA+40,top+hB/2-22,xB-xA-70,f'<div style="font-size:24px;font-weight:700;line-height:1.35;">② 报名者画像不明确</div>'),
         T(20,top+hA+drop+10,xA-40,f'<div style="font-size:24px;font-weight:700;line-height:1.35;">③ 到场率偏低</div><div style="font-size:20px;color:{MUTE};margin-top:4px;">未到场 48%</div>','right'),
         T(xC-30,top+hA+drop+40,W-xC+30,f'<div style="font-size:24px;font-weight:700;color:{O};line-height:1.35;">④ 跟进缺乏优先级</div><div style="font-size:20px;color:{MUTE};margin-top:4px;">到场者中流失 85%</div>'),
         f'<div style="position:absolute;left:{xD-34}px;top:{top+70-6}px;width:12px;height:{hC+12}px;background:{INK};"></div>',
         T(xD-150,top+70+hC+24,230,f'{meta("05 有效商机",INK,18)}<div style="font-size:44px;font-weight:700;letter-spacing:-.03em;margin-top:6px;white-space:nowrap;">{FINAL}</div><div style="font-size:18px;color:{MUTE};margin-top:4px;">比例上限</div>','right')]
    return f'<div style="position:relative;width:{W}px;height:{H}px;">{"".join(s)}{"".join(ann)}</div>'
def kpis():
    out=''
    for i,(st,pain,s,sl,_,_) in enumerate(V.STAGES[:4]):
        worst=s==V.WORST
        lab='行业基准 · 展会口径' if s.startswith('¥') else ('行业基准' if s!='?' else '开场前无法得知')
        fg='#ffffff' if worst else INK; sub='#bdb5a8' if worst else BODY
        out+=(f'<div style="background:{INK if worst else SURF};padding:28px 26px;display:flex;flex-direction:column;gap:12px;">'
              f'{meta("①②③④"[i]+" "+st,sub if worst else MUTE,17)}'
              f'<span style="font-size:{60 if len(s)<5 else 56}px;font-weight:700;line-height:.95;letter-spacing:-.03em;color:{O if s!="?" else INK};white-space:nowrap;">{s}</span>'
              f'<span style="font-size:19px;color:{sub};white-space:nowrap;">{sl}</span>'
              f'<div style="border-top:2px solid {fg};padding-top:12px;font-size:24px;font-weight:700;color:{fg};white-space:nowrap;">{pain}</div>{tag(lab) if not worst else tagd(lab)}</div>')
    return f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;">{out}</div>'
def logo_wall():
    cells=''.join(f'<div style="height:96px;display:flex;align-items:center;justify-content:center;background:#fff;"><img src="{s}" alt="{a}" style="height:{V.SIZE.get(a,int(h)-4)-4}px;max-width:78%;object-fit:contain;"></div>' for s,a,h in V.MEMBERS)
    cells+=f'<div style="height:96px;display:flex;align-items:center;justify-content:center;background:#fff;font-size:34px;color:{MUTE};">…</div>'
    return cells
def partners():
    cell='height:88px;background:#fff;display:flex;align-items:center;justify-content:center;'
    out=''
    for n,src,word in V.PARTNERS:
        if src and word: out+=f'<div style="{cell}gap:10px;"><img src="{src}" alt="" style="height:42px;width:42px;object-fit:contain;"><span style="font-size:22px;font-weight:700;white-space:nowrap;">{word}</span></div>'
        elif src: out+=f'<div style="{cell}"><img src="{src}" alt="{n}" style="height:44px;max-width:80%;object-fit:contain;"></div>'
        else: out+=f'<div style="{cell}border:2px dashed {MUTE};box-sizing:border-box;font-size:19px;font-weight:600;color:{MUTE};white-space:nowrap;">{n} logo</div>'
    return out+f'<div style="{cell}font-size:34px;color:{MUTE};">…</div>'
def fixes():
    out=''
    for k,(si,bs,bl,items,res) in enumerate(SOL):
        st,pain=V.STAGES[si][0],V.STAGES[si][1]
        li=''.join(f'<div style="display:flex;flex-direction:column;gap:4px;"><span style="font-size:27px;font-weight:700;">{t}</span><span style="font-size:23px;line-height:1.55;color:{BODY};">{d}</span></div>' for t,d in items)
        before=(f'<div style="background:{STONE};padding:36px;display:flex;flex-direction:column;gap:20px;">{meta("BEFORE",BODY)}'
                f'<div style="margin-top:auto;display:flex;flex-direction:column;gap:6px;"><span style="font-size:76px;font-weight:700;line-height:.9;letter-spacing:-.04em;white-space:nowrap;">{bs}</span><span style="font-size:20px;color:{BODY};">{bl}</span></div></div>')
        after=(f'<div style="background:{Y};padding:36px;display:flex;flex-direction:column;gap:18px;">{meta("AFTER · KNOCK〃",INK)}{li}'
               f'<div style="margin-top:auto;border-top:2px solid {INK};padding-top:18px;font-size:40px;font-weight:700;letter-spacing:-.02em;line-height:1.2;">{res}</div></div>')
        extra=''
        if si==0:
            extra=(f'<div style="background:{SURF};padding:32px 36px;display:flex;flex-direction:column;gap:20px;margin-top:8px;">'
                   f'<div style="display:flex;justify-content:space-between;align-items:baseline;"><span style="font-size:26px;font-weight:700;">推送对象：社区成员来自</span>{meta("创业者 · 投资人 · 开发者 · OPC",MUTE,18)}</div>'
                   f'<div style="display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:6px;">{logo_wall()}</div>'
                   f'</div>')
        out+=(f'<div style="display:flex;flex-direction:column;gap:16px;">'
              f'<div style="display:flex;justify-content:space-between;align-items:baseline;"><span style="font-size:36px;font-weight:700;white-space:nowrap;">{"ABCD"[k]}　{pain}</span>{meta("环节 0"+str(si+1)+" · "+st,INK)}</div>'
              f'<div style="display:grid;grid-template-columns:1fr 64px 1.5fr;gap:8px;">{before}'
              f'<div style="display:flex;align-items:center;justify-content:center;"><svg width="44" height="24" viewBox="0 0 44 24" aria-hidden="true"><path d="M2 12h38M30 3l10 9-10 9" fill="none" stroke="{INK}" stroke-width="2.5"/></svg></div>{after}</div>{extra}</div>')
    return f'<div style="display:flex;flex-direction:column;gap:56px;">{out}</div>'
PTS=[('精准触达目标人群','活动定向推送给符合画像的 AI 创业者、投资人、开发者与 OPC。'),
     ('会前锁定潜在客户','开场前拿到报名者画像，提前明确哪些人是潜在客户。'),
     ('约好的人如期到场','会前按双方诉求匹配约见，到场率提升约 50%。'),
     ('会后跟进有的放矢','知道先跟进谁、对方需要什么，转化时能更有针对性地介绍方案。')]
def build():
    pts=''.join(f'<div style="background:{SURF};padding:30px 30px;display:flex;flex-direction:column;gap:12px;min-height:170px;"><span style="font-size:20px;font-weight:700;color:{O};">0{i+1}</span><span style="font-size:32px;font-weight:700;white-space:nowrap;">{t}</span><span style="font-size:22px;line-height:1.55;color:{BODY};">{d}</span></div>' for i,(t,d) in enumerate(PTS))
    body=f'''{grain(.28,.8,5)}
<div style="position:relative;padding:0 {P}px;display:flex;flex-direction:column;gap:120px;">
  <section style="position:relative;padding-top:56px;display:flex;flex-direction:column;gap:48px;">
    {dots(700,170,440,.5)}
    <div style="position:relative;display:grid;grid-template-columns:1fr 1fr 1fr;align-items:center;padding-bottom:24px;border-bottom:2px solid {INK};">
      <img src="{LOGO}" alt="Knock〃" style="height:76px;width:auto;display:block;">
      <span style="text-align:center;">{meta("FOR B2B EVENT HOSTS",INK)}</span>
      <span style="text-align:right;font-size:24px;font-weight:600;">商家合作</span>
    </div>
    <h1 style="position:relative;margin:90px 0 30px;font-size:128px;font-weight:700;line-height:.98;letter-spacing:-.045em;white-space:nowrap;">Meet right people<br>in every event</h1>
    <div style="position:relative;display:grid;grid-template-columns:1fr 1fr;gap:6px;">{pts}</div>
  </section>
  <section style="display:flex;flex-direction:column;gap:48px;">{sechead("01","YOUR FUNNEL · 流失走向","活动转化漏斗")}
    <div style="background:{SURF};padding:40px 0 24px 32px;">{sankey()}</div>
    {kpis()}
    <div style="border-top:2px solid {INK};border-bottom:2px solid {INK};padding:36px 0;display:grid;grid-template-columns:auto 1fr;gap:44px;align-items:center;">
      <span style="font-size:120px;font-weight:700;line-height:.85;letter-spacing:-.05em;color:{O};white-space:nowrap;">{FINAL}</span>
      <div style="display:flex;flex-direction:column;gap:10px;"><span style="font-size:34px;font-weight:700;line-height:1.3;">报名者中，最终可能成为有效商机的比例上限</span><span style="font-size:22px;color:{MUTE};">按行业基准推算：到场率 52% × 跟进留存 15%（线索流失率 85%）</span></div>
    </div>
    <div style="font-size:20px;color:{MUTE};">黄 = 留下的人　灰 = 未到场　橙 = 到场后在跟进中流失　· 比例均为行业基准</div>
  </section>
  <section style="display:flex;flex-direction:column;gap:48px;">{sechead("02","BEFORE / AFTER","各环节解决方案")}{fixes()}</section>
  <section style="position:relative;margin:0 -{P}px;">
    <div style="background:{INK};color:#fff;padding:80px {P}px 72px;display:grid;grid-template-columns:200px 1fr;row-gap:36px;">
      <span style="font-size:140px;font-weight:700;line-height:.8;letter-spacing:-.04em;color:{O};">03</span>
      <div style="display:flex;flex-direction:column;gap:24px;">{meta("WAITLIST","#bdb5a8")}<h2 style="margin:0;font-size:80px;font-weight:700;line-height:1;letter-spacing:-.03em;white-space:nowrap;">{V.OFFER_T}</h2>
        <a href="https://knockknock.example/waitlist" style="align-self:flex-start;margin-top:12px;display:inline-flex;align-items:center;height:92px;padding:0 56px;background:{Y};color:{INK};font-size:30px;font-weight:700;text-decoration:none;">加入 waitlist →</a>
      </div>
    </div>
    <div style="padding:40px {P}px 48px;display:flex;justify-content:space-between;align-items:center;">
      <img src="{LOGO}" alt="Knock〃" style="height:60px;width:auto;display:block;"><span style="font-size:24px;font-weight:600;">Knock knock, who's there?</span>
    </div>
  </section>
</div>'''
    return body,BG,F
