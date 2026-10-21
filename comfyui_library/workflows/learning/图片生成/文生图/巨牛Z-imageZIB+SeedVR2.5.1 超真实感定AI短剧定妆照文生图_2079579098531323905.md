---
key: 图片生成/文生图/巨牛Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2079579098531323905.json
name: 巨牛Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2079579098531323905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/巨牛Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2079579098531323905.json
hash: 087109f6b965204b
coverage: 0.8125
learned_at: 2026-10-20 00:40:25
nodes: [Note, RHHiddenNodes, VAEDecode, WujiCleaner, WujiUpscaler, ModelSamplingAuraFlow, LoraLoaderModelOnly, ClownsharKSampler_Beta, SaveImage, LoraLoaderModelOnly, WujiEditor, CheckpointLoaderSimple, ClipLoaderGGUF, WujiStyleSelector, ShowText|pysssss, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 8, "checkpoint": "WuJi_Z-image-base多风格2603_.safetensors", "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/文生图/巨牛Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2079579098531323905.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/巨牛Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2079579098531323905.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `Note`
- `RHHiddenNodes`
- `VAEDecode` ★核心
- `WujiCleaner`
- `WujiUpscaler`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `ClownsharKSampler_Beta` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `WujiEditor`
- `CheckpointLoaderSimple` ★核心
- `ClipLoaderGGUF`
- `WujiStyleSelector`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`
- `checkpoint` = `WuJi_Z-image-base多风格2603_.safetensors`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`RHHiddenNodes`、`VAEDecode`、`WujiCleaner`、`WujiUpscaler`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`ClownsharKSampler_Beta`、`SaveImage`、`WujiEditor`、`CheckpointLoaderSimple`、`ClipLoaderGGUF`、`WujiStyleSelector`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ClownsharKSampler_Beta、WujiStyleSelector、WujiUpscaler、CLIPLoaderGGUF、ClipLoaderGGUF
