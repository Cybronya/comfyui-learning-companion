---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062409203007967233.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2062409203007967233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062409203007967233.json
hash: a5c31ed68ff204b0
coverage: 0.931818
learned_at: 2026-10-15 22:39:03
nodes: [WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, WanVideoTorchCompileSettings, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, easy int, easy int, Evaluate Integers, VHS_LoadVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy showAnything, PreviewImage, ImageFromBatch, easy int, ClothesSegment, WanVideoTextEncodeCached, GrowMask, BlockifyMask, DrawMaskOnImage, SeCVideoSegmentation, SeCModelLoader, PreviewImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062409203007967233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062409203007967233.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
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
- `PoseAndFaceDetection`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `easy int`
- `easy int`
- `Evaluate Integers`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `PreviewImage`
- `ImageFromBatch`
- `easy int`
- `ClothesSegment`
- `WanVideoTextEncodeCached`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `PreviewImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`easy int`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`ClothesSegment`、`WanVideoTextEncodeCached`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCVideoSegmentation`、`SeCModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
