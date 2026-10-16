---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2060253962829389825.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2060253962829389825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2060253962829389825.json
hash: 3a1fc8919dbdd78e
coverage: 0.913043
learned_at: 2026-10-15 22:38:46
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, ImageConcatMulti, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, ImageConcatMulti, PrimitiveStringMultiline, easy int, easy int, easy int, PreviewImage, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ClothesSegment, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoTextEncodeCached, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, SeCVideoSegmentation, DrawMaskOnImage, BlockifyMask, GrowMask, easy int, SeCModelLoader, GetImageSizeAndCount, WanVideoDecode, VHS_LoadVideo, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2060253962829389825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060253962829389825.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `ImageConcatMulti`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `easy int`
- `easy int`
- `easy int`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ClothesSegment`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `ImageBlend`
- `VHS_VideoCombine`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `SeCVideoSegmentation`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `easy int`
- `SeCModelLoader`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`ImageConcatMulti`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Evaluate Integers`、`ClothesSegment`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageBlend`、`DrawViTPose`、`PoseAndFaceDetection`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`SeCModelLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
