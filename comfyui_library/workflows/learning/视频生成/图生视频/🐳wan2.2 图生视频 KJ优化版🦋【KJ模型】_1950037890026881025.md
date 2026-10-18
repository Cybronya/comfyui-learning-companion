---
key: 视频生成/图生视频/🐳wan2.2 图生视频 KJ优化版🦋【KJ模型】_1950037890026881025.json
name: 🐳wan2.2 图生视频 KJ优化版🦋【KJ模型】_1950037890026881025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🐳wan2.2 图生视频 KJ优化版🦋【KJ模型】_1950037890026881025.json
hash: 56971a0c38647bae
coverage: 0.967742
learned_at: 2026-10-15 22:30:52
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, ImpactInt, ImpactInt, ImpactInt, ImageResizeKJv2, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, MarkdownNote, Note Plus (mtb), WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, SimpleMath+, INTConstant, INTConstant, WanVideoTextEncode, LoadImage, CR Text, VHS_VideoCombine, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/🐳wan2.2 图生视频 KJ优化版🦋【KJ模型】_1950037890026881025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950037890026881025.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImageResizeKJv2`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `MarkdownNote`
- `Note Plus (mtb)`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`ImpactInt`、`ImageResizeKJv2`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`Note Plus (mtb)`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`SimpleMath+`、`INTConstant`、`WanVideoTextEncode`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
