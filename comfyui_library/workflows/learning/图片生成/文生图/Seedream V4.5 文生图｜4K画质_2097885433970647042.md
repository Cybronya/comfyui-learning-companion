---
key: Seedream V4.5 文生图｜4K画质_2097885433970647042.json
name: Seedream V4.5 文生图｜4K画质_2097885433970647042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Seedream V4.5 文生图｜4K画质_2097885433970647042.json
hash: 56ab38b0c8ee806f
coverage: 0.333333
learned_at: 2026-10-10 20:59:12
nodes: [SaveImage, RH_SeedreamV45TextToImage, PreviewImage]
patterns: []
missing: [RH_SeedreamV45TextToImage]
discoveries: [次要节点 `RH_SeedreamV45TextToImage` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# Seedream V4.5 文生图｜4K画质_2097885433970647042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Seedream V4.5 文生图｜4K画质_2097885433970647042.json`

## 结构

**生成流程**：Output → Other

**节点**（3 个）：
- `SaveImage`
- `RH_SeedreamV45TextToImage`
- `PreviewImage`

## 知识

覆盖率 **33%**（1/3）

**有卡**：`SaveImage`

**缺卡**（1）：`RH_SeedreamV45TextToImage`

**用到的条目**：SaveImage、sd15-t2i-basic、sd15-t2i-lora、Seed、Text、sampler_name 调整经验、steps 调整经验、cfg 调整经验

## 学习发现

- 次要节点 `RH_SeedreamV45TextToImage` 仅有 KSampler 的通用知识，没有该节点自己的说明
