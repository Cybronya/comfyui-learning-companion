---
key: 视频生成/图生视频/音轨视频生成-wan2.2_2055525011192074241.json
name: 音轨视频生成-wan2.2_2055525011192074241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055525011192074241.json
hash: e5b8f21ab39e38b8
coverage: 0.493827
learned_at: 2026-10-15 22:37:57
nodes: [GetNode, PathchSageAttentionKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, NormalizeAudioLoudness, Qwen3ASRTranscribe, LongCatVoiceCloneTTS, GetNode, AudioCrop, Qwen3ASRLoader, easy showAnything, PreviewAudio, GetNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, SetNode, CLIPLoader, SetNode, SetNode, KSamplerAdvanced, GetNode, GetNode, LoadAudio, SetNode, SetNode, CR Prompt Text, GetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, SetNode, SetNode, easy forLoopEnd, ImageBatch, GetNode, Audio Duration (mtb), KSamplerAdvanced, VAELoader, WanImageToVideo, MathExpression|pysssss, SetNode, ImageFromBatch, GetNode, GetNode, GetNode, SetNode, GetNode, ImageFromBatch, LoadImage, CLIPTextEncode, easy forLoopStart, ModelSamplingSD3, GetNode, GetNode, CLIPTextEncode, GetNode, VHS_VideoCombine, SetNode, MathExpression|pysssss, JWInteger, JWInteger, Float, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/音轨视频生成-wan2.2_2055525011192074241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055525011192074241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（81 个）：
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `NormalizeAudioLoudness`
- `Qwen3ASRTranscribe`
- `LongCatVoiceCloneTTS`
- `GetNode`
- `AudioCrop`
- `Qwen3ASRLoader`
- `easy showAnything`
- `PreviewAudio`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `CR Prompt Text`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `easy forLoopEnd`
- `ImageBatch`
- `GetNode`
- `Audio Duration (mtb)`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `SetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `MathExpression|pysssss`
- `JWInteger`
- `JWInteger`
- `Float`
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **49%**（40/81）

**有卡**：`PathchSageAttentionKJ`、`NormalizeAudioLoudness`、`Qwen3ASRTranscribe`、`LongCatVoiceCloneTTS`、`AudioCrop`、`Qwen3ASRLoader`、`PreviewAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoader`、`KSamplerAdvanced`、`LoadAudio`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`easy forLoopEnd`、`ImageBatch`、`Audio Duration (mtb)`、`VAELoader`、`WanImageToVideo`、`MathExpression|pysssss`、`ImageFromBatch`、`LoadImage`、`CLIPTextEncode`、`easy forLoopStart`、`VHS_VideoCombine`、`JWInteger`、`Float`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
