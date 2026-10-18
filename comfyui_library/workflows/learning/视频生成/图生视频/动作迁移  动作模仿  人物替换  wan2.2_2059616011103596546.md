---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2059616011103596546.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2059616011103596546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2059616011103596546.json
hash: 68a3d63d59636b4b
coverage: 0.913043
learned_at: 2026-10-15 22:38:41
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, easy int, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, ImageConcatMulti, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, GrowMask, BlockifyMask, DrawMaskOnImage, SeCModelLoader, SeCVideoSegmentation, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, ImageBlend, WanVideoAnimateEmbeds, ImageConcatMulti, PrimitiveStringMultiline, easy int, easy int, easy int, PreviewImage, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ClothesSegment, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage, WanVideoModelLoader, WanVideoDecode, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoContextOptions, WanVideoSampler, WanVideoClipVisionEncode, Evaluate Integers, GetImageSizeAndCount]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2059616011103596546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059616011103596546.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `ImageConcatMulti`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoAnimateEmbeds`
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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `GetImageSizeAndCount`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`easy int`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`ImageConcatMulti`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoAnimateEmbeds`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Evaluate Integers`、`ClothesSegment`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
