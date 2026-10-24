---
key: 图片生成/图生图/【遇见AI】wan2.1 skyreels V3 A2V数字人模型_2067528819833135106.json
name: 【遇见AI】wan2.1 skyreels V3 A2V数字人模型_2067528819833135106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 skyreels V3 A2V数字人模型_2067528819833135106.json
hash: b3b80f7226ad154b
coverage: 0.972222
learned_at: 2026-10-23 11:52:27
nodes: [WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoBlockSwap, MarkdownNote, LoadImage, WanVideoSetBlockSwap, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoPassImagesFromSamples, WanVideoClipVisionEncode, LoadImage, WanVideoLoraSelect, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoSLG, VHS_VideoCombine, WanVideoDecode, LoadImage, WanVideoSampler, WanVideoImageToVideoSkyreelsv3_audio, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, VHS_VideoCombine, TrimAudioDuration, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, LoadAudio, DownloadAndLoadWav2VecModel, MelBandRoFormerModelLoader, CLIPVisionLoader]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】wan2.1 skyreels V3 A2V数字人模型_2067528819833135106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 skyreels V3 A2V数字人模型_2067528819833135106.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（36 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `MarkdownNote`
- `LoadImage`
- `WanVideoSetBlockSwap`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoPassImagesFromSamples`
- `WanVideoClipVisionEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoSkyreelsv3_audio`
- `MelBandRoFormerSampler` ★核心
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `TrimAudioDuration`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `LoadAudio`
- `DownloadAndLoadWav2VecModel`
- `MelBandRoFormerModelLoader`
- `CLIPVisionLoader`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoSetBlockSwap`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoPassImagesFromSamples`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoImageToVideoSkyreelsv3_audio`、`MelBandRoFormerSampler`、`MultiTalkWav2VecEmbeds`、`TrimAudioDuration`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`LoadAudio`、`DownloadAndLoadWav2VecModel`、`MelBandRoFormerModelLoader`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
