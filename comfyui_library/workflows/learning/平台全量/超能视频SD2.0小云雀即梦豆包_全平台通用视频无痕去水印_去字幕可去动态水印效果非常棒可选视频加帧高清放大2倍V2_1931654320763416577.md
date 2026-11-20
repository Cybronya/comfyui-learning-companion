---
key: 平台全量/超能视频SD2.0小云雀即梦豆包_全平台通用视频无痕去水印_去字幕可去动态水印效果非常棒可选视频加帧高清放大2倍V2_1931654320763416577.json
name: 超能视频SD2.0小云雀即梦豆包_全平台通用视频无痕去水印_去字幕可去动态水印效果非常棒可选视频加帧高清放大2倍V2_1931654320763416577
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/超能视频SD2.0小云雀即梦豆包_全平台通用视频无痕去水印_去字幕可去动态水印效果非常棒可选视频加帧高清放大2倍V2_1931654320763416577.json
hash: 7eb46de404f7aeea
coverage: 0.538462
learned_at: 2026-11-14 02:47:04
nodes: [GetNode, SeedVR2BlockSwap, SeedVR2ExtraArgs, PreviewImage, SetNode, easy convertAnything, SetNode, SetNode, MathExpression|pysssss, SetNode, GetNode, GetNode, GetNode, easy int, MathExpression|pysssss, SetNode, WanVideoDecode, GetNode, SetNode, GetNode, ImageFromBatch, Note, Int, GetNode, GetNode, GetNode, GetNode, easy showTensorShape, GetNode, GetNode, GetNode, Note, SetNode, LayerUtility: PurgeVRAM V2, GetNode, GetNode, ConditioningZeroOut, ConditioningZeroOut, ImageFromBatch+, SetNode, easy int, GetNode, GetNode, UNETLoader, Anything Everywhere, CLIPLoader, SetNode, GetNode, GIMMVFI_interpolate, GetNode, ImageConcanate, PDIMAGE_LongerSize, PDIMAGE_LongerSize, VHS_VideoCombine, GetNode, SetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, DrawMaskOnImage, LayerMask: MaskGrow, SetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, VAELoader, SetNode, GetNode, ReferenceLatent, CLIPTextEncode, VAEDecode, VAEEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, easy int, VHS_VideoCombine, ImageConcanate, GetNode, SaveImage, easy cleanGpuUsed, GetNode, GetNode, MarkdownNote, VHS_LoadVideo, SaveImage, PreviewImage, WanVideoClipVisionEncode, CLIPVisionLoader, FlashVSRNode, DownloadAndLoadGIMMVFIModel, MathExpression|pysssss, JWInteger, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM V2, MemoryCleaner, LayerUtility: PurgeVRAM V2, MemoryCleaner, ColorMatch, LoadImage, VHS_VideoCombine, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoLoraSelect, WanVideoModelLoader, GrowMaskWithBlur, GetNode, GetNode, GetNode, SetNode, easy imageSize, EmptyFlux2LatentImage, Anything Everywhere, LoadImage, MarkdownNote, Image Comparer (rgthree), PreviewImage, ImageResizeKJv2, VHS_DuplicateMasks, GetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, BlockifyMask, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, SeedVR2GGUF, Fast Groups Bypasser (rgthree), ImageResizeKJv2, WanVideoSampler, easy int]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 891916394088529, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/超能视频SD2.0小云雀即梦豆包_全平台通用视频无痕去水印_去字幕可去动态水印效果非常棒可选视频加帧高清放大2倍V2_1931654320763416577.json

> 来源文件 `comfyui_library/workflows/平台全量/超能视频SD2.0小云雀即梦豆包_全平台通用视频无痕去水印_去字幕可去动态水印效果非常棒可选视频加帧高清放大2倍V2_1931654320763416577.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（143 个）：
- `GetNode`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `PreviewImage`
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `MathExpression|pysssss`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `Note`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showTensorShape`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `ImageFromBatch+`
- `SetNode`
- `easy int`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `Anything Everywhere`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `LayerMask: MaskGrow`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `easy int`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetNode`
- `SaveImage`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `VHS_LoadVideo`
- `SaveImage`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `FlashVSRNode`
- `DownloadAndLoadGIMMVFIModel`
- `MathExpression|pysssss`
- `JWInteger`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `LayerUtility: PurgeVRAM V2`
- `MemoryCleaner`
- `LayerUtility: PurgeVRAM V2`
- `MemoryCleaner`
- `ColorMatch`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy imageSize`
- `EmptyFlux2LatentImage`
- `Anything Everywhere`
- `LoadImage`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ImageResizeKJv2`
- `VHS_DuplicateMasks`
- `GetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `BlockifyMask`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SeedVR2GGUF`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `easy int`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `891916394088529`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（77/143）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`easy convertAnything`、`MathExpression|pysssss`、`easy int`、`WanVideoDecode`、`ImageFromBatch`、`Int`、`easy showTensorShape`、`LayerUtility: PurgeVRAM V2`、`ConditioningZeroOut`、`ImageFromBatch+`、`UNETLoader`、`CLIPLoader`、`GIMMVFI_interpolate`、`ImageConcanate`、`PDIMAGE_LongerSize`、`VHS_VideoCombine`、`DrawMaskOnImage`、`LayerMask: MaskGrow`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSize`、`VAELoader`、`ReferenceLatent`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`KSampler`、`SaveImage`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`FlashVSRNode`、`DownloadAndLoadGIMMVFIModel`、`JWInteger`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`MemoryCleaner`、`ColorMatch`、`LoadImage`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`GrowMaskWithBlur`、`EmptyFlux2LatentImage`、`ImageResizeKJv2`、`VHS_DuplicateMasks`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`BlockifyMask`、`WanVideoBlockSwap`、`SeedVR2GGUF`、`WanVideoSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
