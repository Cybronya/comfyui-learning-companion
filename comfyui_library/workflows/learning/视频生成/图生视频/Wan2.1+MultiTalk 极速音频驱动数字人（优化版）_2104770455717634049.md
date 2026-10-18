---
key: 视频生成/图生视频/Wan2.1+MultiTalk 极速音频驱动数字人（优化版）_2104770455717634049.json
name: Wan2.1+MultiTalk 极速音频驱动数字人（优化版）_2104770455717634049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1+MultiTalk 极速音频驱动数字人（优化版）_2104770455717634049.json
hash: 5baa567ac87028df
coverage: 0.931034
learned_at: 2026-10-17 22:19:07
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, Anything Everywhere, MultiTalkModelLoader, WanVideoVAELoader, Anything Everywhere, AudioSeparation, LoadAudio, WanVideoTextEncodeCached, Audio Duration (mtb), CLIPVisionLoader, WanVideoClipVisionEncode, DownloadAndLoadWav2VecModel, MathExpression|pysssss, MathExpression|pysssss, ImageResizeKJv2, WanVideoImageToVideoMultiTalk, MultiTalkWav2VecEmbeds, WanVideoSchedulerv2, WanVideoDecode, WanVideoSamplerv2, WanVideoSamplerExtraArgs, VHS_VideoCombine, AudioCrop, INTConstant, INTConstant, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+MultiTalk 极速音频驱动数字人（优化版）_2104770455717634049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.1+MultiTalk 极速音频驱动数字人（优化版）_2104770455717634049.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `Anything Everywhere`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `AudioSeparation`
- `LoadAudio`
- `WanVideoTextEncodeCached`
- `Audio Duration (mtb)`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `DownloadAndLoadWav2VecModel`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkWav2VecEmbeds`
- `WanVideoSchedulerv2`
- `WanVideoDecode`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerExtraArgs` ★核心
- `VHS_VideoCombine`
- `AudioCrop`
- `INTConstant`
- `INTConstant`
- `LoadImage`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`AudioSeparation`、`LoadAudio`、`WanVideoTextEncodeCached`、`Audio Duration (mtb)`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`DownloadAndLoadWav2VecModel`、`MathExpression|pysssss`、`ImageResizeKJv2`、`WanVideoImageToVideoMultiTalk`、`MultiTalkWav2VecEmbeds`、`WanVideoSchedulerv2`、`WanVideoDecode`、`WanVideoSamplerv2`、`WanVideoSamplerExtraArgs`、`VHS_VideoCombine`、`AudioCrop`、`INTConstant`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoSamplerExtraArgs、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelectMulti
