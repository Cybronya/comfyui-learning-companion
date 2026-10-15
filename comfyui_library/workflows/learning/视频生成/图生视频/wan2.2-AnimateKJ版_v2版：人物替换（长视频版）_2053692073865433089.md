---
key: 视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2053692073865433089.json
name: wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2053692073865433089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2053692073865433089.json
hash: 736c38112fff58e7
coverage: 0.7
learned_at: 2026-10-15 02:41:29
nodes: [WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, WanVideoDecode, LayerUtility: ImageMaskScaleAsV2, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoLoraSelectMulti, WanVideoVAELoader, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncodeCached, Evaluate Integers, easy int, WanVideoContextOptions, GetImageSizeAndCount, WanVideoBlockSwap, easy int, LayerUtility: ImageScaleByAspectRatio V2, DrawMaskOnImage, BlockifyMask, GrowMask, Note, VHS_VideoInfoLoaded, ImageFromBatch, easy int, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, PreviewImage, ClothesSegment, Evaluate Integers, OnnxDetectionModelLoader, SeCVideoSegmentation, SeCModelLoader, ImageBlend, easy showAnything, VHS_VideoCombine, VHS_LoadVideo, easy int, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, MarkdownNote, 孤海注释, PreviewImage, VHS_VideoCombine]
patterns: []
missing: [Evaluate Integers, Evaluate Integers, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, easy int, easy int, easy int, easy int]
discoveries: [次要节点 `Evaluate Integers` 知识库中没有该节点类型的任何知识, 次要节点 `Evaluate Integers` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageMaskScaleAsV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2053692073865433089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2-AnimateKJ版_v2版：人物替换（长视频版）_2053692073865433089.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
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
- `LoadImage`
- `VHS_VideoCombine`
- `MarkdownNote`
- `孤海注释`
- `PreviewImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **70%**（35/50）

**有卡**：`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`VHS_VideoCombine`、`ImageConcatMulti`、`ClothesSegment`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`SeCModelLoader`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`

**缺卡**（8）：`Evaluate Integers`、`Evaluate Integers`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`easy int`、`easy int`、`easy int`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `Evaluate Integers` 知识库中没有该节点类型的任何知识
- 次要节点 `Evaluate Integers` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageMaskScaleAsV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
