---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064254893577297921.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2064254893577297921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064254893577297921.json
hash: b2b07b6070c58bb0
coverage: 0.974359
learned_at: 2026-10-15 22:39:22
nodes: [WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, WanVideoTorchCompileSettings, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, BlockifyMask, PoseAndFaceDetection, easy int, easy showAnything, SeCModelLoader, ImageFromBatch, DrawMaskOnImage, WanVideoTextEncodeCached, GrowMask, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064254893577297921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064254893577297921.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `ImageBlend`
- `VHS_VideoCombine`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `BlockifyMask`
- `PoseAndFaceDetection`
- `easy int`
- `easy showAnything`
- `SeCModelLoader`
- `ImageFromBatch`
- `DrawMaskOnImage`
- `WanVideoTextEncodeCached`
- `GrowMask`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`BlockifyMask`、`PoseAndFaceDetection`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`DrawMaskOnImage`、`WanVideoTextEncodeCached`、`GrowMask`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
