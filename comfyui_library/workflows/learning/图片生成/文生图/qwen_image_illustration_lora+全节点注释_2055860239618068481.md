---
key: 图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json
name: qwen_image_illustration_lora+全节点注释_2055860239618068481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json
hash: 1c3c8cc8469e6da9
coverage: 0.541667
learned_at: 2026-10-21 02:57:37
nodes: [VAELoader, CLIPLoader, EmptySD3LatentImage, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, SaveImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 543688720796557, "steps": 45}
---

# 图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAELoader`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
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
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `543688720796557`
- `steps` = `45`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（13/24）

**有卡**：`VAELoader`、`CLIPLoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
