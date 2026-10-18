---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066397148832419841.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2066397148832419841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066397148832419841.json
hash: c245588ef9fdcfd7
coverage: 0.974359
learned_at: 2026-10-15 22:39:48
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, LoadImage, easy showAnything, ImageFromBatch, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, ClothesSegment, SeCVideoSegmentation, easy int, VHS_VideoInfoLoaded, GrowMask, WanVideoVAELoader, BlockifyMask, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, CLIPVisionLoader, VHS_VideoCombine, DrawViTPose, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, Evaluate Integers, ImageBlend, WanVideoContextOptions, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, ImageConcatMulti, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066397148832419841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066397148832419841.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `LoadImage`
- `easy showAnything`
- `ImageFromBatch`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `easy int`
- `VHS_VideoInfoLoaded`
- `GrowMask`
- `WanVideoVAELoader`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`LoadImage`、`ImageFromBatch`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`SeCVideoSegmentation`、`easy int`、`VHS_VideoInfoLoaded`、`GrowMask`、`WanVideoVAELoader`、`BlockifyMask`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_VideoCombine`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
