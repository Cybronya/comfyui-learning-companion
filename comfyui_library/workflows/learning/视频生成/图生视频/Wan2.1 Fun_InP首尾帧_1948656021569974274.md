---
key: 视频生成/图生视频/Wan2.1 Fun_InP首尾帧_1948656021569974274.json
name: Wan2.1 Fun_InP首尾帧_1948656021569974274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 Fun_InP首尾帧_1948656021569974274.json
hash: a68ad41d9af66232
coverage: 0.642857
learned_at: 2026-10-15 22:30:47
nodes: [ImageScale, ImageScale, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, SetNode, GetNode, GetNode, WanVideoBlockSwap, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LoadWanVideoT5TextEncoder, SetNode, easy int, SetNode, easy int, easy int, SetNode, SetNode, easy positive, Note, LoadImage, LoadImage, WanVideoModelLoader, easy seed, WanVideoImageToVideoEncode, SetNode, Note Plus (mtb), LoadImageFromUrl, WanVideoDecode, VHS_VideoCombine, WanVideoTextEncode, WanVideoSampler, WanVideoEnhanceAVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 Fun_InP首尾帧_1948656021569974274.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948656021569974274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
- `ImageScale`
- `ImageScale`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `easy int`
- `SetNode`
- `easy int`
- `easy int`
- `SetNode`
- `SetNode`
- `easy positive`
- `Note`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `easy seed`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`

## 知识

覆盖率 **64%**（27/42）

**有卡**：`ImageScale`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`LoadWanVideoT5TextEncoder`、`easy int`、`easy positive`、`LoadImage`、`WanVideoModelLoader`、`easy seed`、`WanVideoImageToVideoEncode`、`Note Plus (mtb)`、`LoadImageFromUrl`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoEnhanceAVideo`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
