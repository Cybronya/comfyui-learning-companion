---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2066882269729611777.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2066882269729611777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2066882269729611777.json
hash: 3285cffd6f5a529b
coverage: 0.974359
learned_at: 2026-10-15 22:39:54
nodes: [VHS_VideoCombine, WanVideoModelLoader, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoAnimateEmbeds, WanVideoContextOptions, Evaluate Integers, WanVideoClipVisionEncode, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, DrawViTPose, ImageBlend, OnnxDetectionModelLoader, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoInfoLoaded, easy showAnything, easy int, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, SeCVideoSegmentation, ClothesSegment, SeCModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoTextEncodeCached, ImageConcatMulti, WanVideoVAELoader, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2066882269729611777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066882269729611777.json`

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
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `DrawViTPose`
- `ImageBlend`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy int`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `SeCModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`VHS_VideoCombine`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageBlend`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoInfoLoaded`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`SeCVideoSegmentation`、`ClothesSegment`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
