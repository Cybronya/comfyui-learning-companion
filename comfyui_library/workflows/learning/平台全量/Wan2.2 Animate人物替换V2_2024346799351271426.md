---
key: 平台全量/Wan2.2 Animate人物替换V2_2024346799351271426.json
name: Wan2.2 Animate人物替换V2_2024346799351271426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate人物替换V2_2024346799351271426.json
hash: 2a14606360e35770
coverage: 0.428571
learned_at: 2026-11-14 01:05:09
nodes: [CLIPVisionLoader, GetNode, SetNode, SetNode, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, GetNode, SetNode, ImageFromBatch, SetNode, SetNode, SetNode, GetNode, RepeatImageBatch, easy mathInt, easy mathInt, GetNode, easy mathInt, easy compare, LazySwitch1way, SetNode, SetNode, GetNode, SetNode, SetNode, easy compare, GetNode, SetNode, easy mathInt, GetNode, GetNode, ImageFromBatch, easy mathInt, LazySwitch1way, GetNode, GetNode, GetNode, RepeatImageBatch, GetNode, BatchCount+, SeCModelLoader, GetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, VHS_VideoInfoLoaded, SetNode, PreviewImage, BatchCount+, easy mathInt, ImageBatch, easy mathInt, BatchCount+, ImageResizeKJv2, SetNode, WanVideoSetLoRAs, GetNode, GetNode, Image Blank, GetNode, GetNode, OnnxDetectionModelLoader, LayerUtility: ImageBlend, DrawViTPose, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, WanVideoSampler, GetNode, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoVAELoader, Note, Note, Note, Note, Note, Note, SeCVideoSegmentation, VHS_VideoCombine, SetNode, SetNode, GetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, VHS_VideoCombine, easy int, SetNode, WanVideoTextEncodeCached, easy int, BlockifyMask, WanVideoLoraSelectMulti, RHHiddenNodes, WanVideoModelLoader, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, VHS_VideoCombine, Note, WanVideoBlockSwap, WanVideoDecode, easy int, easy int, PreviewImage, GrowMask, easy int, VHS_LoadVideo, LoadImage, PointsEditor, Bookmark (rgthree)]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate人物替换V2_2024346799351271426.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate人物替换V2_2024346799351271426.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（140 个）：
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageFromBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `RepeatImageBatch`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `easy mathInt`
- `easy compare`
- `LazySwitch1way`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy compare`
- `GetNode`
- `SetNode`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `easy mathInt`
- `LazySwitch1way`
- `GetNode`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `GetNode`
- `BatchCount+`
- `SeCModelLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `PreviewImage`
- `BatchCount+`
- `easy mathInt`
- `ImageBatch`
- `easy mathInt`
- `BatchCount+`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `Image Blank`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `LayerUtility: ImageBlend`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy int`
- `SetNode`
- `WanVideoTextEncodeCached`
- `easy int`
- `BlockifyMask`
- `WanVideoLoraSelectMulti`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `easy int`
- `easy int`
- `PreviewImage`
- `GrowMask`
- `easy int`
- `VHS_LoadVideo`
- `LoadImage`
- `PointsEditor`
- `Bookmark (rgthree)`

## 知识

覆盖率 **43%**（60/140）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageFromBatch`、`RepeatImageBatch`、`easy mathInt`、`easy compare`、`LazySwitch1way`、`BatchCount+`、`SeCModelLoader`、`VHS_VideoInfo`、`VHS_VideoInfoLoaded`、`ImageBatch`、`ImageResizeKJv2`、`WanVideoSetLoRAs`、`Image Blank`、`OnnxDetectionModelLoader`、`LayerUtility: ImageBlend`、`DrawViTPose`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`easy int`、`WanVideoTextEncodeCached`、`BlockifyMask`、`WanVideoLoraSelectMulti`、`RHHiddenNodes`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoDecode`、`GrowMask`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`、`Bookmark (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
