---
key: 图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json
name: ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json
hash: 3336c6055daff93c
coverage: 0.9375
learned_at: 2026-10-19 22:15:36
nodes: [EmptySD3LatentImage, VAELoader, Note, VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, ModelSamplingAuraFlow, KSampler, LoraLoaderModelOnly, ClipLoaderGGUF, TTResolutionSelector, CR Text, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 737399316097438, "steps": 10}
---

# 图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `EmptySD3LatentImage`
- `VAELoader`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ClipLoaderGGUF`
- `TTResolutionSelector`
- `CR Text`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `737399316097438`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`EmptySD3LatentImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingAuraFlow`、`KSampler`、`ClipLoaderGGUF`、`TTResolutionSelector`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CLIPLoaderGGUF、ClipLoaderGGUF
