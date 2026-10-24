---
key: 图片生成/图生图/Wan2.2（写实修复）_1962173423302676481.json
name: Wan2.2（写实修复）_1962173423302676481
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2（写实修复）_1962173423302676481.json
hash: 99a2360b27d7b3df
coverage: 0.952381
learned_at: 2026-10-23 11:28:26
nodes: [CR Text Concatenate, CR Text, UNETLoader, LoraLoader, LoraLoader, LoraLoader, VAELoader, CLIPLoader, CLIPTextEncode, VAEEncode, CLIPTextEncode, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, SaveImage, KSampler, Image Comparer (rgthree), RH_Captioner, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: CropByMask V2]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1111614118262365, "steps": 12, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
---

# 图片生成/图生图/Wan2.2（写实修复）_1962173423302676481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2（写实修复）_1962173423302676481.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CR Text Concatenate`
- `CR Text`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `RH_Captioner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: CropByMask V2`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `1111614118262365`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`CR Text Concatenate`、`CR Text`、`UNETLoader`、`LoraLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`VAEEncode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`SaveImage`、`KSampler`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LayerUtility: CropByMask V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
