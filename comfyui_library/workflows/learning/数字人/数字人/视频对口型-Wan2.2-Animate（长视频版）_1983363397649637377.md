---
key: 数字人/数字人/视频对口型-Wan2.2-Animate（长视频版）_1983363397649637377.json
name: 视频对口型-Wan2.2-Animate（长视频版）_1983363397649637377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频对口型-Wan2.2-Animate（长视频版）_1983363397649637377.json
hash: a89e3c1836a3659e
coverage: 0.888889
learned_at: 2026-10-26 02:05:01
nodes: [WanVideoTorchCompileSettings, easy int, SeCVideoSegmentation, ImageFromBatch, ClothesSegment, SeCModelLoader, easy int, GrowMask, BlockifyMask, DrawMaskOnImage, DrawViTPose, PoseAndFaceDetection, ImageBlend, PreviewImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, CLIPVisionLoader, Evaluate Integers, WanVideoSampler, WanVideoTextEncodeCached, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoContextOptions, PreviewImage, PreviewImage, VHS_VideoCombine, LoadImage, OnnxDetectionModelLoader, VHS_VideoCombine, WanVideoBlockSwap, LoadImage, ImageConcatMulti, PrimitiveStringMultiline, easy int, LoadImage, VHS_LoadVideo, GetImageSizeAndCount, easy showAnything, VHS_LoadVideo, VHS_VideoInfoLoaded, VHS_VideoCombine, WanVideoDecode, WanVideoVAELoader, ImageConcatMulti, PlaySound|pysssss, easy int, VHS_LoadVideo, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
---

# 数字人/数字人/视频对口型-Wan2.2-Animate（长视频版）_1983363397649637377.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频对口型-Wan2.2-Animate（长视频版）_1983363397649637377.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（54 个）：
- `WanVideoTorchCompileSettings`
- `easy int`
- `SeCVideoSegmentation`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `easy int`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `ImageBlend`
- `PreviewImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
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
- `LoadImage`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadImage`
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `easy int`
- `LoadImage`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `easy showAnything`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `ImageConcatMulti`
- `PlaySound|pysssss`
- `easy int`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `MarkdownNote`

## 知识

覆盖率 **89%**（48/54）

**有卡**：`WanVideoTorchCompileSettings`、`easy int`、`SeCVideoSegmentation`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`DrawViTPose`、`PoseAndFaceDetection`、`ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`Evaluate Integers`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LoadImage`、`OnnxDetectionModelLoader`、`WanVideoBlockSwap`、`ImageConcatMulti`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`WanVideoVAELoader`、`PlaySound|pysssss`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
