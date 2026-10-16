---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066236925765316609.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2066236925765316609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2066236925765316609.json
hash: 181457183e452e51
coverage: 0.974359
learned_at: 2026-10-15 22:39:47
nodes: [VHS_VideoCombine, WanVideoModelLoader, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoAnimateEmbeds, WanVideoContextOptions, Evaluate Integers, WanVideoClipVisionEncode, CLIPVisionLoader, ImageConcatMulti, WanVideoVAELoader, PoseAndFaceDetection, VHS_VideoCombine, DrawViTPose, ImageBlend, OnnxDetectionModelLoader, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoInfoLoaded, easy showAnything, easy int, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, SeCVideoSegmentation, ClothesSegment, SeCModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoTextEncodeCached, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066236925765316609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066236925765316609.json`

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
- `WanVideoVAELoader`
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
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`VHS_VideoCombine`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageBlend`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoInfoLoaded`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`SeCVideoSegmentation`、`ClothesSegment`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
