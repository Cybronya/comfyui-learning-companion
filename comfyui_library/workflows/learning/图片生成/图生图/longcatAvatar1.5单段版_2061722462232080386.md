---
key: 图片生成/图生图/longcatAvatar1.5单段版_2061722462232080386.json
name: longcatAvatar1.5单段版_2061722462232080386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/longcatAvatar1.5单段版_2061722462232080386.json
hash: 25d780a2a2e001dd
coverage: 1
learned_at: 2026-10-23 11:40:53
nodes: [WanVideoSetBlockSwap, LongCatAvatarWhisperEmbeds, WanVideoModelLoader, WanVideoLoraSelect, WhisperModelLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, FloatConstant, WanVideoBlockSwap, WanVideoVAELoader, INTConstant, INTConstant, WanVideoLongCatAvatarExtendEmbeds, ImageResizeKJv2, WanVideoEncode, LoadAudio, CR Text, LoadImage, WanVideoSampler, TrimAudioDuration, ComfyNumberConvert, ComfyMathExpression]
patterns: []
missing: []
---

# 图片生成/图生图/longcatAvatar1.5单段版_2061722462232080386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/longcatAvatar1.5单段版_2061722462232080386.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（24 个）：
- `WanVideoSetBlockSwap`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WhisperModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `FloatConstant`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `LoadAudio`
- `CR Text`
- `LoadImage`
- `WanVideoSampler` ★核心
- `TrimAudioDuration`
- `ComfyNumberConvert`
- `ComfyMathExpression`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`WanVideoSetBlockSwap`、`LongCatAvatarWhisperEmbeds`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WhisperModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`FloatConstant`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`INTConstant`、`WanVideoLongCatAvatarExtendEmbeds`、`ImageResizeKJv2`、`WanVideoEncode`、`LoadAudio`、`CR Text`、`LoadImage`、`WanVideoSampler`、`TrimAudioDuration`、`ComfyNumberConvert`、`ComfyMathExpression`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
