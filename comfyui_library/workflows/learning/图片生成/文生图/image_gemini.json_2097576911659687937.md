---
key: 图片生成/文生图/image_gemini.json_2097576911659687937.json
name: image_gemini.json_2097576911659687937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image_gemini.json_2097576911659687937.json
hash: 9372a32219464ad6
coverage: 0.5
learned_at: 2026-10-20 01:35:07
nodes: [JjkText, JjkText, JjkText, JjkText, LayerUtility: TextJoin, LayerUtility: TextJoin, RH_Nano_Banana2_Gemini31Flash, JjkText, SaveImage, LoadImage, easy promptList, PrimitiveNode]
patterns: []
missing: []
---

# 图片生成/文生图/image_gemini.json_2097576911659687937.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image_gemini.json_2097576911659687937.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `LayerUtility: TextJoin`
- `LayerUtility: TextJoin`
- `RH_Nano_Banana2_Gemini31Flash`
- `JjkText`
- `SaveImage`
- `LoadImage`
- `easy promptList`
- `PrimitiveNode`

## 知识

覆盖率 **50%**（6/12）

**有卡**：`LayerUtility: TextJoin`、`RH_Nano_Banana2_Gemini31Flash`、`SaveImage`、`LoadImage`、`easy promptList`

**用到的条目**：LoadImage、easy promptList、SaveImage、RH_Nano_Banana2_Gemini31Flash、LayerUtility: TextJoin、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
