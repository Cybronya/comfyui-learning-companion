---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2065012164380942338.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2065012164380942338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2065012164380942338.json
hash: 3e67663da634cced
coverage: 0.931818
learned_at: 2026-10-15 22:39:34
nodes: [easy int, ImageConcatMulti, VHS_VideoCombine, PreviewImage, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, PoseAndFaceDetection, OnnxDetectionModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoContextOptions, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageConcatMulti, GrowMask, BlockifyMask, DrawMaskOnImage, ImageBlend, VHS_VideoInfoLoaded, easy showAnything, Evaluate Integers, Evaluate Integers, easy int, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, WanVideoVAELoader, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, VHS_VideoCombine, PreviewImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2065012164380942338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065012164380942338.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `easy int`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
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
- `DrawMaskOnImage`
- `ImageBlend`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `Evaluate Integers`
- `Evaluate Integers`
- `easy int`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `PreviewImage`
- `LoadImage`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`easy int`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageBlend`、`VHS_VideoInfoLoaded`、`Evaluate Integers`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
