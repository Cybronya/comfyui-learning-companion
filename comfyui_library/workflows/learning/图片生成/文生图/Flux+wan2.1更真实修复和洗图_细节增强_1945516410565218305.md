---
key: 图片生成/文生图/Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json
name: Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json
hash: e970033f2df2c49c
coverage: 0.894737
learned_at: 2026-10-15 22:26:24
nodes: [FluxGuidance, CLIPTextEncode, CLIPTextEncode, UNETLoader, RH_Captioner, Text Multiline, VAELoader, DualCLIPLoader, VAELoader, Text Concatenate, easy showAnything, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, UNETLoader, KSampler, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, PreviewImage, Image Comparer (rgthree), LayerUtility: PurgeVRAM V2, VAEDecode, SaveImage, PreviewImage, ImageSharpen, EsesImageEffectBloom, BetterFilmGrain, ModelSamplingSD3, LoadImage, ImageScaleDownToSize, CR SDXL Aspect Ratio, GetImageSizeAndCount, CR Simple Image Compare, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 18799775116191, "steps": 10}
---

# 图片生成/文生图/Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `RH_Captioner`
- `Text Multiline`
- `VAELoader`
- `DualCLIPLoader`
- `VAELoader`
- `Text Concatenate`
- `easy showAnything`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `ImageSharpen`
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `ModelSamplingSD3`
- `LoadImage`
- `ImageScaleDownToSize`
- `CR SDXL Aspect Ratio`
- `GetImageSizeAndCount`
- `CR Simple Image Compare`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `18799775116191`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`FluxGuidance`、`CLIPTextEncode`、`UNETLoader`、`RH_Captioner`、`Text Multiline`、`VAELoader`、`DualCLIPLoader`、`Text Concatenate`、`CLIPLoader`、`VAEEncode`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`ImageSharpen`、`EsesImageEffectBloom`、`BetterFilmGrain`、`ModelSamplingSD3`、`LoadImage`、`ImageScaleDownToSize`、`CR SDXL Aspect Ratio`、`GetImageSizeAndCount`、`CR Simple Image Compare`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
