---
key: 视频生成/图生视频/AI知识分享宝库 _ 原生 视频人物替换 Animate 2.2_1977983075667824642.json
name: AI知识分享宝库 _ 原生 视频人物替换 Animate 2.2_1977983075667824642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI知识分享宝库 _ 原生 视频人物替换 Animate 2.2_1977983075667824642.json
hash: f963fc8ec7afdd7b
coverage: 0.517241
learned_at: 2026-10-15 22:32:17
nodes: [ImpactSwitch, Primitive integer [Crystools], SetNode, SetNode, ImageResizeKJv2, SetNode, Primitive integer [Crystools], WanVideoSetBlockSwap, SetNode, GetNode, WanVideoVAELoader, SetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, CLIPVisionLoader, SetNode, GetNode, GetNode, GetNode, ImpactSwitch, Primitive integer [Crystools], WanVideoTextEncodeCached, SetNode, WanVideoDecode, SetNode, LoadImage, WanVideoSampler, GetImageSizeAndCount, GetNode, GetNode, LoadImage, GetNode, VHS_VideoCombine, VHS_VideoCombine, Primitive integer [Crystools], VHS_LoadVideo, GetNode, SetNode, easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy showAnything, SetNode, SetNode, SetNode, VHS_VideoInfoSource, VHS_VideoCombine, WanVideoSetLoRAs, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, Primitive integer [Crystools], GetNode, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, Primitive integer [Crystools], JjkText, JjkText, SetNode, BlockifyMask, DrawMaskOnImage, SetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, DrawViTPose, GetNode, PoseAndFaceDetection, Sam2Segmentation, PrimitiveString, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/AI知识分享宝库 _ 原生 视频人物替换 Animate 2.2_1977983075667824642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977983075667824642.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（87 个）：
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `Primitive integer [Crystools]`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoDecode`
- `SetNode`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoSource`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `Primitive integer [Crystools]`
- `JjkText`
- `JjkText`
- `SetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `DrawViTPose`
- `GetNode`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `PrimitiveString`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 知识

覆盖率 **52%**（45/87）

**有卡**：`Primitive integer [Crystools]`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`LoadImage`、`WanVideoSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`VHS_LoadVideo`、`VHS_VideoInfoSource`、`WanVideoSetLoRAs`、`SimpleMath+`、`ImageConcatMulti`、`BlockifyMask`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`DrawViTPose`、`PoseAndFaceDetection`、`Sam2Segmentation`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
