---
key: 平台全量/Wan2.2  Animate视频换头原理展示_2031980576953081857.json
name: Wan2.2  Animate视频换头原理展示_2031980576953081857
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2  Animate视频换头原理展示_2031980576953081857.json
hash: c53edb5a20ab5f3a
coverage: 0.695122
learned_at: 2026-11-14 01:04:49
nodes: [GetNode, GetNode, GetNode, GetNode, WanVideoSetLoRAs, SetNode, VHS_VideoInfo, WanVideoSetBlockSwap, JWInteger, GetNode, VAELoader, KSampler, VAEEncode, CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, UNETLoader, LayerUtility: PurgeVRAM, CLIPLoader, TextEncodeQwenImageEdit, CLIPTextEncode, easy cleanGpuUsed, VAEDecode, LayerUtility: ImageRemoveAlpha, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, SetNode, BlockifyMask, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoBlockSwap, CLIPVisionLoader, LayerUtility: PurgeVRAM, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, easy cleanGpuUsed, PreviewImage, ImageResizeKJv2, LayerMask: SegformerB2ClothesUltra, LayerMask: SegformerB2ClothesUltra, GrowMask, SetNode, GetNode, JWInteger, VHS_LoadVideo, SetNode, SetNode, SetNode, LoadImage, DWPreprocessor, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, DrawMaskOnImage, SetNode, VHS_VideoCombine, Reroute, PixelPerfectResolution, SetNode, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, ImageResizeKJv2, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoSampler, AutoCropFaces, ImageAndMaskPreview, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 619934556475807, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2  Animate视频换头原理展示_2031980576953081857.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2  Animate视频换头原理展示_2031980576953081857.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `VHS_VideoInfo`
- `WanVideoSetBlockSwap`
- `JWInteger`
- `GetNode`
- `VAELoader`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `TextEncodeQwenImageEdit`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `LayerUtility: ImageRemoveAlpha`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `SetNode`
- `BlockifyMask`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `PreviewImage`
- `ImageResizeKJv2`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerMask: SegformerB2ClothesUltra`
- `GrowMask`
- `SetNode`
- `GetNode`
- `JWInteger`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `DWPreprocessor`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `Reroute`
- `PixelPerfectResolution`
- `SetNode`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `ImageResizeKJv2`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `AutoCropFaces`
- `ImageAndMaskPreview`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `619934556475807`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **70%**（57/82）

**有卡**：`WanVideoSetLoRAs`、`VHS_VideoInfo`、`WanVideoSetBlockSwap`、`JWInteger`、`VAELoader`、`KSampler`、`VAEEncode`、`CFGNorm`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`CLIPLoader`、`TextEncodeQwenImageEdit`、`CLIPTextEncode`、`VAEDecode`、`LayerUtility: ImageRemoveAlpha`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoModelLoader`、`BlockifyMask`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`LayerMask: SegformerB2ClothesUltra`、`GrowMask`、`VHS_LoadVideo`、`LoadImage`、`DWPreprocessor`、`ImageConcatMulti`、`DrawMaskOnImage`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`AutoCropFaces`、`ImageAndMaskPreview`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
