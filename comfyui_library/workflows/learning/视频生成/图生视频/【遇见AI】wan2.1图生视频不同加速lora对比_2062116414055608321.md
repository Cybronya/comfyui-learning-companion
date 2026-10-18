---
key: 视频生成/图生视频/【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json
name: 【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json
hash: 6807dda76d95ade4
coverage: 0.964286
learned_at: 2026-10-15 22:39:00
nodes: [WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, WanVideoVRAMManagement, WanVideoDecode, WanVideoSampler, VHS_VideoCombine, LoadImage, MarkdownNote, LoadImage, WanVideoTextEncodeCached, WanVideoVAELoader, CLIPVisionLoader, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062116414055608321.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `WanVideoVRAMManagement`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoVRAMManagement`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
