# 渲染与定高（Claude Design 画板）

做法（2026-10-26 实测可用）：
1. `common.py` 放共享文案和 `page()` 外壳；每个主题一个 `th_xxx.py`，提供 `build() -> (body, bg, font)`。
2. `render.py`：把 `/_blob/<id>` 换成本地文件路径，去掉 `<x-dc>` 和 `<helmet>`，再用 `Google Chrome --headless=new --screenshot` 截全图。
3. `fit.sh`：先关掉纸纹（设 `NOGRAIN=1`，否则纸纹铺满整页，量不出底边），按 9000 高渲染；从底部往上找到第一行与底色不同的像素，就是内容底边；用这个高度重新生成，并同时写回根节点高度和 `$preview`。
4. 切成每段约 1900px 的图预览，逐段检查溢出和断行。

脚本已复制在本目录：common.py / build.py / render.py（blob→本地映射是 Knock 商家 one-pager 专用，换项目要改 M 表）/ fit.sh / measure.sh；th_v3.py 是刊物风格的完整范例（2026-10-26 商家 one-pager v3）。用法：bash fit.sh <outdir> <Name>:<module>
