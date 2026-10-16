---
key: 视频生成/图生视频/wan2.2 人物替换 动作模仿_2034143932388483074.json
name: wan2.2 人物替换 动作模仿_2034143932388483074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034143932388483074.json
hash: d69f3791ec0e7569
coverage: 0.913043
learned_at: 2026-10-15 22:35:43
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, easy int, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, ImageConcatMulti, VHS_LoadVideo, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, GrowMask, BlockifyMask, DrawMaskOnImage, SeCModelLoader, SeCVideoSegmentation, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, ImageBlend, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoContextOptions, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, ImageConcatMulti, PrimitiveStringMultiline, easy int, easy int, easy int, PreviewImage, PreviewImage, WanVideoTextEncodeCached, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ClothesSegment, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 人物替换 动作模仿_2034143932388483074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034143932388483074.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
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
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `easy int`
- `easy int`
- `easy int`
- `PreviewImage`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ClothesSegment`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`easy int`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`ImageConcatMulti`、`VHS_LoadVideo`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ClothesSegment`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
