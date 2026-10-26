---
key: 数字人/数字人/LongCat1.5--数字人对口型_2059893332653985793.json
name: LongCat1.5--数字人对口型_2059893332653985793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat1.5--数字人对口型_2059893332653985793.json
hash: fb6d0c31a428f32f
coverage: 0.83871
learned_at: 2026-10-26 01:56:22
nodes: [WanVideoSetBlockSwap, TrimAudioDuration, WanVideoVAELoader, WhisperModelLoader, WanVideoBlockSwap, LongCatAvatarWhisperEmbeds, WanVideoLongCatAvatarExtendEmbeds, ImageResizeKJv2, WanVideoEncode, WanVideoSampler, ComfyNumberConvert, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, Note, Note, Note, Note, Text, Note, WanVideoDecode, CreateVideo, SaveVideo, LoadImage, SimpleMath+, Int, Int, LoadAudio, Audio Duration (mtb), MathExpression|pysssss]
patterns: []
missing: []
---

# 数字人/数字人/LongCat1.5--数字人对口型_2059893332653985793.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat1.5--数字人对口型_2059893332653985793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（31 个）：
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
- `ComfyNumberConvert`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `Note`
- `Note`
- `Note`
- `Note`
- `Text`
- `Note`
- `WanVideoDecode`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `SimpleMath+`
- `Int`
- `Int`
- `LoadAudio`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`WanVideoSetBlockSwap`、`TrimAudioDuration`、`WanVideoVAELoader`、`WhisperModelLoader`、`WanVideoBlockSwap`、`LongCatAvatarWhisperEmbeds`、`WanVideoLongCatAvatarExtendEmbeds`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoSampler`、`ComfyNumberConvert`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`Text`、`WanVideoDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`、`SimpleMath+`、`Int`、`LoadAudio`、`Audio Duration (mtb)`、`MathExpression|pysssss`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
