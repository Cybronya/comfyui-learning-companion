---
key: 音频生成/音频生成/用InfiniteTalk + Qwen3-TTS 对口型，一键生成MOSS给刘培强庆生视频！_2018671065148432385.json
name: 用InfiniteTalk + Qwen3-TTS 对口型，一键生成MOSS给刘培强庆生视频！_2018671065148432385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/用InfiniteTalk + Qwen3-TTS 对口型，一键生成MOSS给刘培强庆生视频！_2018671065148432385.json
hash: dab69d8c2bbd0047
coverage: 0.794118
learned_at: 2026-10-18 02:07:11
nodes: [UNETLoader, CLIPLoader, LoadAudio, LoraLoaderModelOnly, ConditioningZeroOut, AudioEncoderEncode, AudioEncoderLoader, LoadImage, KSamplerSelect, CFGGuider, BasicScheduler, RandomNoise, KSamplerSelect, BasicScheduler, RandomNoise, AudioCrop, PreviewAudio, LoadAudio, CR Text, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, LoadAudio, LoadImage, AudioEncoderEncode, SamplerCustomAdvanced, CFGGuider, SamplerCustomAdvanced, VAEDecode, ImageFromBatch, KSamplerSelect, BasicScheduler, RandomNoise, CFGGuider, SamplerCustomAdvanced, ImageFromBatch, PrimitiveInt, PrimitiveInt, Reroute, ModelPatchLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, MarkdownNote, VAEDecode, VAELoader, Reroute, ImageBatch, VAEDecode, ImageBatch, AudioConcat, MarkdownNote, WanInfiniteTalkToVideo, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanInfiniteTalkToVideo, WanInfiniteTalkToVideo, CreateVideo, MarkdownNote, CR Text, SaveAudio, CLIPTextEncode, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 音频生成/音频生成/用InfiniteTalk + Qwen3-TTS 对口型，一键生成MOSS给刘培强庆生视频！_2018671065148432385.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/用InfiniteTalk + Qwen3-TTS 对口型，一键生成MOSS给刘培强庆生视频！_2018671065148432385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `LoadImage`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `AudioCrop`
- `PreviewAudio`
- `LoadAudio`
- `CR Text`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `LoadAudio`
- `LoadImage`
- `AudioEncoderEncode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ImageFromBatch`
- `PrimitiveInt`
- `PrimitiveInt`
- `Reroute`
- `ModelPatchLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `VAEDecode` ★核心
- `VAELoader`
- `Reroute`
- `ImageBatch`
- `VAEDecode` ★核心
- `ImageBatch`
- `AudioConcat`
- `MarkdownNote`
- `WanInfiniteTalkToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `WanInfiniteTalkToVideo`
- `CreateVideo`
- `MarkdownNote`
- `CR Text`
- `SaveAudio`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **79%**（54/68）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoadAudio`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`AudioEncoderEncode`、`AudioEncoderLoader`、`LoadImage`、`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`RandomNoise`、`AudioCrop`、`PreviewAudio`、`CR Text`、`Qwen3TTSModelLoader`、`Qwen3TTSVoiceClone`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageFromBatch`、`ModelPatchLoader`、`VAELoader`、`ImageBatch`、`AudioConcat`、`WanInfiniteTalkToVideo`、`VHS_VideoCombine`、`CreateVideo`、`SaveAudio`、`CLIPTextEncode`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
