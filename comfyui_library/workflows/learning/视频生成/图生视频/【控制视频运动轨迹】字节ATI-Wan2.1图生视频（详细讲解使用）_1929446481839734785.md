---
key: 视频生成/图生视频/【控制视频运动轨迹】字节ATI-Wan2.1图生视频（详细讲解使用）_1929446481839734785.json
name: 【控制视频运动轨迹】字节ATI-Wan2.1图生视频（详细讲解使用）_1929446481839734785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【控制视频运动轨迹】字节ATI-Wan2.1图生视频（详细讲解使用）_1929446481839734785.json
hash: d3324f47ba934fc8
coverage: 0.481481
learned_at: 2026-10-15 22:30:00
nodes: [LoadAndResizeImage, SetNode, SetNode, SetNode, Anything Everywhere, CLIPVisionLoader, WanVideoVAELoader, Anything Everywhere, LoadWanVideoT5TextEncoder, Anything Everywhere, Anything Everywhere, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoDecode, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, GetNode, AppendStringsToList, GetNode, GetNode, AppendStringsToList, VHS_VideoCombine, WanVideoATITracks, WanVideoSampler, GetNode, GetNode, SplineEditor, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SplineEditor, WanVideoImageToVideoEncode, GetNode, Int, SplineEditor, GetNode, GetNode, CreateShapeImageOnPath, VHS_VideoCombine, Note, Note, WanVideoTextEncode, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/【控制视频运动轨迹】字节ATI-Wan2.1图生视频（详细讲解使用）_1929446481839734785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1929446481839734785.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（54 个）：
- `LoadAndResizeImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetNode`
- `AppendStringsToList`
- `GetNode`
- `GetNode`
- `AppendStringsToList`
- `VHS_VideoCombine`
- `WanVideoATITracks`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `SplineEditor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SplineEditor`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `Int`
- `SplineEditor`
- `GetNode`
- `GetNode`
- `CreateShapeImageOnPath`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `Note`
- `Note`

## 知识

覆盖率 **48%**（26/54）

**有卡**：`LoadAndResizeImage`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`AppendStringsToList`、`VHS_VideoCombine`、`WanVideoATITracks`、`WanVideoSampler`、`SplineEditor`、`WanVideoImageToVideoEncode`、`Int`、`CreateShapeImageOnPath`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoLoraSelect
