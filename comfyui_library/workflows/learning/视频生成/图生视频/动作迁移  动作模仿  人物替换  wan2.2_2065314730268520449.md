---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2065314730268520449.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2065314730268520449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2065314730268520449.json
hash: ffcd066ff74f2998
coverage: 0.931818
learned_at: 2026-10-15 22:39:37
nodes: [ImageConcatMulti, VHS_VideoCombine, PreviewImage, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, PoseAndFaceDetection, OnnxDetectionModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, WanVideoContextOptions, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageConcatMulti, GrowMask, BlockifyMask, DrawMaskOnImage, ImageBlend, VHS_VideoInfoLoaded, easy showAnything, Evaluate Integers, Evaluate Integers, easy int, LayerUtility: ImageMaskScaleAsV2, PreviewImage, easy int, ImageFromBatch, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, WanVideoVAELoader, VHS_LoadVideo, easy int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2065314730268520449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065314730268520449.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
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
- `DrawMaskOnImage`
- `ImageBlend`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `Evaluate Integers`
- `Evaluate Integers`
- `easy int`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `easy int`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageBlend`、`VHS_VideoInfoLoaded`、`Evaluate Integers`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
