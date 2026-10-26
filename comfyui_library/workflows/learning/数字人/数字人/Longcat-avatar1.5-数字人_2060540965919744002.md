---
key: 数字人/数字人/Longcat-avatar1.5-数字人_2060540965919744002.json
name: Longcat-avatar1.5-数字人_2060540965919744002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Longcat-avatar1.5-数字人_2060540965919744002.json
hash: ae7baace4eacdfb9
coverage: 1
learned_at: 2026-10-26 01:56:27
nodes: [LoadImage, CR Prompt Text, LoadAudio, WanVideoTextEncodeCached, TrimAudioDuration, WanVideoVAELoader, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, ComfyNumberConvert, WanVideoSampler, WanVideoEncode, ComfyMathExpression, WhisperModelLoader, Float, WanAnimatePlus BlockSwap, ImageResizeKJv2, WanVideoLongCatAvatarExtendEmbeds, LongCatAvatarWhisperEmbeds, WanVideoLoraSelect, Int, Int]
patterns: []
missing: []
---

# 数字人/数字人/Longcat-avatar1.5-数字人_2060540965919744002.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Longcat-avatar1.5-数字人_2060540965919744002.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `LoadImage`
- `CR Prompt Text`
- `LoadAudio`
- `WanVideoTextEncodeCached`
- `TrimAudioDuration`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `ComfyNumberConvert`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `ComfyMathExpression`
- `WhisperModelLoader`
- `Float`
- `WanAnimatePlus BlockSwap`
- `ImageResizeKJv2`
- `WanVideoLongCatAvatarExtendEmbeds`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoLoraSelect`
- `Int`
- `Int`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`LoadImage`、`CR Prompt Text`、`LoadAudio`、`WanVideoTextEncodeCached`、`TrimAudioDuration`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoModelLoader`、`ComfyNumberConvert`、`WanVideoSampler`、`WanVideoEncode`、`ComfyMathExpression`、`WhisperModelLoader`、`Float`、`WanAnimatePlus BlockSwap`、`ImageResizeKJv2`、`WanVideoLongCatAvatarExtendEmbeds`、`LongCatAvatarWhisperEmbeds`、`WanVideoLoraSelect`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CR Prompt Text
