---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062254625524371457.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2062254625524371457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062254625524371457.json
hash: bd66132c261aa987
coverage: 0.913043
learned_at: 2026-10-15 22:39:02
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, easy int, easy int, easy int, PreviewImage, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ClothesSegment, WanVideoTorchCompileSettings, WanVideoTextEncodeCached, Evaluate Integers, WanVideoClipVisionEncode, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, SeCVideoSegmentation, DrawMaskOnImage, BlockifyMask, GrowMask, easy int, SeCModelLoader, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VHS_LoadVideo, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2062254625524371457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062254625524371457.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Evaluate Integers`、`ClothesSegment`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`SeCModelLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
