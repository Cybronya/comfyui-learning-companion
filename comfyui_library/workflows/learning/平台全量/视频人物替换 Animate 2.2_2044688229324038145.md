---
key: 平台全量/视频人物替换 Animate 2.2_2044688229324038145.json
name: 视频人物替换 Animate 2.2_2044688229324038145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频人物替换 Animate 2.2_2044688229324038145.json
hash: dd0ef6e1f1a7f1e1
coverage: 0.5125
learned_at: 2026-11-14 02:35:11
nodes: [ImpactSwitch, Primitive integer [Crystools], SetNode, SetNode, ImageResizeKJv2, SetNode, Primitive integer [Crystools], WanVideoSetBlockSwap, SetNode, GetNode, WanVideoVAELoader, SetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, CLIPVisionLoader, SetNode, GetNode, GetNode, GetNode, ImpactSwitch, Primitive integer [Crystools], WanVideoTextEncodeCached, SetNode, WanVideoDecode, SetNode, WanVideoSampler, GetImageSizeAndCount, GetNode, GetNode, LoadImage, GetNode, VHS_VideoCombine, VHS_VideoCombine, Primitive integer [Crystools], VHS_LoadVideo, GetNode, SetNode, easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy showAnything, SetNode, SetNode, SetNode, VHS_VideoInfoSource, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, WanVideoSetLoRAs, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, Primitive integer [Crystools], RHHiddenNodes, Primitive integer [Crystools], JjkText, JjkText, SetNode, BlockifyMask, DrawMaskOnImage, SetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, RHHiddenNodes, DrawViTPose, GetNode, PoseAndFaceDetection, Sam2Segmentation, PrimitiveString, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
---

# 平台全量/视频人物替换 Animate 2.2_2044688229324038145.json

> 来源文件 `comfyui_library/workflows/平台全量/视频人物替换 Animate 2.2_2044688229324038145.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（80 个）：
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
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
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
- `RHHiddenNodes`
- `DrawViTPose`
- `GetNode`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `PrimitiveString`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 知识

覆盖率 **51%**（41/80）

**有卡**：`Primitive integer [Crystools]`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`WanVideoSampler`、`GetImageSizeAndCount`、`LoadImage`、`VHS_VideoCombine`、`VHS_LoadVideo`、`VHS_VideoInfoSource`、`RHHiddenNodes`、`WanVideoSetLoRAs`、`SimpleMath+`、`BlockifyMask`、`DrawMaskOnImage`、`easy cleanGpuUsed`、`DrawViTPose`、`PoseAndFaceDetection`、`Sam2Segmentation`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
