---
key: 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imagebaseZIB模型_2026178597890826241.json
name: SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imagebaseZIB模型_2026178597890826241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imagebaseZIB模型_2026178597890826241.json
hash: 416eed28ce81d9be
coverage: 0.8
learned_at: 2026-10-19 22:29:53
nodes: [PrimitiveStringMultiline, SaveImage, Note, WujiStyleSelector, RHHiddenNodes, ShowText|pysssss, WujiUpscaler, WujiCleaner, VAEDecode, WujiEditor, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, ClownsharKSampler_Beta]
patterns: []
missing: []
parameters: {"cfg": 8, "checkpoint": "WuJi_Z-image-base多风格2603_.safetensors", "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imagebaseZIB模型_2026178597890826241.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imagebaseZIB模型_2026178597890826241.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `PrimitiveStringMultiline`
- `SaveImage`
- `Note`
- `WujiStyleSelector`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `WujiUpscaler`
- `WujiCleaner`
- `VAEDecode` ★核心
- `WujiEditor`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ClownsharKSampler_Beta` ★核心

## 关键参数

- `checkpoint` = `WuJi_Z-image-base多风格2603_.safetensors`
- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`SaveImage`、`WujiStyleSelector`、`RHHiddenNodes`、`WujiUpscaler`、`WujiCleaner`、`VAEDecode`、`WujiEditor`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`ClownsharKSampler_Beta`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ClownsharKSampler_Beta、WujiStyleSelector、WujiUpscaler、SaveImage、ModelSamplingAuraFlow
