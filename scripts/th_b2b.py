from common import Y, O, INK, grain
import content as V
V4 = V
def logo(T, dark=False, h=76):
    c = T.get('logo_dark_fg', '#ffffff') if dark else T['ink']
    return f'<span style="font-family:{T["df"]};font-size:{int(h*0.62)}px;font-weight:800;letter-spacing:-.02em;color:{c};white-space:nowrap;">{V.BRAND}<span style="color:{O};">.</span></span>'
def mark(size=200, bg=None):
    return f'<span aria-hidden="true" style="width:{size}px;height:{size}px;border-radius:50%;background:{bg or INK};color:{Y};display:inline-flex;align-items:center;justify-content:center;font-size:{int(size*0.5)}px;font-weight:900;">{V.BRAND[0]}</span>'
T=None
def css(**k): return ';'.join(f"{a.replace('_','-')}:{b}" for a,b in k.items())+';'
def lab(t,c=None,s=None):
    return f'<span style="font-family:{T["lf"]};font-size:{s or T["ls"]}px;font-weight:{T["lw"]};letter-spacing:{T["lt"]};color:{c or T["mute"]};white-space:nowrap;{"text-transform:uppercase;" if T.get("upper") else ""}">{t}</span>'
def h2(t,c=None): return f'<h2 style="margin:0;font-family:{T["df"]};font-size:{T["h2"]}px;font-weight:{T["dw"]};line-height:1.12;letter-spacing:{T["dt"]};color:{c or T["ink"]};white-space:nowrap;">{t}</h2>'
def eyebrow(t,c=None):
    dot=f'<span style="width:12px;height:12px;border-radius:999px;background:{O};"></span>' if T.get('dot') else ''
    return f'<span style="display:inline-flex;align-items:center;gap:12px;">{dot}{lab(t,c or T["eb"],T["ls"]+2)}</span>'
def sechead(n,en,zh): return f'<div style="display:flex;flex-direction:column;gap:22px;">{eyebrow(n+T["sep"]+en)}{h2(zh)}</div>'
def card(inner,pad='36px',bg=None,extra=''):
    return f'<div style="background:{bg or T["surf"]};border-radius:{T["r"]}px;{T["border"]}padding:{pad};{extra}">{inner}</div>'
def band(x0,a0,b0,x1,a1,b1,fill):
    xm=(x0+x1)/2
    return f'<path d="M{x0} {a0} C{xm} {a0} {xm} {a1} {x1} {a1} L{x1} {b1} C{xm} {b1} {xm} {b0} {x0} {b0} Z" fill="{fill}"/>'
def sankey(W):
    P=T['panel']; H=760; top=150; S=3.2; drop=70; nw=14
    xA,xB,xC,xD=int(W*.238),int(W*.543),int(W*.82),int(W*.93)
    hA=100*S; hB=V.ATTEND*S; hC=hB*V.RETAIN/100
    s=[f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" aria-hidden="true" style="position:absolute;left:0;top:0;">',
       f'<rect x="1" y="{top}" width="{xA-12}" height="{hA}" rx="{min(T["r"],16)}" fill="none" stroke="{P["dash"]}" stroke-width="2" stroke-dasharray="8 8"/>',
       band(xA+nw,top,top+hB,xB,top,top+hB,P['main']),band(xB+nw,top,top+hC,xC,top,top+hC,P['main']),
       band(xC+nw,top,top+hC,xD-30,top+70,top+70+hC,P['main']),
       band(xA+nw,top+hB,top+hA,xB-50,top+hA+drop,top+hA+drop+(hA-hB),P['drop']),
       band(xB+nw,top+hC,top+hB,xC-40,top+hA+drop,top+hA+drop+(hB-hC),O)]
    for x,h in [(xA,hA),(xB,hB),(xC,hC)]: s.append(f'<rect x="{x}" y="{top}" width="{nw}" height="{h}" fill="{P["node"]}"/>')
    s.append(f'<rect x="{xD-34}" y="{top+64}" width="12" height="{hC+12}" fill="{P["node"]}"/></svg>')
    tx=P['text']; mu=P['mute']; mainfg=P.get('mainfg',INK)
    A=lambda x,y,w,h,al='left': f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;text-align:{al};">{h}</div>'
    big=lambda v,c=tx: f'<div style="font-family:{T["df"]};font-size:34px;font-weight:{T["kw"]};letter-spacing:-.02em;margin-top:6px;white-space:nowrap;color:{c};">{v}</div>'
    a=[A(xA-6,top-60,300,lab('02 '+V.STAGES[1][0],tx,17)),
       A(xB-6,top-96,280,lab('03 '+V.STAGES[2][0],tx,17)+big(f'到场 {V.ATTEND}%')),
       A(xC-6,top-96,220,lab('04 '+V.STAGES[3][0],tx,17)+big('跟进后 '+V4.FINAL)),
       A(24,top+28,xA-50,lab('01 '+V.STAGES[0][0],tx,17)+f'<div style="font-size:24px;font-weight:700;margin-top:14px;white-space:nowrap;color:{tx};">① {V.STAGES[0][1]}</div>'),
       A(xA+40,top+hB/2-18,xB-xA-70,f'<div style="font-size:24px;font-weight:700;color:{mainfg};">② {V.STAGES[1][1]}</div>'),
       A(20,top+hA+drop+10,xA-40,f'<div style="font-size:24px;font-weight:700;color:{tx};">③ {V.STAGES[2][1]}</div><div style="font-size:20px;color:{mu};margin-top:4px;">未到场 {100-V.ATTEND}%</div>','right'),
       A(xC-30,top+hA+drop+40,W-xC+30,f'<div style="font-size:24px;font-weight:700;color:{O};">④ {V.STAGES[3][1]}</div><div style="font-size:20px;color:{mu};margin-top:4px;">到场者中流失 {100-V.RETAIN}%</div>'),
       A(xD-170,top+70+hC+24,250,lab('05 '+V.STAGES[4][0],tx,17)+f'<div style="font-family:{T["df"]};font-size:44px;font-weight:{T["kw"]};letter-spacing:-.03em;margin-top:6px;color:{tx};">{V4.FINAL}</div><div style="font-size:18px;color:{mu};margin-top:4px;">比例上限</div>','right')]
    return f'<div style="position:relative;width:{W}px;height:{H}px;">{"".join(s)}{"".join(a)}</div>'
def kpis():
    out=''
    for i,(st,pain,s,sl,_,_) in enumerate(V.STAGES[:4]):
        worst=s==V.WORST and T['kpi_worst_dark']; hot=s==V.WORST; bg=T['kpi_worst'] if worst else T['surf']; fg='#ffffff' if worst and T['kpi_worst_dark'] else T['ink']; sub='#bdb5a8' if worst and T['kpi_worst_dark'] else T['mute']
        tg='行业基准 · 展会口径' if s.startswith('¥') else ('行业基准' if s!='?' else '开场前无法得知')
        bd=f'border:2.5px solid {O};' if (hot and not worst) else ('' if worst else T['border'])
        out+=(f'<div style="background:{bg};border-radius:{T["r"]}px;{bd}padding:28px 26px;display:flex;flex-direction:column;gap:12px;">'
              f'{lab("①②③④"[i]+" "+st,sub,16)}<span style="font-family:{T["df"]};font-size:{56 if len(s)<5 else 52}px;font-weight:{T["kw"]};line-height:.95;letter-spacing:-.03em;color:{O if s!="?" else fg};white-space:nowrap;">{s}</span>'
              f'<span style="font-size:19px;color:{sub};white-space:nowrap;">{sl}</span><div style="border-top:1.5px solid {fg if worst else T["line"]};padding-top:12px;font-size:23px;font-weight:700;color:{fg};white-space:nowrap;">{pain}</div>'
              f'<span style="align-self:flex-start;font-size:15px;font-weight:600;color:{sub};border:1.5px solid {sub};border-radius:{min(T["r"],999)}px;padding:2px 10px;white-space:nowrap;">{tg}</span></div>')
    return f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:{T["gap"]}px;">{out}</div>'
def conclusion():
    return (f'<div style="{T["concl"]}display:grid;grid-template-columns:auto 1fr;gap:44px;align-items:center;">'
            f'<span style="font-family:{T["df"]};font-size:116px;font-weight:{T["kw"]};line-height:.85;letter-spacing:-.05em;color:{O};white-space:nowrap;">{V4.FINAL}</span>'
            f'<div style="display:flex;flex-direction:column;gap:10px;"><span style="font-size:32px;font-weight:700;line-height:1.3;color:{T["concl_fg"]};">报名者中，最终可能成为有效商机的比例上限</span><span style="font-size:21px;color:{T["concl_mu"]};">按行业基准推算：到场率 {V.ATTEND}% × 跟进留存 {V.RETAIN}%（线索流失率 {100-V.RETAIN}%）</span></div></div>')
def logo_cells(items, h=96):
    cell=f'height:{h}px;background:#fff;border-radius:{min(T["r"],20)}px;display:flex;align-items:center;justify-content:center;{T["logo_border"]}'
    return cell
def walls():
    cell=logo_cells(None)
    mem=''.join((f'<div style="{cell}"><img src="{s}" alt="{a}" style="height:{V.SIZE.get(a,int(h)-4)-4}px;max-width:78%;object-fit:contain;"></div>' if s else f'<div style="{cell}font-size:22px;font-weight:700;color:#8a8a8a;">{a}</div>') for s,a,h in V.MEMBERS)+f'<div style="{cell}font-size:34px;color:{T["mute"]};">…</div>'
    par=''
    for n,src,word in V.PARTNERS:
        if src and word: par+=f'<div style="{cell}gap:10px;"><img src="{src}" alt="" style="height:42px;width:42px;object-fit:contain;"><span style="font-size:22px;font-weight:700;color:{INK};white-space:nowrap;">{word}</span></div>'
        elif src: par+=f'<div style="{cell}"><img src="{src}" alt="{n}" style="height:44px;max-width:80%;object-fit:contain;"></div>'
        else: par+=f'<div style="{cell}border:2px dashed #b9b4ae;box-sizing:border-box;font-size:19px;font-weight:600;color:#7a766f;white-space:nowrap;">{n} logo</div>'
    par+=f'<div style="{cell}font-size:34px;color:{T["mute"]};">…</div>'
    g=T['gap']
    return card(f'<div style="display:flex;flex-direction:column;gap:20px;"><div style="display:flex;justify-content:space-between;align-items:baseline;"><span style="font-size:26px;font-weight:700;color:{T["ink"]};">推送对象：社区成员来自</span>{lab("创业者 · 投资人 · 开发者 · OPC",T["mute"],17)}</div>'
                f'<div style="display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:{g}px;">{mem}</div></div>','32px 36px',T['wall_bg'],'margin-top:8px;')
def fixes():
    out=''
    for k,(si,bs,bl,items,res) in enumerate(V4.SOL):
        st,pain=V.STAGES[si][0],V.STAGES[si][1]
        li=''.join(f'<div style="display:flex;flex-direction:column;gap:4px;"><span style="font-size:27px;font-weight:700;color:{T["after_fg"]};">{t}</span><span style="font-size:23px;line-height:1.55;color:{T["after_mu"]};">{d}</span></div>' for t,d in items)
        before=(f'<div style="background:{T["before_bg"]};border-radius:{T["r"]}px;padding:36px;display:flex;flex-direction:column;gap:20px;">{lab("BEFORE · 现状",T["before_mu"])}'
                f'<div style="margin-top:auto;display:flex;flex-direction:column;gap:6px;"><span style="font-family:{T["df"]};font-size:76px;font-weight:{T["kw"]};line-height:.9;letter-spacing:-.04em;color:{T["before_fg"]};white-space:nowrap;">{bs}</span><span style="font-size:20px;color:{T["before_mu"]};">{bl}</span></div></div>')
        after=(f'<div style="background:{T["after_bg"]};border-radius:{T["r"]}px;{T["after_border"]}padding:36px;display:flex;flex-direction:column;gap:18px;">{lab("AFTER · "+V.BRAND,T["after_fg"])}{li}'
               f'<div style="margin-top:auto;{T["res_style"]}font-family:{T["df"]};font-size:38px;font-weight:{T["kw"]};letter-spacing:-.02em;line-height:1.2;">{res}</div></div>')
        arrow=f'<div style="display:flex;align-items:center;justify-content:center;"><svg width="44" height="24" viewBox="0 0 44 24" aria-hidden="true"><path d="M2 12h38M30 3l10 9-10 9" fill="none" stroke="{T["ink"]}" stroke-width="2.5"/></svg></div>'
        out+=(f'<div style="display:flex;flex-direction:column;gap:16px;"><div style="display:flex;justify-content:space-between;align-items:baseline;"><span style="font-family:{T["df"]};font-size:36px;font-weight:{T["kw"]};color:{T["ink"]};white-space:nowrap;">{"ABCD"[k]}　{pain}</span>{lab("环节 0"+str(si+1)+" · "+st,T["ink"])}</div>'
              f'<div style="display:grid;grid-template-columns:1fr 64px 1.5fr;gap:{T["gap"]}px;">{before}{arrow}{after}</div>{walls() if si==0 else ""}</div>')
    return f'<div style="display:flex;flex-direction:column;gap:56px;">{out}</div>'
def pts():
    return ''.join(card(f'<div style="display:flex;flex-direction:column;gap:12px;"><span style="font-family:{T["lf"]};font-size:20px;font-weight:700;color:{O};">0{i+1}</span><span style="font-family:{T["df"]};font-size:31px;font-weight:{T["kw"]};color:{T["ink"]};white-space:nowrap;">{t}</span><span style="font-size:22px;line-height:1.55;color:{T["body"]};">{d}</span></div>','30px') for i,(t,d) in enumerate(V4.PTS))
def build_theme(theme):
    global T; T=theme; P=T['pad']; W=1242-2*P
    panel_pad=40
    body=f'''{grain(.25,.85,9) if T.get("grain") else ""}
<div style="position:relative;padding:0 {P}px;display:flex;flex-direction:column;gap:{T["secgap"]}px;color:{T["ink"]};">
  {T["hero"](T)}
  <section style="display:flex;flex-direction:column;gap:44px;">{sechead("01","YOUR FUNNEL","活动转化漏斗")}
    <div style="background:{T["panel"]["bg"]};border-radius:{T["r"]}px;{T["panel"].get("border","")}padding:40px 0 24px {panel_pad}px;">{sankey(W-panel_pad-30)}</div>
    {kpis()}{conclusion()}
    <div style="font-size:20px;color:{T["mute"]};">黄 = 留下的人　灰 = 未到场　橙 = 到场后在跟进中流失　· 比例均为行业基准</div>
  </section>
  <section style="display:flex;flex-direction:column;gap:44px;">{sechead("02","BEFORE / AFTER","各环节解决方案")}{fixes()}</section>
  {T["foot"](T)}
</div>'''
    return body,T['bg'],T['tf']
def foot_block(T,bg,fg,mu,dark=False,radius='0',cta_bg=Y,cta_fg=INK,cta_r=20):
    P=T['pad']
    return (f'<section style="margin:0 -{P}px;background:{bg};color:{fg};border-radius:{radius};padding:96px {P}px 56px;display:flex;flex-direction:column;gap:28px;">'
            f'{eyebrow("03"+T["sep"]+"WAITLIST",mu)}<h2 style="margin:0;font-family:{T["df"]};font-size:84px;font-weight:{T["dw"]};line-height:1.05;letter-spacing:{T["dt"]};white-space:nowrap;">{V.OFFER_T}</h2>'
            f'<a href="https://example.com/waitlist" style="align-self:flex-start;margin-top:12px;display:inline-flex;align-items:center;height:92px;padding:0 56px;border-radius:{cta_r}px;background:{cta_bg};color:{cta_fg};font-size:30px;font-weight:700;text-decoration:none;">加入 waitlist</a>'
            f'<div style="margin-top:56px;border-top:1.5px solid {mu};padding-top:30px;display:flex;justify-content:space-between;align-items:center;">{logo(T,dark,60)}<span style="font-size:24px;color:{mu};">{V.SOURCES[:0]}</span></div></section>')
