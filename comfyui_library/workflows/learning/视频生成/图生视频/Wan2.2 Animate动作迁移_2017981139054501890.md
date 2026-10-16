---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移_2017981139054501890.json
name: Wan2.2 Animate动作迁移_2017981139054501890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017981139054501890.json
hash: c35ae1097a192722
coverage: 0.493506
learned_at: 2026-10-15 22:34:51
nodes: [GetNode, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, OnnxDetectionModelLoader, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, SetNode, easy mathInt, VHS_VideoInfo, SetNode, GetNode, PoseAndFaceDetection, easy cleanGpuUsed, easy cleanGpuUsed, ImageResizeKJv2, DrawViTPose, RepeatImageBatch, BatchCount+, GetNode, ImageBatch, SetNode, ImageFromBatch, easy cleanGpuUsed, WanVideoVAELoader, SetNode, SetNode, SetNode, PreviewImage, GetNode, GetNode, GetNode, WanVideoSampler, easy cleanGpuUsed, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoBlockSwap, Note, VHS_VideoCombine, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoTextEncodeCached, Int, Int, VRAMReserver, Int, BatchCount+, RHHiddenNodes, Note, VHS_LoadVideo, LoadImage, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移_2017981139054501890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017981139054501890.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `VHS_VideoInfo`
- `SetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `DrawViTPose`
- `RepeatImageBatch`
- `BatchCount+`
- `GetNode`
- `ImageBatch`
- `SetNode`
- `ImageFromBatch`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `Note`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `Int`
- `Int`
- `VRAMReserver`
- `Int`
- `BatchCount+`
- `RHHiddenNodes`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `Int`

## 知识

覆盖率 **49%**（38/77）

**有卡**：`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`easy mathInt`、`VHS_VideoInfo`、`PoseAndFaceDetection`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`DrawViTPose`、`RepeatImageBatch`、`BatchCount+`、`ImageBatch`、`ImageFromBatch`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoContextOptions`、`WanVideoDecode`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`Int`、`VRAMReserver`、`RHHiddenNodes`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
