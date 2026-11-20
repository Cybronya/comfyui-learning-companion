---
key: 平台全量/firered-image-edit-1.1-flux2-klein-模特与产品互动_2050753855205453826.json
name: firered-image-edit-1.1-flux2-klein-模特与产品互动_2050753855205453826
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/firered-image-edit-1.1-flux2-klein-模特与产品互动_2050753855205453826.json
hash: 79552972f27b26c4
coverage: 0.844444
learned_at: 2026-11-14 01:10:25
nodes: [ModelSamplingAuraFlow, CFGNorm, CLIPLoader, VAELoader, BasicScheduler, LoraLoaderModelOnly, CheckpointLoaderSimple, UNETLoader, easy ifElse, CLIPLoader, VAELoader, UNETLoader, VAEDecode, PrimitiveNode, easy int, Seed (rgthree), easy ifElse, easy int, KSamplerSelect, DetailDaemonSamplerNode, SamplerCustom, VAEDecode, ImageColorMatch+, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LayerMask: MaskGrow, LayerUtility: ColorImage V2, ImageScaleToTotalPixelsX, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, PreviewImage, KSampler, PainterFluxImageEdit, Seed (rgthree), easy positive, ImageScaleToTotalPixelsX, LayerUtility: ImageMaskScaleAs, LoadImage, ImageColorMatch+, Image Comparer (rgthree), SaveImage, LayerUtility: ImageMaskScaleAs, PreviewImage, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v20.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 817210369762569, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/firered-image-edit-1.1-flux2-klein-模特与产品互动_2050753855205453826.json

> 来源文件 `comfyui_library/workflows/平台全量/firered-image-edit-1.1-flux2-klein-模特与产品互动_2050753855205453826.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `VAELoader`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `easy ifElse`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PrimitiveNode`
- `easy int`
- `Seed (rgthree)`
- `easy ifElse`
- `easy int`
- `KSamplerSelect` ★核心
- `DetailDaemonSamplerNode` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `ImageColorMatch+`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `ImageScaleToTotalPixelsX`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `PainterFluxImageEdit`
- `Seed (rgthree)`
- `easy positive`
- `ImageScaleToTotalPixelsX`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `ImageColorMatch+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: ImageMaskScaleAs`
- `PreviewImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v20.safetensors`
- `seed` = `817210369762569`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`VAELoader`、`BasicScheduler`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`UNETLoader`、`VAEDecode`、`easy int`、`Seed (rgthree)`、`KSamplerSelect`、`DetailDaemonSamplerNode`、`SamplerCustom`、`ImageColorMatch+`、`TextEncodeQwenImageEditPlus`、`LayerMask: MaskGrow`、`LayerUtility: ColorImage V2`、`ImageScaleToTotalPixelsX`、`LayerUtility: ImageBlend`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`KSampler`、`PainterFluxImageEdit`、`easy positive`、`LayerUtility: ImageMaskScaleAs`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
