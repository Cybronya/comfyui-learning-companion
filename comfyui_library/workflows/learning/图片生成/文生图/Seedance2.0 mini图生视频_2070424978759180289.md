---
key: 图片生成/文生图/Seedance2.0 mini图生视频_2070424978759180289.json
name: Seedance2.0 mini图生视频_2070424978759180289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Seedance2.0 mini图生视频_2070424978759180289.json
hash: 8e7522a9a85b8cc6
coverage: 0.25
learned_at: 2026-10-06 21:50:53
nodes: [RH_RhartVideoSparkvideo20MiniImageToVideo, LoadImage, CR Text, SaveVideo]
patterns: []
missing: [CR Text, RH_RhartVideoSparkvideo20MiniImageToVideo, SaveVideo]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `RH_RhartVideoSparkvideo20MiniImageToVideo` 知识库中没有该节点类型的任何知识, 次要节点 `SaveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Seedance2.0 mini图生视频_2070424978759180289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Seedance2.0 mini图生视频_2070424978759180289.json`

## 结构

**生成流程**：Other

**节点**（4 个）：
- `RH_RhartVideoSparkvideo20MiniImageToVideo`
- `LoadImage`
- `CR Text`
- `SaveVideo`

## 知识

覆盖率 **25%**（1/4）

**有卡**：`LoadImage`

**缺卡**（3）：`CR Text`、`RH_RhartVideoSparkvideo20MiniImageToVideo`、`SaveVideo`

**用到的条目**：LoadImage、sd15-t2i-basic、sd15-t2i-lora、SaveImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `RH_RhartVideoSparkvideo20MiniImageToVideo` 知识库中没有该节点类型的任何知识
- 次要节点 `SaveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明
