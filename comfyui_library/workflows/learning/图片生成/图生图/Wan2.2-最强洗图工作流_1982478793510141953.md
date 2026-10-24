---
key: 图片生成/图生图/Wan2.2-最强洗图工作流_1982478793510141953.json
name: Wan2.2-最强洗图工作流_1982478793510141953
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2-最强洗图工作流_1982478793510141953.json
hash: 4d7c36cebb07b867
coverage: 0.909091
learned_at: 2026-10-23 11:28:08
nodes: [CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, LoraLoader, LoraLoader, CR Text, RH_Captioner, easy showAnything, CR Text Concatenate, UNETLoader, VAELoader, CLIPLoader, LoadImage, SaveImage, MarkdownNote, LoadImage, CLIPTextEncode, PathchSageAttentionKJ, ModelSamplingSD3, VAEEncode, VAEDecode, KSampler]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 868244490304787, "steps": 20, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
---

# 图片生成/图生图/Wan2.2-最强洗图工作流_1982478793510141953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2-最强洗图工作流_1982478793510141953.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CR Text`
- `RH_Captioner`
- `easy showAnything`
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `868244490304787`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoader`、`CR Text`、`RH_Captioner`、`CR Text Concatenate`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoadImage`、`SaveImage`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`VAEDecode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
