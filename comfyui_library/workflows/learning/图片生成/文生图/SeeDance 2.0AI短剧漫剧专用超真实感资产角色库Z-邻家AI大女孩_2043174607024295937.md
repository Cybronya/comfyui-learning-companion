---
key: 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-邻家AI大女孩_2043174607024295937.json
name: SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-邻家AI大女孩_2043174607024295937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-邻家AI大女孩_2043174607024295937.json
hash: c2adff36025ddf56
coverage: 0.785714
learned_at: 2026-10-21 02:55:05
nodes: [CheckpointLoaderSimple, PortraitMaster_中文版, WujiSampler, WujiCleaner, PrimitiveStringMultiline, Note, WujiStyleSelector, WujiEditor, WujiUpscaler, RHHiddenNodes, ShowText|pysssss, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"checkpoint": "WuJi_Z-image-base多风格2603_.safetensors"}
---

# 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-邻家AI大女孩_2043174607024295937.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-邻家AI大女孩_2043174607024295937.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（14 个）：
- `CheckpointLoaderSimple` ★核心
- `PortraitMaster_中文版`
- `WujiSampler` ★核心
- `WujiCleaner`
- `PrimitiveStringMultiline`
- `Note`
- `WujiStyleSelector`
- `WujiEditor`
- `WujiUpscaler`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `checkpoint` = `WuJi_Z-image-base多风格2603_.safetensors`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`CheckpointLoaderSimple`、`PortraitMaster_中文版`、`WujiSampler`、`WujiCleaner`、`WujiStyleSelector`、`WujiEditor`、`WujiUpscaler`、`RHHiddenNodes`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、WujiSampler、WujiStyleSelector、WujiUpscaler、SaveImage、RHHiddenNodes、WujiCleaner
