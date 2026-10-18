---
key: 视频生成/图生视频/Wan2.1 FLF2V 首尾帧生视频_1928288843513118721.json
name: Wan2.1 FLF2V 首尾帧生视频_1928288843513118721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 FLF2V 首尾帧生视频_1928288843513118721.json
hash: bad0c9eb7c81ec6a
coverage: 0.738095
learned_at: 2026-10-15 22:29:57
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, Note, WanVideoVRAMManagement, Note, Note, Note, Note, Note, CLIPVisionLoader, ImageResize+, GetNode, GetNode, EmptyImage, AddLabel, AddLabel, ImageConcatMulti, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, CLIPTextEncode, WanVideoTeaCache, MarkdownNote, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSLG, LoadWanVideoClipTextEncoder, SetNode, SetNode, WanVideoImageToVideoEncode, WanVideoSampler, LoadImage, LoadImage, WanVideoTextEncode, ImageResize+, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 FLF2V 首尾帧生视频_1928288843513118721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1928288843513118721.json`

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
- `Note`
- `Note`
- `CLIPVisionLoader`
- `ImageResize+`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `CLIPTextEncode` ★核心
- `WanVideoTeaCache`
- `MarkdownNote`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSLG`
- `LoadWanVideoClipTextEncoder` ★核心
- `SetNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `ImageResize+`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoVRAMManagement`、`CLIPVisionLoader`、`ImageResize+`、`EmptyImage`、`AddLabel`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`WanVideoTeaCache`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSLG`、`LoadWanVideoClipTextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`LoadImage`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
