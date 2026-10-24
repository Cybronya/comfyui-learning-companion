---
key: 图片生成/图生图/Flux Kontext Canva_一致性双图融合plus 局部放大迁移(电商神器)_Borges_1970715585116073985.json
name: Flux Kontext Canva_一致性双图融合plus 局部放大迁移(电商神器)_Borges_1970715585116073985
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Canva_一致性双图融合plus 局部放大迁移(电商神器)_Borges_1970715585116073985.json
hash: 54e7d37a2afbbf92
coverage: 0.864407
learned_at: 2026-10-23 10:56:24
nodes: [DualCLIPLoader, UNETLoader, ConditioningZeroOut, GoogleTranslateTextNode, ShowText|pysssss, LayerMask: PersonMaskUltra, LayerMask: SAM2Ultra, VAELoader, CLIPTextEncode, LayerUtility: CropBoxResolve, ResizeMask, VAEEncode, ReferenceLatent, FluxKontextImageScale, FastCanvasTool, ImageResizeKJ, LayerUtility: ImageAutoCrop V2, PreviewImage, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ColorImage V2, LayerUtility: RestoreCropBox, PreviewImage, FastCanvasTool, Colored Image (mtb), ResizeImageMixlab, PreviewImage, CropByMask_UTK, RepeatLatentBatch, FluxGuidance, VAEDecode, SetNode, preview_mask, PreviewImage, FastCanvas, preview_mask, ImageScale, GetNode, LoraLoaderModelOnly, SaveImage, LayerUtility: RestoreCropBox, SaveImage, ImageScale, Kontext Inpainting Conditioning, KSampler, PreviewImage, JoinImageWithAlpha, ImageBlendV1, GetFilledColorImage, GetImageSize, Light-Tool: ImageToMask, Image Rembg (Remove Background), GrowMaskWithBlur, Text Multiline, Note Plus (mtb), LoadImage, LoadImageFromUrl, LoadImage, FastCanvas]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 408040791779581, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Canva_一致性双图融合plus 局部放大迁移(电商神器)_Borges_1970715585116073985.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Canva_一致性双图融合plus 局部放大迁移(电商神器)_Borges_1970715585116073985.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `GoogleTranslateTextNode`
- `ShowText|pysssss`
- `LayerMask: PersonMaskUltra`
- `LayerMask: SAM2Ultra`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: CropBoxResolve`
- `ResizeMask`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxKontextImageScale`
- `FastCanvasTool`
- `ImageResizeKJ`
- `LayerUtility: ImageAutoCrop V2`
- `PreviewImage`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: RestoreCropBox`
- `PreviewImage`
- `FastCanvasTool`
- `Colored Image (mtb)`
- `ResizeImageMixlab`
- `PreviewImage`
- `CropByMask_UTK`
- `RepeatLatentBatch`
- `FluxGuidance`
- `VAEDecode` ★核心
- `SetNode`
- `preview_mask`
- `PreviewImage`
- `FastCanvas`
- `preview_mask`
- `ImageScale`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LayerUtility: RestoreCropBox`
- `SaveImage`
- `ImageScale`
- `Kontext Inpainting Conditioning`
- `KSampler` ★核心
- `PreviewImage`
- `JoinImageWithAlpha`
- `ImageBlendV1`
- `GetFilledColorImage`
- `GetImageSize`
- `Light-Tool: ImageToMask`
- `Image Rembg (Remove Background)`
- `GrowMaskWithBlur`
- `Text Multiline`
- `Note Plus (mtb)`
- `LoadImage`
- `LoadImageFromUrl`
- `LoadImage`
- `FastCanvas`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `408040791779581`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（51/59）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`ConditioningZeroOut`、`GoogleTranslateTextNode`、`LayerMask: PersonMaskUltra`、`LayerMask: SAM2Ultra`、`VAELoader`、`CLIPTextEncode`、`LayerUtility: CropBoxResolve`、`ResizeMask`、`VAEEncode`、`ReferenceLatent`、`FluxKontextImageScale`、`FastCanvasTool`、`ImageResizeKJ`、`LayerUtility: ImageAutoCrop V2`、`LayerUtility: ColorImage V2`、`LayerUtility: CropByMask V2`、`LayerUtility: RestoreCropBox`、`Colored Image (mtb)`、`ResizeImageMixlab`、`CropByMask_UTK`、`RepeatLatentBatch`、`FluxGuidance`、`VAEDecode`、`preview_mask`、`FastCanvas`、`ImageScale`、`LoraLoaderModelOnly`、`SaveImage`、`Kontext Inpainting Conditioning`、`KSampler`、`JoinImageWithAlpha`、`ImageBlendV1`、`GetFilledColorImage`、`GetImageSize`、`Light-Tool: ImageToMask`、`Image Rembg (Remove Background)`、`GrowMaskWithBlur`、`Text Multiline`、`Note Plus (mtb)`、`LoadImage`、`LoadImageFromUrl`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
