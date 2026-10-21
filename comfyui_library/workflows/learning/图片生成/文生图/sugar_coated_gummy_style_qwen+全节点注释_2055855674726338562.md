---
key: 图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json
name: sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json
hash: 35e281a3850ce6bf
coverage: 0.538462
learned_at: 2026-10-21 02:57:38
nodes: [VAELoader, CLIPLoader, EmptySD3LatentImage, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, StringConcatenate, SaveImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 203443699370811, "steps": 25}
---

# 图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `StringConcatenate`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `203443699370811`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（14/26）

**有卡**：`VAELoader`、`CLIPLoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`StringConcatenate`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
