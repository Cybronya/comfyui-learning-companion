---
key: 视频生成/图生视频/Wan2.2-Animate_v2 KJ版：精准替换（全新Sec遮罩方案）_2008854947357532162.json
name: Wan2.2-Animate_v2 KJ版：精准替换（全新Sec遮罩方案）_2008854947357532162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008854947357532162.json
hash: b804d628328bd25e
coverage: 0.677966
learned_at: 2026-10-15 22:34:09
nodes: [WanVideoDecode, easy int, easy int, easy int, PoseAndFaceDetection, GrowMask, VHS_VideoInfoLoaded, Evaluate Integers, SetNode, BlockifyMask, SeCModelLoader, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanVideoSampler, GetNode, PrimitiveStringMultiline, DrawMaskOnImage, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoAnimateEmbeds, LayerUtility: ImageMaskScaleAsV2, OnnxDetectionModelLoader, easy int, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, DrawViTPose, RHHiddenNodes, SetNode, SetNode, VHS_LoadVideo, ImageConcatMulti, GetNode, GetImageSizeAndCount, GetNode, ImageBlend, ImageConcatMulti, VHS_VideoCombine, WanVideoBlockSwap, ClothesSegment, ClothesSegment, Note, SeCVideoSegmentation, VHS_VideoCombine, ClothesSegment, ImpactSwitch, ImageFromBatch, Evaluate Integers, WanVideoContextOptions, GetNode, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate_v2 KJ版：精准替换（全新Sec遮罩方案）_2008854947357532162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008854947357532162.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（59 个）：
- `WanVideoDecode`
- `easy int`
- `easy int`
- `easy int`
- `PoseAndFaceDetection`
- `GrowMask`
- `VHS_VideoInfoLoaded`
- `Evaluate Integers`
- `SetNode`
- `BlockifyMask`
- `SeCModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetNode`
- `PrimitiveStringMultiline`
- `DrawMaskOnImage`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `LayerUtility: ImageMaskScaleAsV2`
- `OnnxDetectionModelLoader`
- `easy int`
- `WanVideoSetBlockSwap`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `DrawViTPose`
- `RHHiddenNodes`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBlend`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `ClothesSegment`
- `ClothesSegment`
- `Note`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `ClothesSegment`
- `ImpactSwitch`
- `ImageFromBatch`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **68%**（40/59）

**有卡**：`WanVideoDecode`、`easy int`、`PoseAndFaceDetection`、`GrowMask`、`VHS_VideoInfoLoaded`、`Evaluate Integers`、`BlockifyMask`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoSampler`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`LayerUtility: ImageMaskScaleAsV2`、`OnnxDetectionModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`DrawViTPose`、`RHHiddenNodes`、`VHS_LoadVideo`、`ImageConcatMulti`、`GetImageSizeAndCount`、`ImageBlend`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`ClothesSegment`、`SeCVideoSegmentation`、`ImageFromBatch`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、CLIPVisionLoader、GetImageSizeAndCount
