---
key: 图片生成/图生图/【洗图反推】Wan2.2 洗图 超级修复 Wan2.2人像全图修复_1982282591334211586.json
name: 【洗图反推】Wan2.2 洗图 超级修复 Wan2.2人像全图修复_1982282591334211586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【洗图反推】Wan2.2 洗图 超级修复 Wan2.2人像全图修复_1982282591334211586.json
hash: 838276f01aef3385
coverage: 0.851852
learned_at: 2026-10-23 11:50:49
nodes: [VAELoader, CLIPTextEncode, CR Text, CR Text Concatenate, CLIPTextEncode, LoraLoader, DeepTranslatorTextNode, KSamplerSelect, UNETLoader, CLIPLoader, SaveImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, ModelSamplingSD3, easy showAnything, VAEEncode, BasicScheduler, RH_Captioner, VAEDecode, SamplerCustom, Note, LoraLoader, CFGZeroStarAndInit, easy showAnything, PathchSageAttentionKJ, LoadImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors", "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
---

# 图片生成/图生图/【洗图反推】Wan2.2 洗图 超级修复 Wan2.2人像全图修复_1982282591334211586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【洗图反推】Wan2.2 洗图 超级修复 Wan2.2人像全图修复_1982282591334211586.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `DeepTranslatorTextNode`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader` ★核心
- `ModelSamplingSD3`
- `easy showAnything`
- `VAEEncode` ★核心
- `BasicScheduler`
- `RH_Captioner`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `Note`
- `LoraLoader` ★核心
- `CFGZeroStarAndInit`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v2_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`VAELoader`、`CLIPTextEncode`、`CR Text`、`CR Text Concatenate`、`LoraLoader`、`DeepTranslatorTextNode`、`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`VAEEncode`、`BasicScheduler`、`RH_Captioner`、`VAEDecode`、`SamplerCustom`、`CFGZeroStarAndInit`、`PathchSageAttentionKJ`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
