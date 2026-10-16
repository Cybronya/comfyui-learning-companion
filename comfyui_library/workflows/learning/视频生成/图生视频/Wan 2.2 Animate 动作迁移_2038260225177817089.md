---
key: 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2038260225177817089.json
name: Wan 2.2 Animate 动作迁移_2038260225177817089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038260225177817089.json
hash: 30ab303465599c10
coverage: 0.52381
learned_at: 2026-10-15 22:36:01
nodes: [GetNode, GetNode, BatchCount+, ImageBatch, RepeatImageBatch, easy mathInt, easy mathInt, easy mathInt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, easy mathInt, SetNode, easy mathInt, ImageFromBatch, GetNode, SetNode, easy convertAnything, SetNode, SimpleMath+, VHS_VideoInfo, SetNode, SetNode, ImageResizeKJv2, Seed (rgthree), GetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoTextEncodeCached, GetNode, SetNode, SetNode, ImageFromBatch, WanVideoContextOptions, WanVideoAnimateEmbeds, GetNode, WanVideoDecode, SetNode, GetNode, PoseAndFaceDetection, DrawViTPose, SetNode, BatchCount+, OnnxDetectionModelLoader, PurgeVRAM_UTK, PurgeVRAM_UTK, PurgeVRAM_UTK, SetNode, SetNode, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelectMulti, ImpactInt, easy int, easy int, easy int, VHS_LoadVideo, LoadImage, CR Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2038260225177817089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038260225177817089.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（84 个）：
- `GetNode`
- `GetNode`
- `BatchCount+`
- `ImageBatch`
- `RepeatImageBatch`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `SetNode`
- `easy mathInt`
- `ImageFromBatch`
- `GetNode`
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `Seed (rgthree)`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `BatchCount+`
- `OnnxDetectionModelLoader`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `ImpactInt`
- `easy int`
- `easy int`
- `easy int`
- `VHS_LoadVideo`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **52%**（44/84）

**有卡**：`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`easy mathInt`、`ImageFromBatch`、`easy convertAnything`、`SimpleMath+`、`VHS_VideoInfo`、`ImageResizeKJv2`、`Seed (rgthree)`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`PoseAndFaceDetection`、`DrawViTPose`、`OnnxDetectionModelLoader`、`PurgeVRAM_UTK`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`ImpactInt`、`easy int`、`VHS_LoadVideo`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
