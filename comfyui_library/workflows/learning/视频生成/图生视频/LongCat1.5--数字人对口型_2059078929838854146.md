---
key: 视频生成/图生视频/LongCat1.5--数字人对口型_2059078929838854146.json
name: LongCat1.5--数字人对口型_2059078929838854146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LongCat1.5--数字人对口型_2059078929838854146.json
hash: 6dadefa0c8c086a2
coverage: 0.827586
learned_at: 2026-10-15 22:38:36
nodes: [WanVideoSetBlockSwap, TrimAudioDuration, WanVideoVAELoader, WhisperModelLoader, WanVideoBlockSwap, LongCatAvatarWhisperEmbeds, WanVideoLongCatAvatarExtendEmbeds, ImageResizeKJv2, WanVideoEncode, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, ComfyNumberConvert, SimpleMath+, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, Text, LoadImage, Note, Note, LoadAudio, Int, Int, Note, Note, Note, Float]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat1.5--数字人对口型_2059078929838854146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059078929838854146.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoSetBlockSwap`
- `TrimAudioDuration`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `WanVideoBlockSwap`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ComfyNumberConvert`
- `SimpleMath+`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `Text`
- `LoadImage`
- `Note`
- `Note`
- `LoadAudio`
- `Int`
- `Int`
- `Note`
- `Note`
- `Note`
- `Float`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`WanVideoSetBlockSwap`、`TrimAudioDuration`、`WanVideoVAELoader`、`WhisperModelLoader`、`WanVideoBlockSwap`、`LongCatAvatarWhisperEmbeds`、`WanVideoLongCatAvatarExtendEmbeds`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`ComfyNumberConvert`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`Text`、`LoadImage`、`LoadAudio`、`Int`、`Float`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
