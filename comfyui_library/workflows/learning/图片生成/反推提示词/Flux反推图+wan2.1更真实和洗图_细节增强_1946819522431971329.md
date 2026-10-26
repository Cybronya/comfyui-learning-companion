---
key: 图片生成/反推提示词/Flux反推图+wan2.1更真实和洗图_细节增强_1946819522431971329.json
name: Flux反推图+wan2.1更真实和洗图_细节增强_1946819522431971329
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Flux反推图+wan2.1更真实和洗图_细节增强_1946819522431971329.json
hash: 3d32e7138e4b2062
coverage: 0.875
learned_at: 2026-10-26 01:45:08
nodes: [FluxGuidance, CLIPTextEncode, CLIPTextEncode, UNETLoader, RH_Captioner, VAELoader, DualCLIPLoader, VAELoader, Text Concatenate, easy showAnything, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, UNETLoader, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, ImageSharpen, CR SDXL Aspect Ratio, GetImageSizeAndCount, LayerUtility: PurgeVRAM V2, ModelSamplingSD3, PreviewImage, PreviewImage, Text Multiline, Note, ImageScaleDownToSize, LoadImage, Image Comparer (rgthree), SaveImage, CR Simple Image Compare, LayerFilter: FilmV2, KSampler, VAEDecode, EsesImageEffectBloom, SaveImage, BetterFilmGrain]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 952845283631914, "steps": 10}
---

# 图片生成/反推提示词/Flux反推图+wan2.1更真实和洗图_细节增强_1946819522431971329.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Flux反推图+wan2.1更真实和洗图_细节增强_1946819522431971329.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `RH_Captioner`
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ImageSharpen`
- `CR SDXL Aspect Ratio`
- `GetImageSizeAndCount`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingSD3`
- `PreviewImage`
- `PreviewImage`
- `Text Multiline`
- `Note`
- `ImageScaleDownToSize`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CR Simple Image Compare`
- `LayerFilter: FilmV2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EsesImageEffectBloom`
- `SaveImage`
- `BetterFilmGrain`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `952845283631914`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`FluxGuidance`、`CLIPTextEncode`、`UNETLoader`、`RH_Captioner`、`VAELoader`、`DualCLIPLoader`、`Text Concatenate`、`CLIPLoader`、`VAEEncode`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageSharpen`、`CR SDXL Aspect Ratio`、`GetImageSizeAndCount`、`LayerUtility: PurgeVRAM V2`、`ModelSamplingSD3`、`Text Multiline`、`ImageScaleDownToSize`、`LoadImage`、`SaveImage`、`CR Simple Image Compare`、`LayerFilter: FilmV2`、`EsesImageEffectBloom`、`BetterFilmGrain`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
