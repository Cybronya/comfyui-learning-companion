---
key: 图片生成/图生图/啊癫 wan2.2人像写实洗图_1954212582670397441.json
name: 啊癫 wan2.2人像写实洗图_1954212582670397441
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/啊癫 wan2.2人像写实洗图_1954212582670397441.json
hash: da7129e5439a2a4e
coverage: 0.958333
learned_at: 2026-10-23 12:37:08
nodes: [LayerUtility: ImageReel, CLIPTextEncode, CLIPTextEncode, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, LoraLoader, VAELoader, LayerUtility: ImageReelComposit, RH_Captioner, UNETLoader, CLIPLoader, PathchSageAttentionKJ, VAEDecode, VAEEncode, ModelSamplingSD3, CR Text Concatenate, CFGZeroStarAndInit, SaveImage, SaveImage, CR Text, LoraLoader, LoadImage, KSampler]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.26000000000000006, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 996826294681352, "steps": 20, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
---

# 图片生成/图生图/啊癫 wan2.2人像写实洗图_1954212582670397441.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/啊癫 wan2.2人像写实洗图_1954212582670397441.json`

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
- `LayerUtility: ImageReelComposit`
- `RH_Captioner`
- `UNETLoader` ★核心
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
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `996826294681352`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.26000000000000006`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`LayerUtility: ImageReel`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoader`、`VAELoader`、`LayerUtility: ImageReelComposit`、`RH_Captioner`、`UNETLoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`VAEEncode`、`ModelSamplingSD3`、`CR Text Concatenate`、`CFGZeroStarAndInit`、`SaveImage`、`CR Text`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit
