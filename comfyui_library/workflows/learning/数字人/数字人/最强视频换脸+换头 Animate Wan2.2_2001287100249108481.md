---
key: 数字人/数字人/最强视频换脸+换头 Animate Wan2.2_2001287100249108481.json
name: 最强视频换脸+换头 Animate Wan2.2_2001287100249108481
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/最强视频换脸+换头 Animate Wan2.2_2001287100249108481.json
hash: 6ce07d26be760e86
coverage: 0.627907
learned_at: 2026-10-26 02:03:26
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, SetNode, CLIPTextEncode, GetNode, Reroute, DWPreprocessor, VAELoader, GetNode, SetNode, WanVideoAnimateEmbeds, WanVideoDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, FaceMaskFromPoseKeypoints, CLIPVisionLoader, ImageConcatMulti, VHS_VideoInfo, PixelPerfectResolution, VAEEncode, SetNode, GetNode, JWInteger, JWInteger, ImageConcatMulti, VAEDecode, GetNode, TextEncodeQwenImageEdit, AutoCropFaces, WanVideoBlockSwap, GrowMask, BlockifyMask, LayerUtility: PurgeVRAM, SetNode, WanVideoVAELoader, GetNode, ImageResizeKJv2, DrawMaskOnImage, LayerMask: SegformerB2ClothesUltra, GetNode, SetNode, CLIPLoader, ModelSamplingAuraFlow, LayerUtility: PurgeVRAM, UNETLoader, easy cleanGpuUsed, CFGNorm, easy cleanGpuUsed, KSampler, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: ImageRemoveAlpha, SetNode, ImageAndMaskPreview, LayerMask: SegformerB2ClothesUltra, ImageResizeKJv2, SetNode, easy cleanGpuUsed, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoModelLoader, Note, LoadImage, VHS_LoadVideo]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 53405344488006, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/最强视频换脸+换头 Animate Wan2.2_2001287100249108481.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/最强视频换脸+换头 Animate Wan2.2_2001287100249108481.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（86 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Reroute`
- `DWPreprocessor`
- `VAELoader`
- `GetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `FaceMaskFromPoseKeypoints`
- `CLIPVisionLoader`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `PixelPerfectResolution`
- `VAEEncode` ★核心
- `SetNode`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `GetNode`
- `TextEncodeQwenImageEdit`
- `AutoCropFaces`
- `WanVideoBlockSwap`
- `GrowMask`
- `BlockifyMask`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `ImageResizeKJv2`
- `DrawMaskOnImage`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `CFGNorm`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageRemoveAlpha`
- `SetNode`
- `ImageAndMaskPreview`
- `LayerMask: SegformerB2ClothesUltra`
- `ImageResizeKJv2`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `Note`
- `LoadImage`
- `VHS_LoadVideo`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `53405344488006`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **63%**（54/86）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`CLIPTextEncode`、`DWPreprocessor`、`VAELoader`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`FaceMaskFromPoseKeypoints`、`CLIPVisionLoader`、`ImageConcatMulti`、`VHS_VideoInfo`、`PixelPerfectResolution`、`VAEEncode`、`JWInteger`、`VAEDecode`、`TextEncodeQwenImageEdit`、`AutoCropFaces`、`WanVideoBlockSwap`、`GrowMask`、`BlockifyMask`、`LayerUtility: PurgeVRAM`、`WanVideoVAELoader`、`DrawMaskOnImage`、`LayerMask: SegformerB2ClothesUltra`、`CLIPLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`easy cleanGpuUsed`、`CFGNorm`、`KSampler`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LayerUtility: ImageRemoveAlpha`、`ImageAndMaskPreview`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
