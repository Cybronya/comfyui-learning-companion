---
key: 图片生成/文生图/Seedance 1.5 Pro Fast｜文生视频｜支持1080P_2097534454628700162.json
name: Seedance 1.5 Pro Fast｜文生视频｜支持1080P_2097534454628700162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Seedance 1.5 Pro Fast｜文生视频｜支持1080P_2097534454628700162.json
hash: 225bc956f4a7f18f
coverage: 0.666667
learned_at: 2026-10-06 22:58:54
nodes: [MuyeTextEditOutput, SaveVideo, RH_SeedanceV15ProTextToVideoFast]
patterns: []
missing: [RH_SeedanceV15ProTextToVideoFast]
discoveries: [次要节点 `RH_SeedanceV15ProTextToVideoFast` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Seedance 1.5 Pro Fast｜文生视频｜支持1080P_2097534454628700162.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Seedance 1.5 Pro Fast｜文生视频｜支持1080P_2097534454628700162.json`

## 结构

**生成流程**：Output → Other

**节点**（3 个）：
- `MuyeTextEditOutput`
- `SaveVideo`
- `RH_SeedanceV15ProTextToVideoFast`

## 知识

覆盖率 **67%**（2/3）

**有卡**：`MuyeTextEditOutput`、`SaveVideo`

**缺卡**（1）：`RH_SeedanceV15ProTextToVideoFast`

**用到的条目**：MuyeTextEditOutput、SaveVideo、sd15-t2i-basic、sd15-t2i-lora、Text、sampler_name 调整经验、steps 调整经验、cfg 调整经验

## 学习发现

- 次要节点 `RH_SeedanceV15ProTextToVideoFast` 仅有 KSampler 的通用知识，没有该节点自己的说明
