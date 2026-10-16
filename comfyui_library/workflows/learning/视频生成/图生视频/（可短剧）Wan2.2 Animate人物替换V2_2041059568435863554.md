---
key: 视频生成/图生视频/（可短剧）Wan2.2 Animate人物替换V2_2041059568435863554.json
name: （可短剧）Wan2.2 Animate人物替换V2_2041059568435863554.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041059568435863554.json
hash: e32c7caadd3b245c
coverage: 0.432624
learned_at: 2026-10-15 22:36:17
nodes: [CLIPVisionLoader, GetNode, SetNode, SetNode, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, GetNode, SetNode, ImageFromBatch, SetNode, SetNode, SetNode, GetNode, RepeatImageBatch, easy mathInt, easy mathInt, GetNode, easy mathInt, easy compare, LazySwitch1way, SetNode, SetNode, GetNode, SetNode, SetNode, easy compare, GetNode, SetNode, easy mathInt, GetNode, GetNode, ImageFromBatch, easy mathInt, LazySwitch1way, GetNode, GetNode, GetNode, RepeatImageBatch, GetNode, BatchCount+, SeCModelLoader, GetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, VHS_VideoInfoLoaded, SetNode, BatchCount+, easy mathInt, ImageBatch, easy mathInt, BatchCount+, ImageResizeKJv2, SetNode, WanVideoSetLoRAs, GetNode, GetNode, Image Blank, GetNode, GetNode, OnnxDetectionModelLoader, LayerUtility: ImageBlend, DrawViTPose, PoseAndFaceDetection, SetNode, SetNode, SetNode, Bookmark (rgthree), SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoVAELoader, Note, Note, Note, Note, Note, Note, SeCVideoSegmentation, VHS_VideoCombine, SetNode, SetNode, GetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, VHS_VideoCombine, SetNode, WanVideoTextEncodeCached, easy int, GrowMask, BlockifyMask, RHHiddenNodes, WanVideoModelLoader, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, WanVideoDecode, LoadImage, easy int, PreviewImage, Note, VHS_VideoCombine, VHS_LoadVideo, WanVideoBlockSwap, easy int, WanVideoLoraSelectMulti, WanVideoLoraSelect, WanVideoSampler, easy int, easy int, PreviewImage, PointsEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/（可短剧）Wan2.2 Animate人物替换V2_2041059568435863554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041059568435863554.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（141 个）：
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
- `Bookmark (rgthree)`
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
- `SetNode`
- `WanVideoTextEncodeCached`
- `easy int`
- `GrowMask`
- `BlockifyMask`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `WanVideoDecode`
- `LoadImage`
- `easy int`
- `PreviewImage`
- `Note`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `easy int`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `easy int`
- `easy int`
- `PreviewImage`
- `PointsEditor`

## 知识

覆盖率 **43%**（61/141）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageFromBatch`、`RepeatImageBatch`、`easy mathInt`、`easy compare`、`LazySwitch1way`、`BatchCount+`、`SeCModelLoader`、`VHS_VideoInfo`、`VHS_VideoInfoLoaded`、`ImageBatch`、`ImageResizeKJv2`、`WanVideoSetLoRAs`、`Image Blank`、`OnnxDetectionModelLoader`、`LayerUtility: ImageBlend`、`DrawViTPose`、`PoseAndFaceDetection`、`Bookmark (rgthree)`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`WanVideoTextEncodeCached`、`easy int`、`GrowMask`、`BlockifyMask`、`RHHiddenNodes`、`WanVideoModelLoader`、`WanVideoDecode`、`LoadImage`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoLoraSelect`、`WanVideoSampler`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
