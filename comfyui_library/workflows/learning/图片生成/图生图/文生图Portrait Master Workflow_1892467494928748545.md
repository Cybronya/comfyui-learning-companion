---
key: 图片生成/图生图/文生图Portrait Master Workflow_1892467494928748545.json
name: 文生图Portrait Master Workflow_1892467494928748545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/文生图Portrait Master Workflow_1892467494928748545.json
hash: 63fac8acf274bbd8
coverage: 0.621359
learned_at: 2026-10-23 13:03:43
nodes: [Reroute, UpscaleModelLoader, ImageReceiver, ImageReceiver, SetNode, SetNode, ImageScale, GetNode, GetNode, SetNode, CR Integer To String, CR Integer To String, ShowText|pysssss, ImageSender, Reroute, Reroute, GetNode, VAEEncode, SetNode, SetNode, VAEDecode, RepeatLatentBatch, PreviewImage, PreviewImage, ControlNetApplyAdvanced, DeepTranslatorTextNode, ControlNetLoaderAdvanced, SetLatentNoiseMask, CR Seed, Reroute, ImageReceiver, ImageSender, KSampler (Efficient), PrimitiveNode, ImageSender, UltimateSDUpscale, GetNode, MaskToImage, VAEEncode, SetLatentNoiseMask, InpaintPreprocessor, Preview Chooser, DeepTranslatorTextNode, ImageReceiver, KSamplerAdvanced, ControlNetLoaderAdvanced, DeepTranslatorTextNode, GetNode, DeepTranslatorTextNode, GetNode, SetNode, Reroute, Anything Everywhere, SetNode, Reroute, ControlNetLoaderAdvanced, VAEEncodeForInpaint, SetNode, ImpactImageInfo, ShowText|pysssss, Reroute, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ControlNetApplyAdvanced, MiDaS-DepthMapPreprocessor, ControlNetApplyAdvanced, Image Canny Filter, VAEDecode, ImageSender, PreviewImage, PreviewImage, PreviewImage, Reroute, CLIPTextEncode, CLIPTextEncode, Reroute, PreviewImage, KSampler (Efficient), RepeatLatentBatch, RembgNode_Mix, Image Rembg (Remove Background), ImageToMask, InvertMask, MaskToImage, ImageScaleBy, Simple String, SAMModelLoader (segment anything), ImagePadForOutpaint, Note, Note, Note, Fast Groups Muter (rgthree), Note, Preview Chooser, LoadImage, Efficient Loader, ControlNetLoaderAdvanced, GetNode, LatentCompositeMasked, EmptyLatentImage, LoadImage, ImageSender, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 6, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 512, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 121783154799825, "steps": 20, "width": 512}
---

# 图片生成/图生图/文生图Portrait Master Workflow_1892467494928748545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/文生图Portrait Master Workflow_1892467494928748545.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
- `Reroute`
- `UpscaleModelLoader`
- `ImageReceiver`
- `ImageReceiver`
- `SetNode`
- `SetNode`
- `ImageScale`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Integer To String`
- `CR Integer To String`
- `ShowText|pysssss`
- `ImageSender`
- `Reroute`
- `Reroute`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `RepeatLatentBatch`
- `PreviewImage`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `DeepTranslatorTextNode`
- `ControlNetLoaderAdvanced`
- `SetLatentNoiseMask`
- `CR Seed`
- `Reroute`
- `ImageReceiver`
- `ImageSender`
- `KSampler (Efficient)` ★核心
- `PrimitiveNode`
- `ImageSender`
- `UltimateSDUpscale`
- `GetNode`
- `MaskToImage`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `InpaintPreprocessor`
- `Preview Chooser`
- `DeepTranslatorTextNode`
- `ImageReceiver`
- `KSamplerAdvanced` ★核心
- `ControlNetLoaderAdvanced`
- `DeepTranslatorTextNode`
- `GetNode`
- `DeepTranslatorTextNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `Anything Everywhere`
- `SetNode`
- `Reroute`
- `ControlNetLoaderAdvanced`
- `VAEEncodeForInpaint` ★核心
- `SetNode`
- `ImpactImageInfo`
- `ShowText|pysssss`
- `Reroute`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ControlNetApplyAdvanced` ★核心
- `MiDaS-DepthMapPreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `Image Canny Filter`
- `VAEDecode` ★核心
- `ImageSender`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `PreviewImage`
- `KSampler (Efficient)` ★核心
- `RepeatLatentBatch`
- `RembgNode_Mix`
- `Image Rembg (Remove Background)`
- `ImageToMask`
- `InvertMask`
- `MaskToImage`
- `ImageScaleBy`
- `Simple String`
- `SAMModelLoader (segment anything)`
- `ImagePadForOutpaint`
- `Note`
- `Note`
- `Note`
- `Fast Groups Muter (rgthree)`
- `Note`
- `Preview Chooser`
- `LoadImage`
- `Efficient Loader`
- `ControlNetLoaderAdvanced`
- `GetNode`
- `LatentCompositeMasked`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ImageSender`
- `SaveImage`

## 关键参数

- `controlnet_strength` = `0.7000000000000001`
- `seed` = `121783154799825`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（64/103）

**有卡**：`UpscaleModelLoader`、`ImageReceiver`、`ImageScale`、`CR Integer To String`、`ImageSender`、`VAEEncode`、`VAEDecode`、`RepeatLatentBatch`、`ControlNetApplyAdvanced`、`DeepTranslatorTextNode`、`ControlNetLoaderAdvanced`、`SetLatentNoiseMask`、`CR Seed`、`KSampler (Efficient)`、`UltimateSDUpscale`、`MaskToImage`、`InpaintPreprocessor`、`Preview Chooser`、`KSamplerAdvanced`、`VAEEncodeForInpaint`、`ImpactImageInfo`、`GroundingDinoModelLoader (segment anything)`、`GroundingDinoSAMSegment (segment anything)`、`MiDaS-DepthMapPreprocessor`、`Image Canny Filter`、`CLIPTextEncode`、`RembgNode_Mix`、`Image Rembg (Remove Background)`、`ImageToMask`、`InvertMask`、`ImageScaleBy`、`Simple String`、`SAMModelLoader (segment anything)`、`ImagePadForOutpaint`、`LoadImage`、`Efficient Loader`、`LatentCompositeMasked`、`EmptyLatentImage`、`SaveImage`

**用到的条目**：VAEDecode、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoaderAdvanced、MiDaS-DepthMapPreprocessor、Image Canny Filter
