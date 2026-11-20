---
key: 平台全量/wan2.2视频换人_换脸_换装_2046478047649472514.json
name: wan2.2视频换人_换脸_换装_2046478047649472514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2视频换人_换脸_换装_2046478047649472514.json
hash: bfec218c1945238b
coverage: 0.653333
learned_at: 2026-11-14 01:19:52
nodes: [WanVideoDecode, WanVideoModelLoader, easy int, WanVideoTorchCompileSettings, WanVideoSetLoRAs, SetNode, VHS_VideoInfoLoaded, SetNode, easy showAnything, Evaluate Integers, SetNode, BlockifyMask, SeCModelLoader, GetNode, GetNode, Evaluate Integers, WanVideoContextOptions, GetNode, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, GetNode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, GetNode, ImageBlend, GetNode, PrimitiveStringMultiline, GetNode, SetNode, SeCVideoSegmentation, PreviewImage, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, OnnxDetectionModelLoader, CreateVideo, PreViewVideo, VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes, RHHiddenNodes, Note, GetNode, ClothesSegment, ClothesSegment, Note, VHS_VideoCombine, WanVideoSetBlockSwap, SetNode, WanVideoBlockSwap, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, ClothesSegment, ImageFromBatch, easy int, LoadImage, LayerUtility: ImageMaskScaleAsV2, GrowMask, PreviewImage, GetNode, DrawViTPose, PoseAndFaceDetection, VHS_VideoCombine, DrawMaskOnImage, GetNode, LoadImage, Note, easy int, VHS_LoadVideo, easy int, Fast Groups Bypasser (rgthree), ImpactSwitch]
patterns: []
missing: []
---

# 平台全量/wan2.2视频换人_换脸_换装_2046478047649472514.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2视频换人_换脸_换装_2046478047649472514.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（75 个）：
- `WanVideoDecode`
- `WanVideoModelLoader`
- `easy int`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `easy showAnything`
- `Evaluate Integers`
- `SetNode`
- `BlockifyMask`
- `SeCModelLoader`
- `GetNode`
- `GetNode`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `GetNode`
- `ImageBlend`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `SeCVideoSegmentation`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `OnnxDetectionModelLoader`
- `CreateVideo`
- `PreViewVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Note`
- `GetNode`
- `ClothesSegment`
- `ClothesSegment`
- `Note`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `ClothesSegment`
- `ImageFromBatch`
- `easy int`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `GrowMask`
- `PreviewImage`
- `GetNode`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `GetNode`
- `LoadImage`
- `Note`
- `easy int`
- `VHS_LoadVideo`
- `easy int`
- `Fast Groups Bypasser (rgthree)`
- `ImpactSwitch`

## 知识

覆盖率 **65%**（49/75）

**有卡**：`WanVideoDecode`、`WanVideoModelLoader`、`easy int`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`VHS_VideoInfoLoaded`、`Evaluate Integers`、`BlockifyMask`、`SeCModelLoader`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`ImageBlend`、`SeCVideoSegmentation`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`CreateVideo`、`PreViewVideo`、`VHS_VideoCombine`、`RHHiddenNodes`、`ClothesSegment`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageFromBatch`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`GrowMask`、`DrawViTPose`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
