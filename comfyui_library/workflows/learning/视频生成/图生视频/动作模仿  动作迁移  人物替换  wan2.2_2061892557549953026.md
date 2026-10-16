---
key: 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2061892557549953026.json
name: 动作模仿  动作迁移  人物替换  wan2.2_2061892557549953026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061892557549953026.json
hash: 6166b9618c1d0452
coverage: 0.931818
learned_at: 2026-10-15 22:38:57
nodes: [VHS_VideoInfoLoaded, easy int, easy showAnything, ImageConcatMulti, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, VHS_VideoCombine, PoseAndFaceDetection, OnnxDetectionModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, LoadImage, easy int, easy int, Evaluate Integers, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, ImageFromBatch, ClothesSegment, SeCModelLoader, PreviewImage, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, Evaluate Integers, DrawViTPose, ImageConcatMulti, WanVideoClipVisionEncode, ImageBlend, WanVideoContextOptions, WanVideoVAELoader, CLIPVisionLoader, WanVideoAnimateEmbeds, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移  人物替换  wan2.2_2061892557549953026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061892557549953026.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `VHS_VideoInfoLoaded`
- `easy int`
- `easy showAnything`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LoadImage`
- `easy int`
- `easy int`
- `Evaluate Integers`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `PreviewImage`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `Evaluate Integers`
- `DrawViTPose`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`VHS_VideoInfoLoaded`、`easy int`、`ImageConcatMulti`、`VHS_VideoCombine`、`LayerUtility: ImageMaskScaleAsV2`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadImage`、`Evaluate Integers`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`DrawViTPose`、`WanVideoClipVisionEncode`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
