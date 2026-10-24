---
key: 图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json
name: 🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json
hash: 125726da010eed4f
coverage: 0.967742
learned_at: 2026-10-23 13:39:19
nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, WanVideoTextEncode, ImageResizeKJv2, WanVideoContextOptions, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoDecode, INTConstant, INTConstant, ImpactInt, ImpactInt, WanVideoSetBlockSwap, SimpleMath+, ImpactInt, WanVideoModelLoader, CR Text, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, VHS_VideoCombine, Note Plus (mtb), MarkdownNote, LoadImage, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoContextOptions`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `INTConstant`
- `INTConstant`
- `ImpactInt`
- `ImpactInt`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `ImpactInt`
- `WanVideoModelLoader`
- `CR Text`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `MarkdownNote`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`CreateCFGScheduleFloatList`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoContextOptions`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`INTConstant`、`ImpactInt`、`WanVideoSetBlockSwap`、`SimpleMath+`、`WanVideoModelLoader`、`CR Text`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImage`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
