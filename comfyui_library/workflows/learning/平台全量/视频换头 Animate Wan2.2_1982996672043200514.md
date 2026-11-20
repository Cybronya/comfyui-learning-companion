---
key: 平台全量/视频换头 Animate Wan2.2_1982996672043200514.json
name: 视频换头 Animate Wan2.2_1982996672043200514
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频换头 Animate Wan2.2_1982996672043200514.json
hash: bc5a6c3df98ab67c
coverage: 0.701299
learned_at: 2026-11-14 02:38:27
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, Reroute, VAELoader, WanVideoDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, PixelPerfectResolution, SetNode, ImageConcatMulti, VAEDecode, WanVideoBlockSwap, GrowMask, LayerUtility: PurgeVRAM, SetNode, WanVideoVAELoader, DrawMaskOnImage, LayerMask: SegformerB2ClothesUltra, GetNode, CLIPLoader, ModelSamplingAuraFlow, LayerUtility: PurgeVRAM, UNETLoader, easy cleanGpuUsed, CFGNorm, easy cleanGpuUsed, KSampler, WanVideoSetLoRAs, LayerUtility: ImageRemoveAlpha, LayerMask: SegformerB2ClothesUltra, ImageResizeKJv2, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoModelLoader, easy cleanGpuUsed, SetNode, SetNode, SetNode, WanVideoLoraSelectMulti, ImageAndMaskPreview, TextEncodeQwenImageEdit, VAEEncode, VHS_VideoCombine, ImageConcatMulti, VHS_VideoInfo, VHS_VideoCombine, SetNode, WanVideoSetBlockSwap, AutoCropFaces, ImageResizeKJv2, SetNode, ImageResizeKJv2, VHS_LoadVideo, JWInteger, JWInteger, SetNode, LoadImage, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, GetNode, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, SetNode, SetNode, SetNode, GetNode, BlockifyMask]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 364463264461593, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/视频换头 Animate Wan2.2_1982996672043200514.json

> 来源文件 `comfyui_library/workflows/平台全量/视频换头 Animate Wan2.2_1982996672043200514.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（77 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Reroute`
- `VAELoader`
- `WanVideoDecode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PixelPerfectResolution`
- `SetNode`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `WanVideoBlockSwap`
- `GrowMask`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoVAELoader`
- `DrawMaskOnImage`
- `LayerMask: SegformerB2ClothesUltra`
- `GetNode`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `CFGNorm`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `WanVideoSetLoRAs`
- `LayerUtility: ImageRemoveAlpha`
- `LayerMask: SegformerB2ClothesUltra`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `ImageAndMaskPreview`
- `TextEncodeQwenImageEdit`
- `VAEEncode` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoSetBlockSwap`
- `AutoCropFaces`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `BlockifyMask`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `364463264461593`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **70%**（54/77）

**有卡**：`CLIPTextEncode`、`VAELoader`、`WanVideoDecode`、`LoraLoaderModelOnly`、`PixelPerfectResolution`、`ImageConcatMulti`、`VAEDecode`、`WanVideoBlockSwap`、`GrowMask`、`LayerUtility: PurgeVRAM`、`WanVideoVAELoader`、`DrawMaskOnImage`、`LayerMask: SegformerB2ClothesUltra`、`CLIPLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`easy cleanGpuUsed`、`CFGNorm`、`KSampler`、`WanVideoSetLoRAs`、`LayerUtility: ImageRemoveAlpha`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageAndMaskPreview`、`TextEncodeQwenImageEdit`、`VAEEncode`、`VHS_VideoCombine`、`VHS_VideoInfo`、`WanVideoSetBlockSwap`、`AutoCropFaces`、`VHS_LoadVideo`、`JWInteger`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`BlockifyMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
