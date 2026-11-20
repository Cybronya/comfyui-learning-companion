---
key: 平台全量/wan2.1首尾帧官方稳定版720p_1915278424968204289.json
name: wan2.1首尾帧官方稳定版720p_1915278424968204289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1首尾帧官方稳定版720p_1915278424968204289.json
hash: a5d6c6eba24dc5ae
coverage: 0.763158
learned_at: 2026-11-14 01:19:15
nodes: [GetNode, WanVideoBlockSwap, SetNode, SetNode, GetNode, ImageResize+, WanVideoExperimentalArgs, Note, WanVideoVRAMManagement, WanVideoClipVisionEncode, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSampler, ImageConcatMulti, Note, WanVideoModelLoader, WanVideoTextEncode, WanVideoTorchCompileSettings, ImageConcatMulti, WanVideoSLG, WanVideoTeaCache, WanVideoImageToVideoEncode, Note, Note, AddLabel, AddLabel, ImageResize+, easy int, Note, WanVideoDecode, GetImageSizeAndCount, LoadImage, CR Text, LoadImage, EmptyImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/wan2.1首尾帧官方稳定版720p_1915278424968204289.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1首尾帧官方稳定版720p_1915278424968204289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（38 个）：
- `GetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResize+`
- `WanVideoExperimentalArgs`
- `Note`
- `WanVideoVRAMManagement`
- `WanVideoClipVisionEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `ImageConcatMulti`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoImageToVideoEncode`
- `Note`
- `Note`
- `AddLabel`
- `AddLabel`
- `ImageResize+`
- `easy int`
- `Note`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `EmptyImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **76%**（29/38）

**有卡**：`WanVideoBlockSwap`、`ImageResize+`、`WanVideoExperimentalArgs`、`WanVideoVRAMManagement`、`WanVideoClipVisionEncode`、`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSampler`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoImageToVideoEncode`、`AddLabel`、`easy int`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadImage`、`CR Text`、`EmptyImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode
