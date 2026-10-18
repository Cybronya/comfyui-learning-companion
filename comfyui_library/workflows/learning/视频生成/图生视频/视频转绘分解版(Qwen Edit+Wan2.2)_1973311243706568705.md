---
key: 视频生成/图生视频/视频转绘分解版(Qwen Edit+Wan2.2)_1973311243706568705.json
name: 视频转绘分解版(Qwen Edit+Wan2.2)_1973311243706568705.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频转绘分解版(Qwen Edit+Wan2.2)_1973311243706568705.json
hash: a70eb80e974045b9
coverage: 0.888889
learned_at: 2026-10-15 22:32:02
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, DWPreprocessor, PixelPerfectResolution, WanVideoUni3C_ControlnetLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, AudioSeparation, DownloadAndLoadWav2VecModel, LayerUtility: PurgeVRAM, WanVideoEncode, MultiTalkWav2VecEmbeds, WanVideoUni3C_embeds, WanVideoModelLoader, MultiTalkModelLoader, WanVideoClipVisionEncode, WanVideoDecode, FaceMaskFromPoseKeypoints, ImageResizeKJv2, CLIPVisionLoader, WanVideoAnimateEmbeds, ImageCropByMaskAndResize, SimpleMath+, WanVideoTextEncodeCached, PreviewImage, WanVideoSampler, ImageMirror, easy cleanGpuUsed, easy showAnything, JWInteger, JWInteger, Image Resize To Width, ImageResizeKJv2, GetImageSizeAndCount, ImpactInt, VHS_LoadVideo, VHS_LoadVideo, LoadImage, CR Text, VHS_VideoInfo, VHS_VideoInfo, VHS_VideoCombine, SelectVideo, VHS_LoadVideoPath, MathExpression|pysssss, DownloadAndLoadTransNetModel, CLIPLoader, VAELoader, ModelSamplingAuraFlow, CFGNorm, KSampler, VAEEncode, LoraLoaderModelOnly, Int, TransNetV2_Run, LoadVideo, easy forLoopStart, BatchCount+, ShowText|pysssss, TextEncodeQwenImageEdit, CompressImages, Text, ImageScaleToTotalPixels, PreviewImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, easy cleanGpuUsed, easy batchAnything, PreviewImage, Image Comparer (rgthree), TextEncodeQwenImageEdit, Fast Groups Bypasser (rgthree), CompressImages, PreviewImage, ImageFromBatch, PreviewImage, easy forLoopEnd, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 722479029039817, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/视频转绘分解版(Qwen Edit+Wan2.2)_1973311243706568705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973311243706568705.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `DWPreprocessor`
- `PixelPerfectResolution`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: PurgeVRAM`
- `WanVideoEncode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoUni3C_embeds`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `FaceMaskFromPoseKeypoints`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `WanVideoAnimateEmbeds`
- `ImageCropByMaskAndResize`
- `SimpleMath+`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `ImageMirror`
- `easy cleanGpuUsed`
- `easy showAnything`
- `JWInteger`
- `JWInteger`
- `Image Resize To Width`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `ImpactInt`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `CR Text`
- `VHS_VideoInfo`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `SelectVideo`
- `VHS_LoadVideoPath`
- `MathExpression|pysssss`
- `DownloadAndLoadTransNetModel`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `TransNetV2_Run`
- `LoadVideo`
- `easy forLoopStart`
- `BatchCount+`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `CompressImages`
- `Text`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy batchAnything`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEdit`
- `Fast Groups Bypasser (rgthree)`
- `CompressImages`
- `PreviewImage`
- `ImageFromBatch`
- `PreviewImage`
- `easy forLoopEnd`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `722479029039817`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（72/81）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`DWPreprocessor`、`PixelPerfectResolution`、`WanVideoUni3C_ControlnetLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`LayerUtility: PurgeVRAM`、`WanVideoEncode`、`MultiTalkWav2VecEmbeds`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`ImageCropByMaskAndResize`、`SimpleMath+`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`ImageMirror`、`easy cleanGpuUsed`、`JWInteger`、`Image Resize To Width`、`GetImageSizeAndCount`、`ImpactInt`、`VHS_LoadVideo`、`LoadImage`、`CR Text`、`VHS_VideoInfo`、`VHS_VideoCombine`、`SelectVideo`、`VHS_LoadVideoPath`、`MathExpression|pysssss`、`DownloadAndLoadTransNetModel`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`VAEEncode`、`LoraLoaderModelOnly`、`Int`、`TransNetV2_Run`、`LoadVideo`、`easy forLoopStart`、`BatchCount+`、`TextEncodeQwenImageEdit`、`CompressImages`、`Text`、`ImageScaleToTotalPixels`、`UNETLoader`、`VAEDecode`、`easy batchAnything`、`ImageFromBatch`、`easy forLoopEnd`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、WanVideoUni3C_ControlnetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
