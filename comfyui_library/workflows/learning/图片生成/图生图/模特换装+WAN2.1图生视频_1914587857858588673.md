---
key: 图片生成/图生图/模特换装+WAN2.1图生视频_1914587857858588673.json
name: 模特换装+WAN2.1图生视频_1914587857858588673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/模特换装+WAN2.1图生视频_1914587857858588673.json
hash: 8f2583faa94fbe77
coverage: 0.878378
learned_at: 2026-10-23 13:10:33
nodes: [Image Blank, MaskToImage, Image Blank, CLIPTextEncode, CLIPTextEncode, ImageCompositeMasked, ImageConcanate, ImageToMask, ImageConcanate, GetImageSize+, GetImageSize+, MathExpression|pysssss, MathExpression|pysssss, VAEDecode, GetImageSize+, InpaintModelConditioning, CLIPVisionEncode, StyleModelApply, FluxGuidance, MaskPreview+, PreviewImage, PreviewImage, KSampler, GroundingDinoModelLoader (segment anything), MaskPreview+, ImageResizeKJ, GroundingDinoModelLoader (segment anything), FeatherMask, ImageResizeKJ, GroundingDinoSAMSegment (segment anything), GetNode, DifferentialDiffusion, WanVideoEnhanceAVideo, WanVideoTeaCache, GroundingDinoSAMSegment (segment anything), SetNode, WanVideoSampler, GetNode, LoadWanVideoClipTextEncoder, WanVideoDecode, DownloadAndLoadGIMMVFIModel, TextInput_, PreviewImage, Image Comparer (rgthree), SaveImage, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, GIMMVFI_interpolate, GrowMask, PreviewImage, ImageCrop, WanVideoVAELoader, WanVideoTextEncode, WanVideoModelLoader, VHS_VideoCombine, WanVideoImageClipEncode, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleBy, VHS_VideoCombine, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, SAMModelLoader (segment anything), SAMModelLoader (segment anything), UNETLoader, VAELoader, DualCLIPLoader, LoraLoader, CLIPVisionLoader, StyleModelLoader, LayerUtility: ImageAutoCrop V2]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "黑色性感的衣服_1.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 866575856684179, "steps": 30, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/模特换装+WAN2.1图生视频_1914587857858588673.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/模特换装+WAN2.1图生视频_1914587857858588673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `Image Blank`
- `MaskToImage`
- `Image Blank`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageToMask`
- `ImageConcanate`
- `GetImageSize+`
- `GetImageSize+`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `GetImageSize+`
- `InpaintModelConditioning`
- `CLIPVisionEncode`
- `StyleModelApply`
- `FluxGuidance`
- `MaskPreview+`
- `PreviewImage`
- `PreviewImage`
- `KSampler` ★核心
- `GroundingDinoModelLoader (segment anything)`
- `MaskPreview+`
- `ImageResizeKJ`
- `GroundingDinoModelLoader (segment anything)`
- `FeatherMask`
- `ImageResizeKJ`
- `GroundingDinoSAMSegment (segment anything)`
- `GetNode`
- `DifferentialDiffusion`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `GroundingDinoSAMSegment (segment anything)`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `DownloadAndLoadGIMMVFIModel`
- `TextInput_`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `GIMMVFI_interpolate`
- `GrowMask`
- `PreviewImage`
- `ImageCrop`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoImageClipEncode`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `SAMModelLoader (segment anything)`
- `SAMModelLoader (segment anything)`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`
- `LayerUtility: ImageAutoCrop V2`

**识别到的模式**：lora

## 关键参数

- `seed` = `866575856684179`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `lora_name` = `黑色性感的衣服_1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **88%**（65/74）

**有卡**：`Image Blank`、`MaskToImage`、`CLIPTextEncode`、`ImageCompositeMasked`、`ImageConcanate`、`ImageToMask`、`GetImageSize+`、`MathExpression|pysssss`、`VAEDecode`、`InpaintModelConditioning`、`CLIPVisionEncode`、`StyleModelApply`、`FluxGuidance`、`MaskPreview+`、`KSampler`、`GroundingDinoModelLoader (segment anything)`、`ImageResizeKJ`、`FeatherMask`、`GroundingDinoSAMSegment (segment anything)`、`DifferentialDiffusion`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSampler`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`DownloadAndLoadGIMMVFIModel`、`TextInput_`、`SaveImage`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`GIMMVFI_interpolate`、`GrowMask`、`ImageCrop`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoImageClipEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleBy`、`LoadImage`、`SAMModelLoader (segment anything)`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`LoraLoader`、`CLIPVisionLoader`、`StyleModelLoader`、`LayerUtility: ImageAutoCrop V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、WanVideoSampler
