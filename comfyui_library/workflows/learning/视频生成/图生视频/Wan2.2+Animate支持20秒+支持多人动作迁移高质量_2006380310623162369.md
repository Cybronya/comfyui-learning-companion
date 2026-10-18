---
key: 视频生成/图生视频/Wan2.2+Animate支持20秒+支持多人动作迁移高质量_2006380310623162369.json
name: Wan2.2+Animate支持20秒+支持多人动作迁移高质量_2006380310623162369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Animate支持20秒+支持多人动作迁移高质量_2006380310623162369.json
hash: 452ff1e923d3413e
coverage: 0.541667
learned_at: 2026-10-15 22:34:01
nodes: [SetNode, easy mathInt, easy compare, easy mathInt, SetNode, easy mathInt, easy compare, ImageFromBatch, ImageBatch, RepeatImageBatch, RepeatImageBatch, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, BatchCount+, SetNode, easy mathInt, ImageBatch, easy mathInt, GetNode, LazySwitch1way, SetNode, WanVideoBlockSwap, WanVideoSetLoRAs, easy cleanGpuUsed, LazySwitch1way, BatchCount+, GetNode, WanVideoVAELoader, SetNode, easy mathInt, easy mathInt, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, Int, Int, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTeaCache, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, WanVideoTextEncodeCached, SetNode, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, RHHiddenNodes, WanVideoClipVisionEncode, WanVideoDecode, RHHiddenNodes, RHHiddenNodes, VHS_LoadVideo, LoadImage, PreviewImage, ImageResizeKJv2, Int, WanVideoAnimateEmbeds, WanVideoSampler, SetNode, RHHiddenNodes, Note, Int, GetNode, GetNode, ImageFromBatch, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2+Animate支持20秒+支持多人动作迁移高质量_2006380310623162369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006380310623162369.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（96 个）：
- `SetNode`
- `easy mathInt`
- `easy compare`
- `easy mathInt`
- `SetNode`
- `easy mathInt`
- `easy compare`
- `ImageFromBatch`
- `ImageBatch`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `easy mathInt`
- `ImageBatch`
- `easy mathInt`
- `GetNode`
- `LazySwitch1way`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `LazySwitch1way`
- `BatchCount+`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `easy mathInt`
- `easy mathInt`
- `WanVideoSetBlockSwap`
- `SetNode`
- `CLIPVisionLoader`
- `Int`
- `Int`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTeaCache`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RHHiddenNodes`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `VHS_LoadVideo`
- `LoadImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `Int`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `SetNode`
- `RHHiddenNodes`
- `Note`
- `Int`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **54%**（52/96）

**有卡**：`easy mathInt`、`easy compare`、`ImageFromBatch`、`ImageBatch`、`RepeatImageBatch`、`BatchCount+`、`LazySwitch1way`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`Int`、`WanVideoTeaCache`、`WanVideoTextEncodeCached`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`RHHiddenNodes`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
