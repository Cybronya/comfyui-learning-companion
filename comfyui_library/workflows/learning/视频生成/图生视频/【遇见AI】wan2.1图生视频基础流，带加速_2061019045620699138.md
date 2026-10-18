---
key: 视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，带加速_2061019045620699138.json
name: 【遇见AI】wan2.1图生视频基础流，带加速_2061019045620699138.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，带加速_2061019045620699138.json
hash: a9ef3dec31d2aa35
coverage: 1
learned_at: 2026-10-15 22:38:51
nodes: [WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, WanVideoVRAMManagement, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader, LoadImage, CLIPVisionLoader, WanVideoModelLoader, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，带加速_2061019045620699138.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061019045620699138.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `WanVideoVRAMManagement`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `LoadImage`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（21/21）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoVRAMManagement`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`LoadImage`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
