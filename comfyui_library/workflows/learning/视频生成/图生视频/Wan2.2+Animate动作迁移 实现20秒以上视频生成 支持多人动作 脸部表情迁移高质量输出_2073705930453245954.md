---
key: 视频生成/图生视频/Wan2.2+Animate动作迁移 实现20秒以上视频生成 支持多人动作 脸部表情迁移高质量输出_2073705930453245954.json
name: Wan2.2+Animate动作迁移 实现20秒以上视频生成 支持多人动作 脸部表情迁移高质量输出_2073705930453245954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073705930453245954.json
hash: 789e485cfdbc0812
coverage: 0.542553
learned_at: 2026-10-15 22:41:09
nodes: [SetNode, easy mathInt, easy compare, easy mathInt, SetNode, easy mathInt, easy compare, ImageFromBatch, ImageBatch, RepeatImageBatch, RepeatImageBatch, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, BatchCount+, SetNode, easy mathInt, ImageBatch, easy mathInt, GetNode, LazySwitch1way, SetNode, WanVideoBlockSwap, WanVideoSetLoRAs, easy cleanGpuUsed, LazySwitch1way, BatchCount+, GetNode, WanVideoVAELoader, SetNode, easy mathInt, easy mathInt, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, Int, Int, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTeaCache, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, WanVideoTextEncodeCached, SetNode, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, RHHiddenNodes, WanVideoClipVisionEncode, WanVideoDecode, RHHiddenNodes, RHHiddenNodes, PreviewImage, ImageResizeKJv2, Int, WanVideoAnimateEmbeds, WanVideoSampler, SetNode, RHHiddenNodes, Int, GetNode, GetNode, ImageFromBatch, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2+Animate动作迁移 实现20秒以上视频生成 支持多人动作 脸部表情迁移高质量输出_2073705930453245954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073705930453245954.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（94 个）：
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
- `PreviewImage`
- `ImageResizeKJv2`
- `Int`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `SetNode`
- `RHHiddenNodes`
- `Int`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **54%**（51/94）

**有卡**：`easy mathInt`、`easy compare`、`ImageFromBatch`、`ImageBatch`、`RepeatImageBatch`、`BatchCount+`、`LazySwitch1way`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`Int`、`WanVideoTeaCache`、`WanVideoTextEncodeCached`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`RHHiddenNodes`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
