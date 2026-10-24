---
key: 图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json
name: Wan2.1首尾帧控制_1904236934053666817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json
hash: 8017f4d4c6c6e62d
coverage: 0.871795
learned_at: 2026-10-23 11:27:54
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, CLIPTextEncode, Note, GetNode, GetNode, EmptyImage, AddLabel, AddLabel, ImageConcatMulti, LoadImage, CLIPVisionLoader, ImageResize+, WanVideoTeaCache, WanVideoTextEncode, ImageConcatMulti, Text Multiline, LoadImage, WanVideoVRAMManagement, WanVideoBlockSwap, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, WanVideoModelLoader, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoVAELoader, ImageResize+, WanVideoClipVisionEncode, SetNode, SetNode, WanVideoImageToVideoEncode, WanVideoImageToVideoEncode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoTextEmbedBridge`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `LoadImage`
- `CLIPVisionLoader`
- `ImageResize+`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `ImageConcatMulti`
- `Text Multiline`
- `LoadImage`
- `WanVideoVRAMManagement`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`EmptyImage`、`AddLabel`、`ImageConcatMulti`、`LoadImage`、`CLIPVisionLoader`、`ImageResize+`、`WanVideoTeaCache`、`WanVideoTextEncode`、`Text Multiline`、`WanVideoVRAMManagement`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
