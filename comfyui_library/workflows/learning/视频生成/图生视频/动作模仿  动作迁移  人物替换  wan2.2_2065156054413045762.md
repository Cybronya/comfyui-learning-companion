---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2065156054413045762.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2065156054413045762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2065156054413045762.json
hash: 24d934ddc352fee1
coverage: 0.931818
learned_at: 2026-10-15 22:39:36
nodes: [easy int, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, PoseAndFaceDetection, OnnxDetectionModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSampler, WanVideoContextOptions, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageConcatMulti, GrowMask, BlockifyMask, ImageBlend, VHS_VideoInfoLoaded, easy showAnything, Evaluate Integers, Evaluate Integers, easy int, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, LoadImage, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeCModelLoader, easy int, PreviewImage, DrawMaskOnImage, WanVideoVAELoader, WanVideoSetBlockSwap, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2065156054413045762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065156054413045762.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `easy int`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `ImageConcatMulti`
- `GrowMask`
- `BlockifyMask`
- `ImageBlend`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `Evaluate Integers`
- `Evaluate Integers`
- `easy int`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `LoadImage`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SeCModelLoader`
- `easy int`
- `PreviewImage`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`easy int`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`ImageConcatMulti`、`GrowMask`、`BlockifyMask`、`ImageBlend`、`VHS_VideoInfoLoaded`、`Evaluate Integers`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`LoadImage`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeCModelLoader`、`DrawMaskOnImage`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
