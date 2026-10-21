---
key: 图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json
name: Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json
hash: c4385aa4378f54ce
coverage: 0.8125
learned_at: 2026-10-21 02:54:21
nodes: [UNETLoader, QwenImage21Cache, CLIPLoader, LoraLoaderModelOnly, VAELoader, VAEDecode, SaveImage, PreviewImage, Note, TextEncodeQwenImage21, CR Text Concatenate, MuyeTextEditOutput, LoadImage, KSampler, PrimitiveStringMultiline, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1600, "sampler_name": "euler", "scheduler": "simple", "seed": 314454577880058, "steps": 25, "width": 1200}
---

# 图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `Note`
- `TextEncodeQwenImage21`
- `CR Text Concatenate`
- `MuyeTextEditOutput`
- `LoadImage`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心

## 关键参数

- `seed` = `314454577880058`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`CR Text Concatenate`、`MuyeTextEditOutput`、`LoadImage`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、SaveImage、EmptyLatentImage
