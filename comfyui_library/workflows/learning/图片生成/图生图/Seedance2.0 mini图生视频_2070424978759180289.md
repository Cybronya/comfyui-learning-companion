---
key: 图片生成/图生图/Seedance2.0 mini图生视频_2070424978759180289.json
name: Seedance2.0 mini图生视频_2070424978759180289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Seedance2.0 mini图生视频_2070424978759180289.json
hash: 574e5383d0c36b66
coverage: 0.75
learned_at: 2026-10-09 22:09:16
nodes: [RH_RhartVideoSparkvideo20MiniImageToVideo, LoadImage, CR Text, SaveVideo]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Seedance2.0 mini图生视频_2070424978759180289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2070424978759180289.json`

## 结构

**生成流程**：Output → Other

**节点**（4 个）：
- `RH_RhartVideoSparkvideo20MiniImageToVideo`
- `LoadImage`
- `CR Text`
- `SaveVideo`

## 知识

覆盖率 **75%**（3/4）

**有卡**：`RH_RhartVideoSparkvideo20MiniImageToVideo`、`LoadImage`、`SaveVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、SaveVideo、RH_RhartVideoSparkvideo20MiniImageToVideo、sd15-t2i-basic、sd15-t2i-lora、Text、SaveImage、CS_Preview_Any

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
