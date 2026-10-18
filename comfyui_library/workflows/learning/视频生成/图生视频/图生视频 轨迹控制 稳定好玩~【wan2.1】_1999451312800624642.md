---
key: 视频生成/图生视频/图生视频 轨迹控制 稳定好玩~【wan2.1】_1999451312800624642.json
name: 图生视频 轨迹控制 稳定好玩~【wan2.1】_1999451312800624642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 轨迹控制 稳定好玩~【wan2.1】_1999451312800624642.json
hash: ef3fb17c10a7ddf2
coverage: 0.878788
learned_at: 2026-10-15 22:33:37
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetLoRAs, ImpactInt, MarkdownNote, WanVideoSetBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, easy showAnything, MarkdownNote, CLIPVisionLoader, RepeatImageBatch, WanVideoAddWanMoveTracks, WanVideoWanDrawWanMoveTracks, VHS_VideoCombine, WanVideoDecode, WanVideoWanDrawWanMoveTracks, WanVideoImageToVideoEncode, ImageResizeKJv2, WanVideoClipVisionEncode, SimpleMath+, VHS_VideoCombine, VHS_VideoCombine, SplineEditor, CR Text, WanVideoSampler, MarkdownNote, Note Plus (mtb), ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频 轨迹控制 稳定好玩~【wan2.1】_1999451312800624642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999451312800624642.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `ImpactInt`
- `MarkdownNote`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `easy showAnything`
- `MarkdownNote`
- `CLIPVisionLoader`
- `RepeatImageBatch`
- `WanVideoAddWanMoveTracks`
- `WanVideoWanDrawWanMoveTracks`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoWanDrawWanMoveTracks`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SplineEditor`
- `CR Text`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `Note Plus (mtb)`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `WanVideoLoraSelect`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`ImpactInt`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CLIPVisionLoader`、`RepeatImageBatch`、`WanVideoAddWanMoveTracks`、`WanVideoWanDrawWanMoveTracks`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`SimpleMath+`、`SplineEditor`、`CR Text`、`WanVideoSampler`、`Note Plus (mtb)`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
