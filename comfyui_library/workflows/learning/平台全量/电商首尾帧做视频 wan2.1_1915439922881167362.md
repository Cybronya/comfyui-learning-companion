---
key: 平台全量/电商首尾帧做视频 wan2.1_1915439922881167362.json
name: 电商首尾帧做视频 wan2.1_1915439922881167362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电商首尾帧做视频 wan2.1_1915439922881167362.json
hash: cc1d8425bd40f59e
coverage: 0.738095
learned_at: 2026-11-14 02:25:33
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, Note, WanVideoVRAMManagement, Note, Note, Note, LoadWanVideoT5TextEncoder, Note, Note, CLIPVisionLoader, ImageResize+, SetNode, SetNode, GetNode, GetNode, EmptyImage, AddLabel, AddLabel, ImageConcatMulti, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, CLIPTextEncode, WanVideoTeaCache, WanVideoSampler, MarkdownNote, WanVideoImageToVideoEncode, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, LoadImage, LoadImage, WanVideoTextEncode, ImageResize+, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/电商首尾帧做视频 wan2.1_1915439922881167362.json

> 来源文件 `comfyui_library/workflows/平台全量/电商首尾帧做视频 wan2.1_1915439922881167362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoTextEmbedBridge`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
- `WanVideoVRAMManagement`
- `Note`
- `Note`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `CLIPVisionLoader`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `CLIPTextEncode` ★核心
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `ImageResize+`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoVRAMManagement`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`ImageResize+`、`EmptyImage`、`AddLabel`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LoadImage`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：CLIPLoader、CLIPTextEncode、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode
