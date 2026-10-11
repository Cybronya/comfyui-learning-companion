---
key: 视频生成/文生视频/Seedance+2.0+真人短片生成器（高速满血版）_2038240207052480514.json
name: Seedance+2.0+真人短片生成器（高速满血版）_2038240207052480514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance+2.0+真人短片生成器（高速满血版）_2038240207052480514.json
hash: f4be4883e1786745
coverage: 0.857143
learned_at: 2026-10-11 03:48:37
nodes: [SaveVideo, LoadAudio, LoadVideo, RH_RhartVideoSparkvideo20MultimodalVideo, LoadImage, LoadImage, Primitive string multiline [Crystools]]
patterns: []
missing: [Primitive string multiline [Crystools]]
discoveries: [次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Seedance+2.0+真人短片生成器（高速满血版）_2038240207052480514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance+2.0+真人短片生成器（高速满血版）_2038240207052480514.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `SaveVideo`
- `LoadAudio`
- `LoadVideo`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `LoadImage`
- `LoadImage`
- `Primitive string multiline [Crystools]`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`SaveVideo`、`LoadAudio`、`LoadVideo`、`RH_RhartVideoSparkvideo20MultimodalVideo`、`LoadImage`

**缺卡**（1）：`Primitive string multiline [Crystools]`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、sd15-t2i-basic、sd15-t2i-lora、String

## 学习发现

- 次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识
