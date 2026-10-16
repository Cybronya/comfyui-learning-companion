---
key: 视频生成/图生视频/wan2.1首尾帧视频_1930189801167732738.json
name: wan2.1首尾帧视频_1930189801167732738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1930189801167732738.json
hash: 5bce62f9bfce13dc
coverage: 0.931034
learned_at: 2026-10-15 22:30:03
nodes: [SetNode, LoadImage, LoadImage, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSLG, WanVideoTeaCache, SetNode, WanVideoTextEncode, Int, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, ImageResize+, ImageResize+, WanVideoImageToVideoEncode, WanVideoExperimentalArgs, WanVideoClipVisionEncode, WanVideoEnhanceAVideo, easy cleanGpuUsed, WanVideoSampler, RIFE VFI, WanVideoDecode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, VHS_VideoCombine, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1首尾帧视频_1930189801167732738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930189801167732738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（29 个）：
- `SetNode`
- `LoadImage`
- `LoadImage`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `SetNode`
- `WanVideoTextEncode`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `ImageResize+`
- `ImageResize+`
- `WanVideoImageToVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoClipVisionEncode`
- `WanVideoEnhanceAVideo`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `RIFE VFI`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `Text Multiline`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`LoadImage`、`Primitive integer [Crystools]`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoTextEncode`、`Int`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`ImageResize+`、`WanVideoImageToVideoEncode`、`WanVideoExperimentalArgs`、`WanVideoClipVisionEncode`、`WanVideoEnhanceAVideo`、`easy cleanGpuUsed`、`WanVideoSampler`、`RIFE VFI`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
