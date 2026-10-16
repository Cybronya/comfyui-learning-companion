---
key: 视频生成/图生视频/wan2.2   角色替换  人物替换  动作迁移   动作模仿_2075959064147881986.json
name: wan2.2   角色替换  人物替换  动作迁移   动作模仿_2075959064147881986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2075959064147881986.json
hash: 3a0295065446ffdb
coverage: 0.974359
learned_at: 2026-10-15 22:41:28
nodes: [WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, GrowMask, BlockifyMask, easy int, SeCVideoSegmentation, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoSetLoRAs, DrawMaskOnImage, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, ClothesSegment, ImageFromBatch, SeCModelLoader, easy showAnything, VHS_VideoInfoLoaded, LayerUtility: ImageScaleByAspectRatio V2, ImageBlend, WanVideoContextOptions, WanVideoTorchCompileSettings, WanVideoAnimateEmbeds, Evaluate Integers, DrawViTPose, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, WanVideoClipVisionEncode, CLIPVisionLoader, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2   角色替换  人物替换  动作迁移   动作模仿_2075959064147881986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075959064147881986.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GrowMask`
- `BlockifyMask`
- `easy int`
- `SeCVideoSegmentation`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoTorchCompileSettings`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`GrowMask`、`BlockifyMask`、`easy int`、`SeCVideoSegmentation`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`DrawViTPose`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
