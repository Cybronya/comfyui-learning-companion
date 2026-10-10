---
key: Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json
name: Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json
hash: e970033f2df2c49c
coverage: 0.763158
learned_at: 2026-10-10 20:58:35
nodes: [FluxGuidance, CLIPTextEncode, CLIPTextEncode, UNETLoader, RH_Captioner, Text Multiline, VAELoader, DualCLIPLoader, VAELoader, Text Concatenate, easy showAnything, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, UNETLoader, KSampler, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, PreviewImage, Image Comparer (rgthree), LayerUtility: PurgeVRAM V2, VAEDecode, SaveImage, PreviewImage, ImageSharpen, EsesImageEffectBloom, BetterFilmGrain, ModelSamplingSD3, LoadImage, ImageScaleDownToSize, CR SDXL Aspect Ratio, GetImageSizeAndCount, CR Simple Image Compare, SaveImage]
patterns: [image_to_image]
missing: [CR Simple Image Compare, LayerUtility: PurgeVRAM V2, Text Concatenate, Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 18799775116191, "steps": 10}
discoveries: [次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# Flux+wan2.1更真实修复和洗图_细节增强_1945516410565218305.json

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

覆盖率 **76%**（29/38）

**有卡**：`FluxGuidance`、`CLIPTextEncode`、`UNETLoader`、`RH_Captioner`、`VAELoader`、`DualCLIPLoader`、`CLIPLoader`、`VAEEncode`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`ImageSharpen`、`EsesImageEffectBloom`、`BetterFilmGrain`、`ModelSamplingSD3`、`LoadImage`、`ImageScaleDownToSize`、`GetImageSizeAndCount`

**缺卡**（5）：`CR Simple Image Compare`、`LayerUtility: PurgeVRAM V2`、`Text Concatenate`、`Text Multiline`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 学习发现

- 次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
