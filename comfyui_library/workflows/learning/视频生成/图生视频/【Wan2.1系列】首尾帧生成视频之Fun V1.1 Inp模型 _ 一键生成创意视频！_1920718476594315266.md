---
key: 视频生成/图生视频/【Wan2.1系列】首尾帧生成视频之Fun V1.1 Inp模型 _ 一键生成创意视频！_1920718476594315266.json
name: 【Wan2.1系列】首尾帧生成视频之Fun V1.1 Inp模型 _ 一键生成创意视频！_1920718476594315266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【Wan2.1系列】首尾帧生成视频之Fun V1.1 Inp模型 _ 一键生成创意视频！_1920718476594315266.json
hash: 23d3a49f255b9a29
coverage: 0.833333
learned_at: 2026-10-15 22:29:42
nodes: [LoadWanVideoT5TextEncoder, ImageResize+, SetNode, SetNode, GetNode, GetNode, EmptyImage, AddLabel, AddLabel, ImageConcatMulti, ImageConcatMulti, GetImageSizeAndCount, WanVideoSLG, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoTeaCache, WanVideoSampler, ImageResize+, CLIPVisionLoader, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoModelLoader, WanVideoVAELoader, VHS_VideoCombine, LoadImage, LoadImage, WanVideoTextEncode, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/【Wan2.1系列】首尾帧生成视频之Fun V1.1 Inp模型 _ 一键生成创意视频！_1920718476594315266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1920718476594315266.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `ImageResize+`
- `CLIPVisionLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `MarkdownNote`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`LoadWanVideoT5TextEncoder`、`ImageResize+`、`EmptyImage`、`AddLabel`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoSampler`、`CLIPVisionLoader`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
