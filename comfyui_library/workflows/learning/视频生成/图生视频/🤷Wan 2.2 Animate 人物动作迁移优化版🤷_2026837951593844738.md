---
key: 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2026837951593844738.json
name: 🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2026837951593844738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2026837951593844738.json
hash: d21e81c314189a17
coverage: 0.523256
learned_at: 2026-10-15 22:35:14
nodes: [GetNode, GetNode, BatchCount+, ImageBatch, RepeatImageBatch, easy mathInt, easy mathInt, easy mathInt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy int, GetNode, SetNode, SetNode, SetNode, SetNode, easy mathInt, SetNode, easy mathInt, ImageFromBatch, GetNode, SetNode, easy convertAnything, SetNode, SimpleMath+, VHS_VideoInfo, SetNode, SetNode, easy int, ImageResizeKJv2, Seed (rgthree), GetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoTextEncodeCached, GetNode, SetNode, CR Text, SetNode, ImageFromBatch, VHS_VideoCombine, WanVideoContextOptions, WanVideoAnimateEmbeds, GetNode, WanVideoDecode, SetNode, GetNode, PoseAndFaceDetection, DrawViTPose, SetNode, BatchCount+, OnnxDetectionModelLoader, Note Plus (mtb), MarkdownNote, PurgeVRAM_UTK, PurgeVRAM_UTK, PurgeVRAM_UTK, SetNode, VHS_LoadVideo, ImpactInt, easy int, SetNode, LoadImage, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2026837951593844738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026837951593844738.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（86 个）：
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
- `easy int`
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
- `easy int`
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
- `CR Text`
- `SetNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
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
- `Note Plus (mtb)`
- `MarkdownNote`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `SetNode`
- `VHS_LoadVideo`
- `ImpactInt`
- `easy int`
- `SetNode`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **52%**（45/86）

**有卡**：`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`easy mathInt`、`easy int`、`ImageFromBatch`、`easy convertAnything`、`SimpleMath+`、`VHS_VideoInfo`、`ImageResizeKJv2`、`Seed (rgthree)`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`CR Text`、`VHS_VideoCombine`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`PoseAndFaceDetection`、`DrawViTPose`、`OnnxDetectionModelLoader`、`Note Plus (mtb)`、`PurgeVRAM_UTK`、`VHS_LoadVideo`、`ImpactInt`、`LoadImage`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
