---
key: 平台全量/【大炮视频】wan2.1最新官方稳定首尾帧_1914979282009976834.json
name: 【大炮视频】wan2.1最新官方稳定首尾帧_1914979282009976834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【大炮视频】wan2.1最新官方稳定首尾帧_1914979282009976834.json
hash: 4e696e44b52cc35e
coverage: 0.714286
learned_at: 2026-11-14 01:23:51
nodes: [WanVideoVRAMManagement, LoadWanVideoT5TextEncoder, GetNode, AddLabel, AddLabel, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, Note, ImageResize+, Note, Note, Note, MarkdownNote, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoBlockSwap, SetNode, SetNode, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTextEncode, CR Text, Note, Note, WanVideoSampler, GetNode, EmptyImage, ImageConcatMulti, ImageResize+, Note Plus (mtb), Note, Note Plus (mtb), VHS_VideoCombine, LoadImage, LoadImage, WanVideoTorchCompileSettings, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/【大炮视频】wan2.1最新官方稳定首尾帧_1914979282009976834.json

> 来源文件 `comfyui_library/workflows/平台全量/【大炮视频】wan2.1最新官方稳定首尾帧_1914979282009976834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoVRAMManagement`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `Note`
- `ImageResize+`
- `Note`
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTextEncode`
- `CR Text`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `GetNode`
- `EmptyImage`
- `ImageConcatMulti`
- `ImageResize+`
- `Note Plus (mtb)`
- `Note`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **71%**（30/42）

**有卡**：`WanVideoVRAMManagement`、`LoadWanVideoT5TextEncoder`、`AddLabel`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageResize+`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`CR Text`、`WanVideoSampler`、`EmptyImage`、`Note Plus (mtb)`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode
