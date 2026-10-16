---
key: 视频生成/图生视频/Wan2.2 FUN 控制模型 视频姿态动作迁移_1957318001500549121.json
name: Wan2.2 FUN 控制模型 视频姿态动作迁移_1957318001500549121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957318001500549121.json
hash: a9e57b8818fd8729
coverage: 0.467532
learned_at: 2026-10-15 22:31:16
nodes: [WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoLoraSelectMulti, GetNode, SetNode, SetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoImageToVideoEncode, GetNode, ImageResizeKJv2, WanVideoEncode, SetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, PrimitiveNode, PrimitiveNode, GetNode, GetNode, GetNode, WanVideoSampler, SetNode, WanVideoDecode, SetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoSampler, ImageResizeKJv2, SetNode, SetNode, ImpactInt, SetNode, ImpactInt, Note, Note, Note, Note, WanVideoControlEmbeds, ImpactInt, LoadImage, GetNode, GetImageSizeAndCount, SetNode, Note, ImpactInt, SetNode, GetNode, ImageConcatMulti, GetNode, SetNode, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, LoadImage, SimpleMath+, SetNode, SetNode, ImpactInt, Note, CR Text, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 FUN 控制模型 视频姿态动作迁移_1957318001500549121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957318001500549121.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（77 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoDecode`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `ImpactInt`
- `SetNode`
- `ImpactInt`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoControlEmbeds`
- `ImpactInt`
- `LoadImage`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `Note`
- `ImpactInt`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `ImpactInt`
- `Note`
- `CR Text`
- `RHHiddenNodes`

## 知识

覆盖率 **47%**（36/77）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`ImpactInt`、`WanVideoControlEmbeds`、`LoadImage`、`GetImageSizeAndCount`、`ImageConcatMulti`、`VHS_LoadVideo`、`VHS_VideoCombine`、`CR Text`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncode
