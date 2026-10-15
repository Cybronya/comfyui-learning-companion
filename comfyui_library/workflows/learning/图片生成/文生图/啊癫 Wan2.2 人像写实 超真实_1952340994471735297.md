---
key: 图片生成/文生图/啊癫 Wan2.2 人像写实 超真实_1952340994471735297.json
name: 啊癫 Wan2.2 人像写实 超真实_1952340994471735297
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/啊癫 Wan2.2 人像写实 超真实_1952340994471735297.json
hash: b7c4bc01cf261a59
coverage: 0.96
learned_at: 2026-10-15 22:28:23
nodes: [CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, LoraLoader, VAELoader, UNETLoader, CLIPLoader, PathchSageAttentionKJ, VAEEncode, ModelSamplingSD3, CR Text Concatenate, LoraLoader, SaveImage, SaveLatent, CR Text, CFGZeroStarAndInit, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, VAEDecode, RH_Captioner, SaveImage, LoadImage, easy showAnything, KSampler]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1083726181617890, "steps": 20, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
---

# 图片生成/文生图/啊癫 Wan2.2 人像写实 超真实_1952340994471735297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/啊癫 Wan2.2 人像写实 超真实_1952340994471735297.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `CR Text Concatenate`
- `LoraLoader` ★核心
- `SaveImage`
- `SaveLatent`
- `CR Text`
- `CFGZeroStarAndInit`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `RH_Captioner`
- `SaveImage`
- `LoadImage`
- `easy showAnything`
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `1083726181617890`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoader`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAEEncode`、`ModelSamplingSD3`、`CR Text Concatenate`、`SaveImage`、`SaveLatent`、`CR Text`、`CFGZeroStarAndInit`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`RH_Captioner`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit
