import th_b2b as B
from th_b2b import Y, O, INK
import content as V
TITLE='<br>'.join(V.TITLE)
def ptsgrid(T): return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:{T["gap"]}px;">{B.pts()}</div>'
def hero_pub(T):
    return f'''<section style="position:relative;padding-top:56px;display:flex;flex-direction:column;gap:44px;">
    <div style="display:flex;justify-content:space-between;align-items:center;">{B.logo(T,False,80)}<span style="font-size:24px;font-weight:600;background:#fff;border-radius:999px;padding:14px 30px;">商家合作</span></div>
    <div style="position:relative;height:440px;">
      <div style="position:absolute;right:10px;top:0;width:420px;height:420px;border-radius:999px;background:{Y};display:flex;align-items:center;justify-content:center;">{B.mark(210)}</div>
      <div style="position:absolute;right:400px;top:270px;width:150px;height:150px;border-radius:999px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:700;letter-spacing:.06em;text-align:center;line-height:1.3;">FOR B2B<br>EVENT<br>HOSTS</div>
      <svg width="1130" height="440" viewBox="0 0 1130 440" aria-hidden="true" style="position:absolute;inset:0;"><path d="M-20 400 C 260 480, 520 100, 900 30" fill="none" stroke="{O}" stroke-width="3"/></svg>
    </div>
    <h1 style="margin:-20px 0 10px;font-family:{T["df"]};font-size:108px;font-weight:500;line-height:1.02;letter-spacing:-.03em;white-space:nowrap;">{TITLE}</h1>
    {ptsgrid(T)}</section>'''
def hero_edit(T):
    return f'''<section style="position:relative;padding-top:56px;display:flex;flex-direction:column;gap:48px;">
    <div style="display:flex;justify-content:space-between;align-items:center;padding-bottom:26px;border-bottom:1.5px solid {INK};">{B.logo(T,False,76)}{B.lab("For B2B event hosts · 商家合作",INK,20)}</div>
    <div style="display:grid;grid-template-columns:1fr auto;align-items:end;gap:40px;margin-top:70px;">
      <h1 style="margin:0;font-family:{T["df"]};font-size:100px;font-weight:400;line-height:1.05;letter-spacing:-.03em;white-space:nowrap;">{V.TITLE[0]}<br><em style="font-weight:300;">{V.TITLE[1]}</em></h1>
      {B.mark(150)}</div>
    {ptsgrid(T)}</section>'''
def hero_dark(T):
    return f'''<section style="position:relative;padding-top:56px;display:flex;flex-direction:column;gap:44px;">
    <div style="display:flex;justify-content:space-between;align-items:center;padding-bottom:28px;border-bottom:1.5px solid {T["line"]};">{B.logo(T,True,76)}{B.lab("For B2B event hosts · 商家合作",T["ink"],20)}</div>
    <div style="display:flex;flex-direction:column;gap:20px;margin-top:70px;">{B.lab("// 每一场活动",T["mute"],20)}
      <h1 style="margin:0;font-family:{T["df"]};font-size:108px;font-weight:600;line-height:1.02;letter-spacing:-.04em;white-space:nowrap;">{V.TITLE[0]}<br><span style="color:{Y};">{V.TITLE[1]}</span></h1></div>
    {ptsgrid(T)}</section>'''
def hero_cohere(T):
    return f'''<section style="position:relative;padding-top:56px;display:flex;flex-direction:column;gap:56px;">
    <div style="display:flex;justify-content:space-between;align-items:center;">{B.logo(T,False,76)}<span style="font-size:22px;font-weight:500;background:{INK};color:#fff;border-radius:32px;padding:14px 30px;">商家合作</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:30px;text-align:center;margin-top:80px;">{B.lab("For B2B event hosts",T["mute"],19)}
      <h1 style="margin:0;font-family:{T["df"]};font-size:110px;font-weight:400;line-height:1;letter-spacing:-.045em;white-space:nowrap;">{TITLE}</h1></div>
    <div style="margin-top:30px;">{ptsgrid(T)}</div></section>'''
def hero_intercom(T):
    return f'''<section style="position:relative;padding-top:52px;display:flex;flex-direction:column;gap:48px;">
    <div style="display:flex;justify-content:space-between;align-items:center;">{B.logo(T,False,76)}<span style="font-size:22px;font-weight:500;background:{INK};color:#fff;border-radius:8px;padding:14px 26px;">商家合作</span></div>
    <div style="display:flex;flex-direction:column;gap:26px;margin-top:70px;">{B.lab("For B2B event hosts",T["mute"],22)}
      <h1 style="margin:0;font-family:{T["df"]};font-size:108px;font-weight:500;line-height:1.04;letter-spacing:-.035em;white-space:nowrap;">{TITLE}</h1></div>
    {ptsgrid(T)}</section>'''
base=dict(upper=False,dot=False,grain=False,kpi_worst=INK,kpi_worst_dark=True,logo_border='',after_border='')
PUB=dict(base,bg='#f3f0ee',ink=INK,body='#262627',mute='#696969',line='#d1cdc7',surf='#ffffff',r=40,border='',
 df="'Sofia Sans','PingFang SC','Noto Sans SC',sans-serif",tf="'Sofia Sans','PingFang SC','Noto Sans SC',sans-serif",lf="'Sofia Sans','PingFang SC',sans-serif",
 ls=19,lw=700,lt='.06em',upper=True,dot=True,eb=INK,sep=' · ',h2=72,dw=500,dt='-.02em',kw=700,gap=16,pad=56,secgap=130,
 panel=dict(bg='#ffffff',dash='#b9b4ae',main=Y,drop='#ddd6cf',node=INK,text=INK,mute='#696969'),
 concl='background:#fff;border-radius:40px;padding:40px 48px;',concl_fg=INK,concl_mu='#696969',
 before_bg='#e7e2dd',before_fg=INK,before_mu='#696969',after_bg=Y,after_fg=INK,after_mu='#262627',res_style=f'border-top:2px solid {INK};padding-top:18px;color:{INK};',
 wall_bg='#e7e2dd',hero=hero_pub,kpi_worst_dark=False,foot=lambda T:B.foot_block(T,'#ffffff',INK,'#696969',False,'80px 80px 0 0',Y,INK,20))
EDIT=dict(base,bg='#faf9f5',ink=INK,body='#3d3d3a',mute='#5e5d59',line='#d8d3c8',surf='#f0eee6',r=16,border='',
 df="'Newsreader','Noto Serif SC',serif",tf="'PingFang SC','Noto Sans SC',sans-serif",lf="'Special Elite','Courier Prime',monospace",
 ls=19,lw=400,lt='.06em',eb='#5e5d59',sep=' · ',h2=72,dw=400,dt='-.02em',kw=500,gap=16,pad=64,secgap=130,
 panel=dict(bg='#f0eee6',dash='#b8b2a5',main=Y,drop='#d8d2c4',node=INK,text=INK,mute='#5e5d59'),
 concl=f'border-top:1.5px solid {INK};border-bottom:1.5px solid {INK};padding:36px 0;',concl_fg=INK,concl_mu='#5e5d59',
 before_bg='#e8e4da',before_fg='#3d3d3a',before_mu='#5e5d59',after_bg='#ffffff',after_border=f'border:1.5px solid {INK};',after_fg=INK,after_mu='#3d3d3a',
 res_style=f'align-self:flex-start;background:linear-gradient(transparent 55%, {Y} 55%);color:{INK};',
 wall_bg='#f0eee6',hero=hero_edit,kpi_worst_dark=False,foot=lambda T:B.foot_block(T,'#f0eee6',INK,'#5e5d59',False,'0',Y,INK,8))
DARK=dict(base,bg=INK,ink='#f3ece3',body='#cfcac2',mute='#a19d96',line='#2e302f',surf='#1d1f1e',r=0,border='border:1.5px solid #2e302f;',
 df="'Outfit','PingFang SC','Noto Sans SC',sans-serif",tf="'Outfit','PingFang SC','Noto Sans SC',sans-serif",lf="'JetBrains Mono','Courier Prime',monospace",
 ls=18,lw=500,lt='.06em',upper=True,eb=Y,sep=' / ',h2=68,dw=600,dt='-.02em',kw=700,gap=12,pad=56,secgap=120,
 panel=dict(bg='#1d1f1e',border='border:1.5px solid #2e302f;',dash='#5e5d59',main=Y,drop='#5a5c5b',node='#f3ece3',text='#f3ece3',mute='#a19d96',mainfg=INK),
 kpi_worst='#3a2418',concl='background:#1d1f1e;border:1.5px solid #2e302f;padding:40px 44px;',concl_fg='#f3ece3',concl_mu='#a19d96',
 before_bg='#1d1f1e',before_fg='#a19d96',before_mu='#a19d96',after_bg=Y,after_fg=INK,after_mu='#2a2620',res_style=f'border-top:2px solid {INK};padding-top:18px;color:{INK};',
 wall_bg='#1d1f1e',hero=hero_dark,foot=lambda T:B.foot_block(T,'#1d1f1e','#f3ece3','#a19d96',True,'0',Y,INK,0))
COHERE=dict(base,bg='#ffffff',ink=INK,body='#212121',mute='#75758a',line='#d9d9dd',surf='#eeece7',r=22,border='',
 df="'Space Grotesk','PingFang SC','Noto Sans SC',sans-serif",tf="'Inter','PingFang SC','Noto Sans SC',sans-serif",lf="'JetBrains Mono',monospace",
 ls=18,lw=400,lt='.08em',upper=True,eb='#75758a',sep=' — ',h2=76,dw=400,dt='-.03em',kw=500,gap=16,pad=64,secgap=150,
 panel=dict(bg='#eeece7',dash='#b5b2aa',main=Y,drop='#d6d3cb',node=INK,text=INK,mute='#75758a'),
 concl='background:#eeece7;border-radius:22px;padding:40px 44px;',concl_fg=INK,concl_mu='#75758a',
 before_bg='#eeece7',before_fg=INK,before_mu='#75758a',after_bg=Y,after_fg=INK,after_mu='#2a2620',res_style=f'border-top:1px solid {INK};padding-top:18px;color:{INK};',
 wall_bg='#eeece7',hero=hero_cohere,kpi_worst_dark=False,foot=lambda T:B.foot_block(T,'#eeece7',INK,'#75758a',False,'22px 22px 0 0',Y,INK,32))
INTERCOM=dict(base,bg='#f5f1ec',ink=INK,body='#3a3a38',mute='#626260',line='#d3cec6',surf='#ffffff',r=14,border='',
 df="'Onest','PingFang SC','Noto Sans SC',sans-serif",tf="'Onest','PingFang SC','Noto Sans SC',sans-serif",lf="'Onest','PingFang SC',sans-serif",
 ls=19,lw=500,lt='0',eb='#626260',sep=' · ',h2=70,dw=500,dt='-.02em',kw=600,gap=14,pad=60,secgap=130,
 panel=dict(bg='#ffffff',dash='#d3cec6',main=Y,drop='#e3ddd4',node=INK,text=INK,mute='#626260'),
 concl='background:#fff;border-radius:16px;padding:40px 44px;',concl_fg=INK,concl_mu='#626260',
 before_bg='#ebe7e1',before_fg=INK,before_mu='#626260',after_bg='#ffffff',after_border=f'border:1.5px solid {INK};',after_fg=INK,after_mu='#3a3a38',
 res_style=f'border-top:1px solid #d3cec6;padding-top:18px;color:{O};',
 wall_bg='#ebe7e1',hero=hero_intercom,kpi_worst_dark=False,foot=lambda T:B.foot_block(T,'#ffffff',INK,'#626260',False,'0',Y,INK,8))
