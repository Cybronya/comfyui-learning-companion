---
key: 视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2109959301526806530.json
name: wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2109959301526806530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2109959301526806530.json
hash: 0b73111e5083dcb8
coverage: 0.895833
learned_at: 2026-10-18 00:24:10
nodes: [WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, WanVideoDecode, LayerUtility: ImageMaskScaleAsV2, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoLoraSelectMulti, WanVideoVAELoader, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncodeCached, Evaluate Integers, easy int, WanVideoContextOptions, GetImageSizeAndCount, WanVideoBlockSwap, easy int, LayerUtility: ImageScaleByAspectRatio V2, DrawMaskOnImage, BlockifyMask, GrowMask, Note, VHS_VideoInfoLoaded, ImageFromBatch, easy int, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, PreviewImage, ClothesSegment, Evaluate Integers, OnnxDetectionModelLoader, SeCVideoSegmentation, SeCModelLoader, ImageBlend, easy showAnything, VHS_VideoCombine, VHS_LoadVideo, easy int, PrimitiveStringMultiline, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2109959301526806530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2109959301526806530.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `WanVideoTorchCompileSettings`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `WanVideoDecode`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `Evaluate Integers`
- `easy int`
- `WanVideoContextOptions`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `Note`
- `VHS_VideoInfoLoaded`
- `ImageFromBatch`
- `easy int`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `ClothesSegment`
- `Evaluate Integers`
- `OnnxDetectionModelLoader`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `ImageBlend`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `easy int`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **90%**（43/48）

**有卡**：`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoDecode`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`Evaluate Integers`、`easy int`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`VHS_VideoCombine`、`ImageConcatMulti`、`ClothesSegment`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`SeCModelLoader`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
