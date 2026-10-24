---
key: 图片生成/图生图/wan2.2 洗图工作流_1976841960134791170.json
name: wan2.2 洗图工作流_1976841960134791170
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2 洗图工作流_1976841960134791170.json
hash: 04874810ac69c9cd
coverage: 0.833333
learned_at: 2026-10-23 11:45:55
nodes: [CFGZeroStarAndInit, VAELoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, CLIPLoader, LoraLoader, StringFunction|pysssss, Florence2ModelLoader, Florence2Run, PathchSageAttentionKJ, LoraLoader, LoraLoader, SaveImage, LoadImage, ImageScaleBy, VAEEncode, VAEDecode, Note, Note, Note, Image Comparer (rgthree), ModelSamplingSD3, KSampler]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.12000000000000002, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 573471209358564, "steps": 20, "strength_clip": 0.5000000000000001, "strength_model": 0.5000000000000001}
---

# 图片生成/图生图/wan2.2 洗图工作流_1976841960134791170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2 洗图工作流_1976841960134791170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CFGZeroStarAndInit`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `StringFunction|pysssss`
- `Florence2ModelLoader`
- `Florence2Run`
- `PathchSageAttentionKJ`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `SaveImage`
- `LoadImage`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Note`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `ModelSamplingSD3`
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `0.5000000000000001`
- `strength_clip` = `0.5000000000000001`
- `seed` = `573471209358564`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.12000000000000002`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CFGZeroStarAndInit`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`LoraLoader`、`StringFunction|pysssss`、`Florence2ModelLoader`、`Florence2Run`、`PathchSageAttentionKJ`、`SaveImage`、`LoadImage`、`ImageScaleBy`、`VAEEncode`、`VAEDecode`、`ModelSamplingSD3`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit
