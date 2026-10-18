---
key: 视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2062004447684947969.json
name: wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2062004447684947969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2062004447684947969.json
hash: 4ea094a048a5b573
coverage: 0.843137
learned_at: 2026-10-15 22:38:58
nodes: [WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, WanVideoDecode, LayerUtility: ImageMaskScaleAsV2, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, PreviewImage, WanVideoLoraSelectMulti, WanVideoVAELoader, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncodeCached, Evaluate Integers, easy int, VHS_VideoCombine, WanVideoContextOptions, GetImageSizeAndCount, WanVideoBlockSwap, easy int, LayerUtility: ImageScaleByAspectRatio V2, DrawMaskOnImage, BlockifyMask, GrowMask, Note, VHS_VideoInfoLoaded, ImageFromBatch, easy int, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, PreviewImage, ClothesSegment, Evaluate Integers, OnnxDetectionModelLoader, SeCVideoSegmentation, SeCModelLoader, ImageBlend, easy showAnything, VHS_VideoCombine, VHS_LoadVideo, easy int, PrimitiveStringMultiline, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2062004447684947969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062004447684947969.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `WanVideoTorchCompileSettings`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
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
- `VHS_VideoCombine`
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
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`WanVideoDecode`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`Evaluate Integers`、`easy int`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`ImageConcatMulti`、`ClothesSegment`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`SeCModelLoader`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
