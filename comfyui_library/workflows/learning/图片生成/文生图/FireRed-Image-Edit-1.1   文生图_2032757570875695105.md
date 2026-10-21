---
key: 图片生成/文生图/FireRed-Image-Edit-1.1   文生图_2032757570875695105.json
name: FireRed-Image-Edit-1.1   文生图_2032757570875695105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FireRed-Image-Edit-1.1   文生图_2032757570875695105.json
hash: 291a1cb005241dec
coverage: 0.8125
learned_at: 2026-10-21 02:52:01
nodes: [PreviewImage, UpscaleModelLoader, UltimateSDUpscale, PreviewImage, ModelSamplingAuraFlow, CLIPLoader, VAELoader, EmptySD3LatentImage, KSampler (Efficient), CLIPTextEncode, UNETLoader_Any, LoraLoaderModelOnly, CLIPTextEncode, Note, SaveImage, LayerFilter: HDREffects]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 937502736318774, "steps": 8}
---

# 图片生成/文生图/FireRed-Image-Edit-1.1   文生图_2032757570875695105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FireRed-Image-Edit-1.1   文生图_2032757570875695105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（16 个）：
- `PreviewImage`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `KSampler (Efficient)` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader_Any` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `SaveImage`
- `LayerFilter: HDREffects`

## 关键参数

- `seed` = `937502736318774`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`UpscaleModelLoader`、`UltimateSDUpscale`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`EmptySD3LatentImage`、`KSampler (Efficient)`、`CLIPTextEncode`、`UNETLoader_Any`、`LoraLoaderModelOnly`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、KSampler (Efficient)、UltimateSDUpscale、UpscaleModelLoader、UpscaleModelLoader
