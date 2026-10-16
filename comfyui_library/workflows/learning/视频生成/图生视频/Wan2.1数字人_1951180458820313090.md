---
key: 视频生成/图生视频/Wan2.1数字人_1951180458820313090.json
name: Wan2.1数字人_1951180458820313090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951180458820313090.json
hash: fea8a9fdd58d4b24
coverage: 1
learned_at: 2026-10-15 22:30:57
nodes: [WanVideoBlockSwap, WanVideoApplyNAG, WanVideoTextEncodeSingle, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoSampler, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, LoadImage, JWInteger, JWInteger, WanVideoTextEncodeSingle, ImageResizeKJv2, AudioSeparation, MathExpression|pysssss, WanVideoLoraSelect, WanVideoTorchCompileSettings, Audio Duration (mtb), LoadAudio, MultiTalkModelLoader, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, WanVideoContextOptions, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoDecode, WanVideoVAELoader, FloatConstant, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1数字人_1951180458820313090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951180458820313090.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoBlockSwap`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `WanVideoTextEncodeSingle`
- `ImageResizeKJv2`
- `AudioSeparation`
- `MathExpression|pysssss`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `Audio Duration (mtb)`
- `LoadAudio`
- `MultiTalkModelLoader`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `WanVideoContextOptions`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `FloatConstant`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoBlockSwap`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`LoadImage`、`JWInteger`、`ImageResizeKJv2`、`AudioSeparation`、`MathExpression|pysssss`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`Audio Duration (mtb)`、`LoadAudio`、`MultiTalkModelLoader`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoContextOptions`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoVAELoader`、`FloatConstant`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
