---
key: 图片生成/图生图/高级洗图去ai感超清质感wan2.2_1973025620135383042.json
name: 高级洗图去ai感超清质感wan2.2_1973025620135383042
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高级洗图去ai感超清质感wan2.2_1973025620135383042.json
hash: defa5b708f0c297f
coverage: 0.846154
learned_at: 2026-10-23 13:35:30
nodes: [CLIPTextEncode, VAEEncode, Reroute, PDImageResizeV2, VAEDecode, EmptyHunyuanLatentVideo, UNETLoader, ModelSamplingSD3, KSampler, VAELoader, LoraLoader, SaveImage, LayerUtility: SaveImagePlusV2, LoraLoader, LoraLoader, CLIPLoader, easy showAnything, CLIPTextEncode, CR Text, ttN concat, ImpactSwitch, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, PreviewImage, RH_Captioner, LoadImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.30000000000000004, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1234567916, "steps": 20, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
---

# 图片生成/图生图/高级洗图去ai感超清质感wan2.2_1973025620135383042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高级洗图去ai感超清质感wan2.2_1973025620135383042.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Reroute`
- `PDImageResizeV2`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAELoader`
- `LoraLoader` ★核心
- `SaveImage`
- `LayerUtility: SaveImagePlusV2`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CR Text`
- `ttN concat`
- `ImpactSwitch`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `RH_Captioner`
- `LoadImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `1234567916`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`PDImageResizeV2`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`ModelSamplingSD3`、`KSampler`、`VAELoader`、`LoraLoader`、`SaveImage`、`LayerUtility: SaveImagePlusV2`、`CLIPLoader`、`CR Text`、`ttN concat`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`RH_Captioner`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
