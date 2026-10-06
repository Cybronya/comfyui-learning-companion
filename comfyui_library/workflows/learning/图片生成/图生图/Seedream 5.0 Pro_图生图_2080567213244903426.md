---
key: 图片生成/图生图/Seedream 5.0 Pro_图生图_2080567213244903426.json
name: Seedream 5.0 Pro_图生图_2080567213244903426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Seedream 5.0 Pro_图生图_2080567213244903426.json
hash: ceb3440ee40a2b1a
coverage: 0.75
learned_at: 2026-10-07 02:41:31
nodes: [SaveImage, Text, RH_SeedreamV5ProImageToImage, LoadImage]
patterns: []
missing: [RH_SeedreamV5ProImageToImage]
discoveries: [次要节点 `RH_SeedreamV5ProImageToImage` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Seedream 5.0 Pro_图生图_2080567213244903426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Seedream 5.0 Pro_图生图_2080567213244903426.json`

## 结构

**生成流程**：Output → Other

**节点**（4 个）：
- `SaveImage`
- `Text`
- `RH_SeedreamV5ProImageToImage`
- `LoadImage`

## 知识

覆盖率 **75%**（3/4）

**有卡**：`SaveImage`、`Text`、`LoadImage`

**缺卡**（1）：`RH_SeedreamV5ProImageToImage`

**用到的条目**：LoadImage、SaveImage、Text、sd15-t2i-basic、sd15-t2i-lora、sampler_name 调整经验、steps 调整经验、cfg 调整经验

## 学习发现

- 次要节点 `RH_SeedreamV5ProImageToImage` 仅有 KSampler 的通用知识，没有该节点自己的说明
