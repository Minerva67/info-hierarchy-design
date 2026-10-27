# info-hierarchy-design

Claude Code skill：给对外物料（B2B one-pager、合作长图、方案页、落地页首屏、小红书长图）做「信息组织 → 信息层级 → 每块可视化 → 选设计风格」，先把叙事和结构定下来再出视觉。

## 包含什么

- `SKILL.md`：完整流程
  - 动手前先写三行：给谁看 / 看完做什么 / 对方关心什么结果
  - 用读者自己的流程当骨架，每个环节挂「痛点 → 数据 → 方案 → 结果」
  - 三层信息层级，全页只用一处强调色
  - 按数据形状选可视化，结构定了再选风格（含 to B 风格筛选）
  - 文案口径：平实书面、只写读者得到什么、数字诚实、姿态对等
  - 反模式清单（实际踩过的坑）
- `references/viz-patterns.md`：连接条形漏斗、桑基流失图、Before/After 卡、五栏数据表、对账单、气泡图的实现要点
- `scripts/`：Claude Design 画板的生成与渲染脚本
  - `common.py` / `build.py`：共享外壳与构建
  - `render.py` / `fit.sh` / `measure.sh`：headless Chrome 本地渲染、自动定高
  - `th_b2b.py` + `th_b2b_themes.py`：同一份内容一次换皮出多版的主题引擎
  - `th_v3.py` / `th_v4.py`：Knock〃 商家 one-pager 的完整范例

## 安装

把本目录放到 `~/.claude/skills/info-hierarchy-design/`。

## 说明

- `render.py` 里的 blob → 本地文件映射和 `members.txt` 是 Knock〃 项目专用，换项目要改。
- 本仓库是本地 skill 的快照，真身在 `~/.claude/skills/info-hierarchy-design/`。
