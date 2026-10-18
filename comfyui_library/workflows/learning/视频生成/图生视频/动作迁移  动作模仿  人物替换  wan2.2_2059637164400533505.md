---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2059637164400533505.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2059637164400533505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2059637164400533505.json
hash: 6254b83c5d3b633e
coverage: 0.913043
learned_at: 2026-10-15 22:38:41
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, easy int, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, GrowMask, BlockifyMask, DrawMaskOnImage, SeCModelLoader, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, ImageBlend, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageConcatMulti, easy int, easy int, easy int, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, VHS_LoadVideo, LoadImage, WanVideoTextEncodeCached, PreviewImage, ClothesSegment, PrimitiveStringMultiline, WanVideoTorchCompileSettings, WanVideoDecode, GetImageSizeAndCount, Evaluate Integers, WanVideoContextOptions, SeCVideoSegmentation, PreviewImage, WanVideoSampler, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2059637164400533505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059637164400533505.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `ImageConcatMulti`
- `easy int`
- `easy int`
- `easy int`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `ClothesSegment`
- `PrimitiveStringMultiline`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `SeCVideoSegmentation`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`easy int`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`ImageConcatMulti`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Evaluate Integers`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncodeCached`、`ClothesSegment`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`SeCVideoSegmentation`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
