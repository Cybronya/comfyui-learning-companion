---
key: 视频生成/文生视频/全能视频X-V1.5 文生视频-RH低价渠道版_2061189140082946049.json
name: 全能视频X-V1.5 文生视频-RH低价渠道版_2061189140082946049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频X-V1.5 文生视频-RH低价渠道版_2061189140082946049.json
hash: 26b5d2748aaab603
coverage: 0.5
learned_at: 2026-10-11 19:49:47
nodes: [SaveVideo, CR Text, RH_RhartVideoGOfficialTextToVideo, PreviewAny, RH_RhartVideoGTextToVideo, PreviewAny]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/全能视频X-V1.5 文生视频-RH低价渠道版_2061189140082946049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频X-V1.5 文生视频-RH低价渠道版_2061189140082946049.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `SaveVideo`
- `CR Text`
- `RH_RhartVideoGOfficialTextToVideo`
- `PreviewAny`
- `RH_RhartVideoGTextToVideo`
- `PreviewAny`

## 知识

覆盖率 **50%**（3/6）

**有卡**：`SaveVideo`、`RH_RhartVideoGOfficialTextToVideo`、`RH_RhartVideoGTextToVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：SaveVideo、RH_RhartVideoGTextToVideo、RH_RhartVideoGOfficialTextToVideo、sd15-t2i-basic、sd15-t2i-lora、Text、SaveImage、CS_Preview_Any

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
