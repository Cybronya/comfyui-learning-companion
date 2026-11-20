---
key: 平台全量/Wan2.2写实洗图工作流自用_1963849654646689793.json
name: Wan2.2写实洗图工作流自用_1963849654646689793
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2写实洗图工作流自用_1963849654646689793.json
hash: d3cc6b41a497cf08
coverage: 0.83871
learned_at: 2026-11-14 01:06:18
nodes: [VAELoader, UNETLoader, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, LoraLoader, LayerUtility: ImageReel, CLIPTextEncode, PathchSageAttentionKJ, CFGZeroStarAndInit, ModelSamplingSD3, CR Text, LoraLoader, CLIPLoader, SaveImage, PreviewImage, LoadImage, CR Text Concatenate, LayerUtility: ImageReelComposit, SaveImage, easy showAnything, RH_Captioner, CLIPTextEncode, Note, KSampler, Note, JWFloat, TT_img_enc, SaveImage, VAEDecode, Note]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 526033090279833, "steps": 6, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2写实洗图工作流自用_1963849654646689793.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2写实洗图工作流自用_1963849654646689793.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `CR Text`
- `LoraLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `CR Text Concatenate`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `easy showAnything`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `Note`
- `KSampler` ★核心
- `Note`
- `JWFloat`
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `Note`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `526033090279833`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`VAELoader`、`UNETLoader`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoader`、`LayerUtility: ImageReel`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`CFGZeroStarAndInit`、`ModelSamplingSD3`、`CR Text`、`CLIPLoader`、`SaveImage`、`LoadImage`、`CR Text Concatenate`、`LayerUtility: ImageReelComposit`、`RH_Captioner`、`KSampler`、`JWFloat`、`TT_img_enc`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
