---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062929462974570497.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2062929462974570497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062929462974570497.json
hash: 3199f44309d794d9
coverage: 0.931818
learned_at: 2026-10-15 22:39:09
nodes: [VHS_LoadVideo, ImageConcatMulti, VHS_VideoCombine, LoadImage, easy int, easy int, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, LayerUtility: ImageMaskScaleAsV2, easy showAnything, VHS_VideoInfoLoaded, PreviewImage, SeCModelLoader, easy int, ClothesSegment, WanVideoTextEncodeCached, ImageFromBatch, SeCVideoSegmentation, PreviewImage, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, ImageBlend, DrawMaskOnImage, GrowMask, BlockifyMask, CLIPVisionLoader, Evaluate Integers, WanVideoContextOptions, ImageConcatMulti, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoModelLoader, WanVideoSampler, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoDecode, GetImageSizeAndCount, OnnxDetectionModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062929462974570497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062929462974570497.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LoadImage`
- `easy int`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `PreviewImage`
- `SeCModelLoader`
- `easy int`
- `ClothesSegment`
- `WanVideoTextEncodeCached`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `PreviewImage`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `ImageBlend`
- `DrawMaskOnImage`
- `GrowMask`
- `BlockifyMask`
- `CLIPVisionLoader`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`VHS_LoadVideo`、`ImageConcatMulti`、`VHS_VideoCombine`、`LoadImage`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`Evaluate Integers`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`ClothesSegment`、`WanVideoTextEncodeCached`、`ImageFromBatch`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageBlend`、`DrawMaskOnImage`、`GrowMask`、`BlockifyMask`、`CLIPVisionLoader`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
