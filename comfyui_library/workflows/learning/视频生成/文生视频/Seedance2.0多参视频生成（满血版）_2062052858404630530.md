---
key: 视频生成/文生视频/Seedance2.0多参视频生成（满血版）_2062052858404630530.json
name: Seedance2.0多参视频生成（满血版）_2062052858404630530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.0多参视频生成（满血版）_2062052858404630530.json
hash: 1c33f12613adad7f
coverage: 0.625
learned_at: 2026-10-11 20:21:30
nodes: [SaveVideo, RH_BytedanceSeedance20GlobalMultimodalVideo, LoadImage, CR Prompt Text, LoadImage, Note, LoadVideo, Note]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Seedance2.0多参视频生成（满血版）_2062052858404630530.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.0多参视频生成（满血版）_2062052858404630530.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `SaveVideo`
- `RH_BytedanceSeedance20GlobalMultimodalVideo`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `Note`
- `LoadVideo`
- `Note`

## 知识

覆盖率 **62%**（5/8）

**有卡**：`SaveVideo`、`RH_BytedanceSeedance20GlobalMultimodalVideo`、`LoadImage`、`LoadVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance20GlobalMultimodalVideo、SaveVideo、LoadVideo、sd15-t2i-basic、sd15-t2i-lora、Seed、Text

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
