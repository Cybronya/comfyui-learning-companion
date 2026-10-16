---
key: 视频生成/图生视频/【遇见AI】wan2.1 UniAnimate视频转绘 动作参考_2062803456766861313.json
name: 【遇见AI】wan2.1 UniAnimate视频转绘 动作参考_2062803456766861313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062803456766861313.json
hash: 3e8e53740834fede
coverage: 0.84375
learned_at: 2026-10-15 22:39:07
nodes: [WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, PreviewImage, WanVideoImageToVideoEncode, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, WanVideoClipVisionEncode, WanVideoUniAnimateDWPoseDetector, LoadImage, MarkdownNote, LoadImage, WanVideoUniAnimatePoseInput, PreviewImage, PreviewImage, WanVideoBlockSwap, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader, CLIPVisionLoader, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1 UniAnimate视频转绘 动作参考_2062803456766861313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062803456766861313.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（32 个）：
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PreviewImage`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `WanVideoUniAnimateDWPoseDetector`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `WanVideoUniAnimatePoseInput`
- `PreviewImage`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoUniAnimateDWPoseDetector`、`LoadImage`、`WanVideoUniAnimatePoseInput`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`CLIPVisionLoader`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
