---
key: 数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1986670264182308866.json
name: Wan2.2-视频人物替换对口型（长视频版）_1986670264182308866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1986670264182308866.json
hash: fb3287d2996a152a
coverage: 0.897959
learned_at: 2026-10-26 01:57:57
nodes: [easy int, SeCVideoSegmentation, ImageFromBatch, ClothesSegment, SeCModelLoader, easy int, GrowMask, BlockifyMask, DrawViTPose, PoseAndFaceDetection, ImageBlend, PreviewImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoLoraSelectMulti, Evaluate Integers, WanVideoSampler, WanVideoTextEncodeCached, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoContextOptions, PreviewImage, PreviewImage, VHS_VideoCombine, OnnxDetectionModelLoader, VHS_VideoCombine, PrimitiveStringMultiline, easy int, GetImageSizeAndCount, easy showAnything, VHS_VideoInfoLoaded, WanVideoDecode, easy int, LoadImage, VHS_LoadVideo, WanVideoTorchCompileSettings, WanVideoModelLoader, PlaySound|pysssss, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, DrawMaskOnImage, WanVideoSetBlockSwap, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1986670264182308866.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2-视频人物替换对口型（长视频版）_1986670264182308866.json`

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
- `PrimitiveStringMultiline`
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

## 知识

覆盖率 **90%**（44/49）

**有卡**：`easy int`、`SeCVideoSegmentation`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`GrowMask`、`BlockifyMask`、`DrawViTPose`、`PoseAndFaceDetection`、`ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`Evaluate Integers`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`LoadImage`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`PlaySound|pysssss`、`ImageConcatMulti`、`DrawMaskOnImage`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
