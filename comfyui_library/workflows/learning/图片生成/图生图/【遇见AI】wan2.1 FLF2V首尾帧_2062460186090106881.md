---
key: 图片生成/图生图/【遇见AI】wan2.1 FLF2V首尾帧_2062460186090106881.json
name: 【遇见AI】wan2.1 FLF2V首尾帧_2062460186090106881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 FLF2V首尾帧_2062460186090106881.json
hash: 52c03014f4427bb7
coverage: 0.96
learned_at: 2026-10-23 11:52:23
nodes: [WanVideoImageToVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, LoadImage, MarkdownNote, LoadImage, WanVideoTextEncodeCached, WanVideoVAELoader, LoadImage, LoadImage, WanVideoModelLoader, CLIPVisionLoader, ImageResizeKJv2, ImageResizeKJv2, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoSLG, WanVideoTeaCache, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】wan2.1 FLF2V首尾帧_2062460186090106881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 FLF2V首尾帧_2062460186090106881.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoImageToVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`WanVideoImageToVideoEncode`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoSLG`、`WanVideoTeaCache`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
