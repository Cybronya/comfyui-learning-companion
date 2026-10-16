---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2068230684107427842.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2068230684107427842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2068230684107427842.json
hash: 14be0816c7e4c6a6
coverage: 0.974359
learned_at: 2026-10-15 22:40:17
nodes: [VHS_VideoCombine, WanVideoModelLoader, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoAnimateEmbeds, WanVideoContextOptions, Evaluate Integers, WanVideoClipVisionEncode, CLIPVisionLoader, ImageConcatMulti, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, easy int, ImageFromBatch, SeCVideoSegmentation, ClothesSegment, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoTextEncodeCached, GrowMask, BlockifyMask, DrawMaskOnImage, WanVideoVAELoader, ImageBlend, DrawViTPose, LayerUtility: ImageMaskScaleAsV2, SeCModelLoader, easy showAnything, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2068230684107427842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068230684107427842.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageConcatMulti`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `easy int`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `ImageBlend`
- `DrawViTPose`
- `LayerUtility: ImageMaskScaleAsV2`
- `SeCModelLoader`
- `easy showAnything`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`VHS_VideoCombine`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`easy int`、`ImageFromBatch`、`SeCVideoSegmentation`、`ClothesSegment`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoVAELoader`、`ImageBlend`、`DrawViTPose`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
