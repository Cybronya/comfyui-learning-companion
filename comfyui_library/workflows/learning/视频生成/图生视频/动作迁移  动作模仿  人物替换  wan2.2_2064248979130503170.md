---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064248979130503170.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2064248979130503170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064248979130503170.json
hash: 8b2101c64c63b82e
coverage: 0.931818
learned_at: 2026-10-15 22:39:22
nodes: [WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, WanVideoTorchCompileSettings, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, easy int, easy int, Evaluate Integers, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy showAnything, PreviewImage, ImageFromBatch, easy int, ClothesSegment, WanVideoTextEncodeCached, GrowMask, BlockifyMask, DrawMaskOnImage, SeCVideoSegmentation, SeCModelLoader, PreviewImage, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2064248979130503170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064248979130503170.json`

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
- `LoadImage`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`easy int`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`ClothesSegment`、`WanVideoTextEncodeCached`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCVideoSegmentation`、`SeCModelLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
