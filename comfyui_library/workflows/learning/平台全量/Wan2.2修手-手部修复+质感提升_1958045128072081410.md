---
key: 平台全量/Wan2.2修手-手部修复+质感提升_1958045128072081410.json
name: Wan2.2修手-手部修复+质感提升_1958045128072081410
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2修手-手部修复+质感提升_1958045128072081410.json
hash: 4ec49a73ba0af944
coverage: 0.869565
learned_at: 2026-11-14 01:06:16
nodes: [ImageScaleBy, CLIPTextEncode, VAEDecode, MaskPreview+, ModelSamplingSD3, SaveImage, SaveImage, InpaintModelConditioning, Image Comparer (rgthree), KSampler, VAEDecode, Image Comparer (rgthree), KSampler, CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), VAELoader, UpscaleModelLoader, ImageUpscaleWithModel, VAEEncode, LoraLoaderModelOnly, LoadImage, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.33000000000000007, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 279589923291184, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2修手-手部修复+质感提升_1958045128072081410.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2修手-手部修复+质感提升_1958045128072081410.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `MaskPreview+`
- `ModelSamplingSD3`
- `SaveImage`
- `SaveImage`
- `InpaintModelConditioning`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `279589923291184`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.33000000000000007`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ImageScaleBy`、`CLIPTextEncode`、`VAEDecode`、`MaskPreview+`、`ModelSamplingSD3`、`SaveImage`、`InpaintModelConditioning`、`KSampler`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEEncode`、`LoraLoaderModelOnly`、`LoadImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
