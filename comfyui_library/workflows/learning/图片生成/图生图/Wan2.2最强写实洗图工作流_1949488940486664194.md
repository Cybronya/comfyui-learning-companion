---
key: 图片生成/图生图/Wan2.2最强写实洗图工作流_1949488940486664194.json
name: Wan2.2最强写实洗图工作流_1949488940486664194
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2最强写实洗图工作流_1949488940486664194.json
hash: e93bd240e75944f9
coverage: 0.958333
learned_at: 2026-10-23 11:28:22
nodes: [LayerUtility: ImageReel, CLIPTextEncode, CLIPTextEncode, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, LoraLoader, VAELoader, LoadImage, LayerUtility: ImageReelComposit, RH_Captioner, UNETLoader, KSampler, CLIPLoader, PathchSageAttentionKJ, VAEDecode, VAEEncode, ModelSamplingSD3, CR Text Concatenate, CFGZeroStarAndInit, SaveImage, SaveImage, CR Text, LoraLoader]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 19881444223505, "steps": 20, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
---

# 图片生成/图生图/Wan2.2最强写实洗图工作流_1949488940486664194.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2最强写实洗图工作流_1949488940486664194.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAELoader`
- `LoadImage`
- `LayerUtility: ImageReelComposit`
- `RH_Captioner`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `CR Text Concatenate`
- `CFGZeroStarAndInit`
- `SaveImage`
- `SaveImage`
- `CR Text`
- `LoraLoader` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `19881444223505`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`LayerUtility: ImageReel`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoader`、`VAELoader`、`LoadImage`、`LayerUtility: ImageReelComposit`、`RH_Captioner`、`UNETLoader`、`KSampler`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`VAEEncode`、`ModelSamplingSD3`、`CR Text Concatenate`、`CFGZeroStarAndInit`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit
