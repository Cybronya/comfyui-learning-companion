---
key: 数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1996134086378995713.json
name: Wan2.2-视频人物替换对口型（长视频版）_1996134086378995713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1996134086378995713.json
hash: 1468b7d6d8d69d49
coverage: 0.897959
learned_at: 2026-10-26 01:57:58
nodes: [easy int, SeCVideoSegmentation, ImageFromBatch, ClothesSegment, SeCModelLoader, easy int, GrowMask, BlockifyMask, DrawViTPose, PoseAndFaceDetection, ImageBlend, PreviewImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoLoraSelectMulti, Evaluate Integers, WanVideoSampler, WanVideoTextEncodeCached, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoContextOptions, PreviewImage, PreviewImage, VHS_VideoCombine, OnnxDetectionModelLoader, VHS_VideoCombine, easy int, GetImageSizeAndCount, easy showAnything, VHS_VideoInfoLoaded, WanVideoDecode, easy int, LoadImage, VHS_LoadVideo, WanVideoTorchCompileSettings, WanVideoModelLoader, PlaySound|pysssss, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, DrawMaskOnImage, WanVideoSetBlockSwap, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1996134086378995713.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1996134086378995713.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（49 个）：
- `easy int`
- `SeCVideoSegmentation`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `easy int`
- `GrowMask`
- `BlockifyMask`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `ImageBlend`
- `PreviewImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `Evaluate Integers`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `easy int`
- `GetImageSizeAndCount`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `WanVideoDecode`
- `easy int`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `PlaySound|pysssss`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`easy int`、`SeCVideoSegmentation`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`GrowMask`、`BlockifyMask`、`DrawViTPose`、`PoseAndFaceDetection`、`ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`Evaluate Integers`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`LoadImage`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`PlaySound|pysssss`、`ImageConcatMulti`、`DrawMaskOnImage`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
