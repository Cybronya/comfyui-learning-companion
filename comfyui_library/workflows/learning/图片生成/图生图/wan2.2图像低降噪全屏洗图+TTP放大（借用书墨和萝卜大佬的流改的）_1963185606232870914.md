---
key: 图片生成/图生图/wan2.2图像低降噪全屏洗图+TTP放大（借用书墨和萝卜大佬的流改的）_1963185606232870914.json
name: wan2.2图像低降噪全屏洗图+TTP放大（借用书墨和萝卜大佬的流改的）_1963185606232870914
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2图像低降噪全屏洗图+TTP放大（借用书墨和萝卜大佬的流改的）_1963185606232870914.json
hash: 345547a278447097
coverage: 0.823529
learned_at: 2026-10-23 11:46:04
nodes: [CLIPTextEncode, MathExpression|pysssss, LayerUtility: PurgeVRAM, easy sleep, VAEEncode, ShowText|pysssss, CR Text Concatenate, easy loadImagesForLoop, easy forLoopStart, easy forLoopEnd, PrimitiveStringMultiline, Note, LayerUtility: SaveImagePlus, ShowText|pysssss, PreviewImage, LayerMask: LoadFlorence2Model, VAELoader, CLIPLoader, DualCLIPLoader, UNETLoader, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, SaveImage, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleBy, SaveImage, ImageScaleToTotalPixels, KSampler, VAEDecode, PreviewImage, DifferentialDiffusion, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, KSampler, LoadImage, CR Simple Image Compare, CLIPTextEncode, LayerUtility: Florence2Image2Prompt, Note, Note, ShowText|pysssss]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 157914450627527, "steps": 7}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan2.2图像低降噪全屏洗图+TTP放大（借用书墨和萝卜大佬的流改的）_1963185606232870914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2图像低降噪全屏洗图+TTP放大（借用书墨和萝卜大佬的流改的）_1963185606232870914.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `LayerUtility: PurgeVRAM`
- `easy sleep`
- `VAEEncode` ★核心
- `ShowText|pysssss`
- `CR Text Concatenate`
- `easy loadImagesForLoop`
- `easy forLoopStart`
- `easy forLoopEnd`
- `PrimitiveStringMultiline`
- `Note`
- `LayerUtility: SaveImagePlus`
- `ShowText|pysssss`
- `PreviewImage`
- `LayerMask: LoadFlorence2Model`
- `VAELoader`
- `CLIPLoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactImageBatchToImageList`
- `VAEEncode` ★核心
- `SaveImage`
- `TTP_Image_Assy`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `DifferentialDiffusion`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoadImage`
- `CR Simple Image Compare`
- `CLIPTextEncode` ★核心
- `LayerUtility: Florence2Image2Prompt`
- `Note`
- `Note`
- `ShowText|pysssss`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `157914450627527`
- `steps` = `7`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **82%**（42/51）

**有卡**：`CLIPTextEncode`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM`、`easy sleep`、`VAEEncode`、`CR Text Concatenate`、`easy loadImagesForLoop`、`easy forLoopStart`、`easy forLoopEnd`、`LayerUtility: SaveImagePlus`、`LayerMask: LoadFlorence2Model`、`VAELoader`、`CLIPLoader`、`DualCLIPLoader`、`UNETLoader`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImpactImageBatchToImageList`、`SaveImage`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleBy`、`ImageScaleToTotalPixels`、`KSampler`、`VAEDecode`、`DifferentialDiffusion`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`LoadImage`、`CR Simple Image Compare`、`LayerUtility: Florence2Image2Prompt`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
