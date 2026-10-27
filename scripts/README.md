# 脚本用法

```
scripts/
  content.py          # 你的内容：环节、痛点、基准、方案、结果、卖点（只改这个）
  common.py           # 配色（Y/O/INK）、字体、纸纹、画板外壳
  th_b2b.py           # 主题引擎：桑基漏斗、KPI、结论、Before/After、logo 墙
  th_b2b_themes.py    # 5 套主题参数：PUB / EDIT / DARK / COHERE / INTERCOM
  theme_*.py          # 每套主题的入口
  build.py fit.sh render.py measure.sh   # 构建、渲染、自动定高
```

```bash
cd scripts
bash fit.sh out "MyPage:theme_pub"      # 输出 out/MyPage.dc.html 和 out/MyPage.png
```

- 需要本机有 Chrome（或用环境变量 `CHROME` 指定路径）和 Python 3 + Pillow。
- 输出的 `.dc.html` 是 Claude Design 画板格式；`.png` 可直接发社媒。
- 换品牌色：改 `common.py` 里的 `Y / O / INK`；换主题细节：改 `th_b2b_themes.py` 里对应的 dict。
- 图片素材：放进 `scripts/assets/`，在 `blobmap.json` 里写 `{"<blob id>": "文件名"}`，本地渲染时会自动替换。
