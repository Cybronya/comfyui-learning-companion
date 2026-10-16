---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062242927623106561.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2062242927623106561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062242927623106561.json
hash: 940298e5d41826c6
coverage: 0.931818
learned_at: 2026-10-15 22:39:02
nodes: [Evaluate Integers, WanVideoContextOptions, Evaluate Integers, easy int, easy int, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, ClothesSegment, VHS_VideoInfoLoaded, easy showAnything, LayerUtility: ImageMaskScaleAsV2, PreviewImage, PreviewImage, ImageFromBatch, DrawMaskOnImage, BlockifyMask, GrowMask, LoadImage, OnnxDetectionModelLoader, VHS_VideoCombine, ImageBlend, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoAnimateEmbeds, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncodeCached, SeCVideoSegmentation, easy int, SeCModelLoader, PoseAndFaceDetection, DrawViTPose]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062242927623106561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062242927623106561.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `Evaluate Integers`
- `WanVideoContextOptions`
- `Evaluate Integers`
- `easy int`
- `easy int`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ClothesSegment`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `SeCVideoSegmentation`
- `easy int`
- `SeCModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`Evaluate Integers`、`WanVideoContextOptions`、`easy int`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`ClothesSegment`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`LoadImage`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`SeCModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
