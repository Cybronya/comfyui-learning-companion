---
key: 图片生成/文生图/Wan2.2 最强写实洗图，已经没有后期修复的必要_1961285660298645506.json
name: Wan2.2 最强写实洗图，已经没有后期修复的必要_1961285660298645506
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 最强写实洗图，已经没有后期修复的必要_1961285660298645506.json
hash: f19bfc3978f8e6cd
coverage: 0.833333
learned_at: 2026-10-15 22:27:35
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, LoraLoader, LoraLoader, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, LoadImage, GetImageSize, KSampler, VAEDecode, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, VAEEncode, VAEDecode, LayerUtility: LoadJoyCaptionBeta1Model, CR Text Concatenate, ShowText|pysssss, Note, SaveImage, SaveImage, PreviewImage, PreviewImage, CR Text, LayerUtility: JoyCaptionBeta1, KSampler, Fast Groups Bypasser (rgthree), Note, LoraLoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.5000000000000001, "height": 512, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 915923548774129, "steps": 20, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001, "width": 512}
---

# 图片生成/文生图/Wan2.2 最强写实洗图，已经没有后期修复的必要_1961285660298645506.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 最强写实洗图，已经没有后期修复的必要_1961285660298645506.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `LoadImage`
- `GetImageSize`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `CR Text Concatenate`
- `ShowText|pysssss`
- `Note`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `CR Text`
- `LayerUtility: JoyCaptionBeta1`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoraLoader` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `915923548774129`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LoadImage`、`GetImageSize`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`VAEEncode`、`LayerUtility: LoadJoyCaptionBeta1Model`、`CR Text Concatenate`、`SaveImage`、`CR Text`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
