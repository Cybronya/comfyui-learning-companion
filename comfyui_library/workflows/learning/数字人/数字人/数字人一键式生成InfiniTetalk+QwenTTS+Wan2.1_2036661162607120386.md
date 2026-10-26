---
key: 数字人/数字人/数字人一键式生成InfiniTetalk+QwenTTS+Wan2.1_2036661162607120386.json
name: 数字人一键式生成InfiniTetalk+QwenTTS+Wan2.1_2036661162607120386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/数字人一键式生成InfiniTetalk+QwenTTS+Wan2.1_2036661162607120386.json
hash: 9488932e7f582bcf
coverage: 0.587302
learned_at: 2026-10-26 02:02:46
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoClipVisionEncode, Reroute, SetNode, easy showAnything, CLIPVisionLoader, Reroute, Reroute, Anything Everywhere, Reroute, Reroute, SetNode, WanVideoLoraSelect, WanVideoTorchCompileSettings, Audio Duration (mtb), MathExpression|pysssss, AudioSeparation, GetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, DownloadAndLoadWav2VecModel, WanVideoBlockSwap, MathExpression|pysssss, MultiTalkWav2VecEmbeds, PlaySound|pysssss, WanVideoDecode, GetNode, PreviewAudio, MultiTalkModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, PreviewAudio, AudioCrop, AudioCrop, Qwen3TTSVoiceClone, SetNode, WanVideoSampler, GetImageRangeFromBatch, Qwen3TTSModelLoader, Fast Groups Bypasser (rgthree), Reroute, Reroute, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, Reroute, LayerUtility: ImageScaleByAspectRatio V2, easy int, Note, Note, Note, LoadAudio, LoadImage, PreviewAudio, CR Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/数字人一键式生成InfiniTetalk+QwenTTS+Wan2.1_2036661162607120386.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/数字人一键式生成InfiniTetalk+QwenTTS+Wan2.1_2036661162607120386.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（63 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoClipVisionEncode`
- `Reroute`
- `SetNode`
- `easy showAnything`
- `CLIPVisionLoader`
- `Reroute`
- `Reroute`
- `Anything Everywhere`
- `Reroute`
- `Reroute`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `AudioSeparation`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `MultiTalkWav2VecEmbeds`
- `PlaySound|pysssss`
- `WanVideoDecode`
- `GetNode`
- `PreviewAudio`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `PreviewAudio`
- `AudioCrop`
- `AudioCrop`
- `Qwen3TTSVoiceClone`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `Qwen3TTSModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Reroute`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `Note`
- `Note`
- `Note`
- `LoadAudio`
- `LoadImage`
- `PreviewAudio`
- `CR Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **59%**（37/63）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`AudioSeparation`、`WanVideoModelLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoBlockSwap`、`MultiTalkWav2VecEmbeds`、`PlaySound|pysssss`、`WanVideoDecode`、`PreviewAudio`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`AudioCrop`、`Qwen3TTSVoiceClone`、`WanVideoSampler`、`GetImageRangeFromBatch`、`Qwen3TTSModelLoader`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`LoadAudio`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
