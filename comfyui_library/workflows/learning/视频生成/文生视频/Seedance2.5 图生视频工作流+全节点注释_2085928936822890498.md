---
key: 视频生成/文生视频/Seedance2.5 图生视频工作流+全节点注释_2085928936822890498.json
name: Seedance2.5 图生视频工作流+全节点注释_2085928936822890498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.5 图生视频工作流+全节点注释_2085928936822890498.json
hash: 65244625e7815d35
coverage: 0.416667
learned_at: 2026-10-11 20:53:47
nodes: [LoadImage, JjkText, RH_BytedanceSeedance25TokenImageToVideo, SaveVideo, CR Text, Note, Note, Note, Note, LoadImage, LoadImage, Note]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Seedance2.5 图生视频工作流+全节点注释_2085928936822890498.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.5 图生视频工作流+全节点注释_2085928936822890498.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `LoadImage`
- `JjkText`
- `RH_BytedanceSeedance25TokenImageToVideo`
- `SaveVideo`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`

## 知识

覆盖率 **42%**（5/12）

**有卡**：`LoadImage`、`RH_BytedanceSeedance25TokenImageToVideo`、`SaveVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance25TokenImageToVideo、SaveVideo、sd15-t2i-basic、sd15-t2i-lora、Seed、Text、sampler_name 调整经验

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
