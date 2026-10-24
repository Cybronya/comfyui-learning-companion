---
key: 图片生成/图生图/wan2.1超大尺寸局部重绘修复_1949565647637880833.json
name: wan2.1超大尺寸局部重绘修复_1949565647637880833
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.1超大尺寸局部重绘修复_1949565647637880833.json
hash: 2cc925d75df89d88
coverage: 0.777778
learned_at: 2026-10-23 11:45:52
nodes: [LoadImage, LoadImage, ShowText|pysssss, RH_Captioner, CLIPTextEncode, Mask Fill Holes, LayerUtility: RestoreCropBox, LayerUtility: GetImageSize, GetImageSize, easy showAnything, Bjornulf_AnythingToText, easy showAnything, Bjornulf_AnythingToText, GrowMaskWithBlur, LoraLoader, ImageScale, VAEEncode, KSampler, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: CropByMask V2, CR Text Concatenate, CLIPTextEncode, LoadImage, PrimitiveNode, UNETLoader, CLIPLoader, VAELoader, Image Comparer (rgthree), SaveImage, PreviewImage, MarkdownNote, MarkdownNote]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 487563980678608, "steps": 20, "strength_clip": 0.45000000000000007, "strength_model": 0.45000000000000007}
---

# 图片生成/图生图/wan2.1超大尺寸局部重绘修复_1949565647637880833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.1超大尺寸局部重绘修复_1949565647637880833.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `LoadImage`
- `LoadImage`
- `ShowText|pysssss`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `Mask Fill Holes`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: GetImageSize`
- `GetImageSize`
- `easy showAnything`
- `Bjornulf_AnythingToText`
- `easy showAnything`
- `Bjornulf_AnythingToText`
- `GrowMaskWithBlur`
- `LoraLoader` ★核心
- `ImageScale`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: CropByMask V2`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PrimitiveNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.45000000000000007`
- `strength_clip` = `0.45000000000000007`
- `seed` = `487563980678608`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`LoadImage`、`RH_Captioner`、`CLIPTextEncode`、`Mask Fill Holes`、`LayerUtility: RestoreCropBox`、`LayerUtility: GetImageSize`、`GetImageSize`、`Bjornulf_AnythingToText`、`GrowMaskWithBlur`、`LoraLoader`、`ImageScale`、`VAEEncode`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`LayerUtility: CropByMask V2`、`CR Text Concatenate`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
