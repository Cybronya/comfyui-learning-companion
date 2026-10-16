---
key: 视频生成/文生视频/通义万相wan2.2视频转绘视频人物替换视频换脸V1.0_1957329600441413634.json
name: 通义万相wan2.2视频转绘视频人物替换视频换脸V1.0_1957329600441413634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1957329600441413634.json
hash: 790f37bdd807680c
coverage: 0.891304
learned_at: 2026-10-15 22:43:41
nodes: [WanVideoModelLoader, PrimitiveNode, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoModelLoader, SetNode, WanVideoTextEncode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, ImpactInt, ImpactInt, ImageResizeKJv2, SimpleMath+, ImageBlend, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, ImageConcatMulti, ImpactInt, PrimitiveNode, SimpleMath+, WanVideoSampler, VHS_LoadVideo, Note, LoadWanVideoT5TextEncoder, WanVideoDecode, ImpactInt, LoadImage, CR Text, ImageConcatMulti, VHS_VideoCombine, ImpactInt, WanVideoSampler, ImageResizeKJv2, AIO_Preprocessor, easy anythingIndexSwitch, WanVideoEncode, GetImageSizeAndCount, WanVideoControlEmbeds, WanVideoImageToVideoEncode, Reroute, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/通义万相wan2.2视频转绘视频人物替换视频换脸V1.0_1957329600441413634.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1957329600441413634.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `WanVideoModelLoader`
- `PrimitiveNode`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `ImpactInt`
- `ImpactInt`
- `ImageResizeKJv2`
- `SimpleMath+`
- `ImageBlend`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `ImageConcatMulti`
- `ImpactInt`
- `PrimitiveNode`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `ImpactInt`
- `LoadImage`
- `CR Text`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImpactInt`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `AIO_Preprocessor`
- `easy anythingIndexSwitch`
- `WanVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoControlEmbeds`
- `WanVideoImageToVideoEncode`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoVAELoader`、`ImpactInt`、`ImageResizeKJv2`、`SimpleMath+`、`ImageBlend`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`ImageConcatMulti`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`LoadImage`、`CR Text`、`VHS_VideoCombine`、`AIO_Preprocessor`、`easy anythingIndexSwitch`、`WanVideoEncode`、`GetImageSizeAndCount`、`WanVideoControlEmbeds`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
