---
key: 图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2003676950780624897.json
name: Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2003676950780624897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2003676950780624897.json
hash: 87ee559b04385251
coverage: 0.8125
learned_at: 2026-10-19 21:47:10
nodes: [PrimitiveStringMultiline, Note, RHHiddenNodes, ShowText|pysssss, VAEDecode, WujiCleaner, WujiUpscaler, WujiStyleSelector, ModelSamplingAuraFlow, LoraLoaderModelOnly, ClownsharKSampler_Beta, SaveImage, LoraLoaderModelOnly, WujiEditor, CheckpointLoaderSimple, ClipLoaderGGUF]
patterns: []
missing: []
parameters: {"cfg": 8, "checkpoint": "WuJi_Z-image-base多风格2603_.safetensors", "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2003676950780624897.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2003676950780624897.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `PrimitiveStringMultiline`
- `Note`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `WujiCleaner`
- `WujiUpscaler`
- `WujiStyleSelector`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `ClownsharKSampler_Beta` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `WujiEditor`
- `CheckpointLoaderSimple` ★核心
- `ClipLoaderGGUF`

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

**有卡**：`RHHiddenNodes`、`VAEDecode`、`WujiCleaner`、`WujiUpscaler`、`WujiStyleSelector`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`ClownsharKSampler_Beta`、`SaveImage`、`WujiEditor`、`CheckpointLoaderSimple`、`ClipLoaderGGUF`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ClownsharKSampler_Beta、WujiStyleSelector、WujiUpscaler、CLIPLoaderGGUF、ClipLoaderGGUF
