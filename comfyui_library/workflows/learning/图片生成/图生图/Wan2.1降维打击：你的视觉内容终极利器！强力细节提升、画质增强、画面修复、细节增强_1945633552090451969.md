---
key: 图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json
name: Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json
hash: ea0811e68586dd0c
coverage: 0.842105
learned_at: 2026-10-23 11:27:53
nodes: [Note, CLIPTextEncode, CLIPTextEncode, ImageUpscaleWithModel, LayerUtility: ImageScaleRestore V2, VAEEncode, VAEDecode, UpscaleModelLoader, VAELoader, UNETLoader, CLIPLoader, Image Comparer (rgthree), SaveImage, RH_Captioner, easy showAnything, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 604799962816683, "steps": 10}
---

# 图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1降维打击：你的视觉内容终极利器！强力细节提升、画质增强、画面修复、细节增强_1945633552090451969.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleRestore V2`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `RH_Captioner`
- `easy showAnything`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `604799962816683`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPTextEncode`、`ImageUpscaleWithModel`、`LayerUtility: ImageScaleRestore V2`、`VAEEncode`、`VAEDecode`、`UpscaleModelLoader`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`RH_Captioner`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
