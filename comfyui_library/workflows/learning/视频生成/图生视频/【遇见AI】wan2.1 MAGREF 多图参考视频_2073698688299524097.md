---
key: 视频生成/图生视频/【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json
name: 【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json
hash: b3311985c1a9b464
coverage: 0.935484
learned_at: 2026-10-15 22:41:09
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoBlockSwap, WanVideoSampler, WanVideoExperimentalArgs, WanVideoClipVisionEncode, SaveImage, SaveImage, easy imageRemBg, easy imageRemBg, ImageConcatMulti, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, WanVideoImageToVideoEncode, PreviewImage, MarkdownNote, LoadImage, LoadImage, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader, LoadImage, LoadImage, CLIPVisionLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073698688299524097.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（31 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoClipVisionEncode`
- `SaveImage`
- `SaveImage`
- `easy imageRemBg`
- `easy imageRemBg`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `PreviewImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `LoadImage`
- `LoadImage`
- `CLIPVisionLoader`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoClipVisionEncode`、`SaveImage`、`easy imageRemBg`、`ImageConcatMulti`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
