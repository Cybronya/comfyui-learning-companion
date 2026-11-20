---
key: 平台全量/Animate动作迁移高清全能V3版(WAN 2.2)-极致真人表情舞蹈动作模仿复刻天花板 人物场景_2075174251463794690.json
name: Animate动作迁移高清全能V3版(WAN 2.2)-极致真人表情舞蹈动作模仿复刻天花板 人物场景_2075174251463794690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Animate动作迁移高清全能V3版(WAN 2.2)-极致真人表情舞蹈动作模仿复刻天花板 人物场景_2075174251463794690.json
hash: 35c9721e5388755d
coverage: 0.396396
learned_at: 2026-11-14 00:18:53
nodes: [GetNode, GetNode, SetNode, WanVideoLoraSelectMulti, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, PurgeVRAM_UTK, GetNode, GetNode, ImageFromBatch, SetNode, WanVideoDecode, SetNode, GetNode, Seed, PurgeVRAM_UTK, GetNode, WanVideoSampler, SetNode, WanVideoAnimateEmbeds, GetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, GetNode, PoseAndFaceDetection, DrawViTPose, PurgeVRAM_UTK, SetNode, SetNode, easy mathInt, easy mathInt, easy mathInt, easy mathInt, BatchCount+, ImageFromBatch, easy mathInt, ImageBatch, RepeatImageBatch, BatchCount+, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, WanVideoContextOptions, SetNode, WanVideoTextEncodeCached, WanVideoVAELoader, SetNode, WanVideoLoraSelect, OnnxDetectionModelLoader, WanVideoModelLoader, SetNode, SimpleMath+, easy convertAnything, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, WanVideoClipVisionEncode, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, easy int, easy int, ImpactInt, easy int, SetNode, SetNode, VHS_VideoCombine, VHS_LoadVideo, LoadImage, CR Text]
patterns: []
missing: []
---

# 平台全量/Animate动作迁移高清全能V3版(WAN 2.2)-极致真人表情舞蹈动作模仿复刻天花板 人物场景_2075174251463794690.json

> 来源文件 `comfyui_library/workflows/平台全量/Animate动作迁移高清全能V3版(WAN 2.2)-极致真人表情舞蹈动作模仿复刻天花板 人物场景_2075174251463794690.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（111 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PurgeVRAM_UTK`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `SetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `Seed`
- `PurgeVRAM_UTK`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `PurgeVRAM_UTK`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `BatchCount+`
- `ImageFromBatch`
- `easy mathInt`
- `ImageBatch`
- `RepeatImageBatch`
- `BatchCount+`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelect`
- `OnnxDetectionModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `SimpleMath+`
- `easy convertAnything`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `easy int`
- `easy int`
- `ImpactInt`
- `easy int`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **40%**（44/111）

**有卡**：`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`PurgeVRAM_UTK`、`ImageFromBatch`、`WanVideoDecode`、`Seed`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`VHS_VideoInfo`、`PoseAndFaceDetection`、`DrawViTPose`、`easy mathInt`、`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`OnnxDetectionModelLoader`、`WanVideoModelLoader`、`SimpleMath+`、`easy convertAnything`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`easy int`、`ImpactInt`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、Seed、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect
