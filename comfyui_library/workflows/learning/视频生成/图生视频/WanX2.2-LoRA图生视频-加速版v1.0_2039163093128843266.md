---
key: 视频生成/图生视频/WanX2.2-LoRA图生视频-加速版v1.0_2039163093128843266.json
name: WanX2.2-LoRA图生视频-加速版v1.0_2039163093128843266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039163093128843266.json
hash: 47da8a83c26d3ae9
coverage: 0.521739
learned_at: 2026-10-15 22:36:06
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, VAELoader, VAEDecode, ModelSamplingSD3, CLIPLoader, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, WanImageToVideo, GetImageSizeAndCount, PathchSageAttentionKJ, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, easy int, LoadImage, TextInput_, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/WanX2.2-LoRA图生视频-加速版v1.0_2039163093128843266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039163093128843266.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `VAELoader`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `GetImageSizeAndCount`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `easy int`
- `LoadImage`
- `TextInput_`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **52%**（24/46）

**有卡**：`ModelSamplingSD3`、`VAELoader`、`VAEDecode`、`CLIPLoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`WanImageToVideo`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`easy int`、`LoadImage`、`TextInput_`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
