---
key: 平台全量/LTX2.3局部重绘 去字幕去水印换人_2037721536735481857.json
name: LTX2.3局部重绘 去字幕去水印换人_2037721536735481857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3局部重绘 去字幕去水印换人_2037721536735481857.json
hash: 84ebc6547c98f8cd
coverage: 0.96875
learned_at: 2026-11-14 00:38:40
nodes: [LTXVAudioVAEDecode, GetImageSize+, ImageInvert, SamplerCustomAdvanced, EmptyImage, MaskToImage, LTXVConditioning, KSamplerSelect, LTXVSeparateAVLatent, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, LTXVCropGuides, VAEDecodeTiled, LTXVAudioVAEDecode, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConcatAVLatent, SamplerCustomAdvanced, SAM3VideoOutput, MaskExpandBatch+, ImageScaleBy, LTXVPreprocess, RandomNoise, KSamplerSelect, GrowMaskWithBlur, BlockifyMask, VHS_VideoInfoLoaded, Reroute, LTXVAddGuideMulti, VHS_VideoCombine, VHS_VideoCombine, VAEEncode, ImageCompositeFromMaskBatch+, SAM3VideoSegmentation, SAM3VideoSegmentation, CLIPTextEncode, Reroute, LTXVAudioVAEEncode, SolidMask, GetImageSize, ComfyMathExpression, LTXVEmptyLatentAudio, LTXVConcatAVLatent, VHS_VideoCombine, CLIPTextEncode, VHS_LoadVideo, SAM3Propagate, SAM3VideoModelLoader, ResizeImageMaskNode, SAM3PointCollector, VHS_VideoCombine, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, UNETLoader, LoraLoaderModelOnly, SetLatentNoiseMask, LTXVAddGuideMulti, CFGGuider, ManualSigmas, VAEDecodeTiled]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3局部重绘 去字幕去水印换人_2037721536735481857.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3局部重绘 去字幕去水印换人_2037721536735481857.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（64 个）：
- `LTXVAudioVAEDecode` ★核心
- `GetImageSize+`
- `ImageInvert`
- `SamplerCustomAdvanced` ★核心
- `EmptyImage`
- `MaskToImage`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SAM3VideoOutput`
- `MaskExpandBatch+`
- `ImageScaleBy`
- `LTXVPreprocess`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `GrowMaskWithBlur`
- `BlockifyMask`
- `VHS_VideoInfoLoaded`
- `Reroute`
- `LTXVAddGuideMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEEncode` ★核心
- `ImageCompositeFromMaskBatch+`
- `SAM3VideoSegmentation`
- `SAM3VideoSegmentation`
- `CLIPTextEncode` ★核心
- `Reroute`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `GetImageSize`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `SAM3Propagate`
- `SAM3VideoModelLoader`
- `ResizeImageMaskNode`
- `SAM3PointCollector`
- `VHS_VideoCombine`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetLatentNoiseMask`
- `LTXVAddGuideMulti`
- `CFGGuider`
- `ManualSigmas`
- `VAEDecodeTiled` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（62/64）

**有卡**：`LTXVAudioVAEDecode`、`GetImageSize+`、`ImageInvert`、`SamplerCustomAdvanced`、`EmptyImage`、`MaskToImage`、`LTXVConditioning`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`RandomNoise`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`SAM3VideoOutput`、`MaskExpandBatch+`、`ImageScaleBy`、`LTXVPreprocess`、`GrowMaskWithBlur`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`LTXVAddGuideMulti`、`VHS_VideoCombine`、`VAEEncode`、`ImageCompositeFromMaskBatch+`、`SAM3VideoSegmentation`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`SolidMask`、`GetImageSize`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`VHS_LoadVideo`、`SAM3Propagate`、`SAM3VideoModelLoader`、`ResizeImageMaskNode`、`SAM3PointCollector`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`SetLatentNoiseMask`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced、LatentUpscaleModelLoader
