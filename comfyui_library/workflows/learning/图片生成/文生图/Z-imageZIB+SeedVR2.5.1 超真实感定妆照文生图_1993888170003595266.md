---
key: 图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_1993888170003595266.json
name: Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_1993888170003595266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_1993888170003595266.json
hash: a48fa61b5a5e6494
coverage: 0.8
learned_at: 2026-10-19 21:32:59
nodes: [PrimitiveStringMultiline, Note, RHHiddenNodes, ShowText|pysssss, WujiEditor, VAEDecode, WujiCleaner, WujiUpscaler, WujiStyleSelector, ModelSamplingAuraFlow, CheckpointLoaderSimple, LoraLoaderModelOnly, ClownsharKSampler_Beta, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "checkpoint": "WuJi_Z-image-base多风格2603_.safetensors", "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_1993888170003595266.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_1993888170003595266.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `PrimitiveStringMultiline`
- `Note`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `WujiEditor`
- `VAEDecode` ★核心
- `WujiCleaner`
- `WujiUpscaler`
- `WujiStyleSelector`
- `ModelSamplingAuraFlow`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `ClownsharKSampler_Beta` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

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

**有卡**：`RHHiddenNodes`、`WujiEditor`、`VAEDecode`、`WujiCleaner`、`WujiUpscaler`、`WujiStyleSelector`、`ModelSamplingAuraFlow`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`ClownsharKSampler_Beta`、`SaveImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ClownsharKSampler_Beta、WujiStyleSelector、WujiUpscaler、SaveImage、ModelSamplingAuraFlow
