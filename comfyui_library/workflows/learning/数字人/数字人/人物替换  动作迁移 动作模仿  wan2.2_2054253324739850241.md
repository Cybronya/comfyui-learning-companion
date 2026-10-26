---
key: 数字人/数字人/人物替换  动作迁移 动作模仿  wan2.2_2054253324739850241.json
name: 人物替换  动作迁移 动作模仿  wan2.2_2054253324739850241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/人物替换  动作迁移 动作模仿  wan2.2_2054253324739850241.json
hash: 7f47556f0064bd0c
coverage: 0.913043
learned_at: 2026-10-26 02:00:17
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, easy int, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, WanVideoVAELoader, GrowMask, BlockifyMask, DrawMaskOnImage, SeCModelLoader, SeCVideoSegmentation, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, ImageBlend, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoSampler, easy int, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ImageConcatMulti, ImageConcatMulti, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, easy int, easy int, PrimitiveStringMultiline, VHS_VideoCombine, WanVideoTextEncodeCached, ClothesSegment, PreviewImage, GetImageSizeAndCount, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/人物替换  动作迁移 动作模仿  wan2.2_2054253324739850241.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/人物替换  动作迁移 动作模仿  wan2.2_2054253324739850241.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `WanVideoVAELoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoSampler` ★核心
- `easy int`
- `PreviewImage`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `easy int`
- `easy int`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `ClothesSegment`
- `PreviewImage`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`easy int`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`WanVideoVAELoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`ClothesSegment`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
