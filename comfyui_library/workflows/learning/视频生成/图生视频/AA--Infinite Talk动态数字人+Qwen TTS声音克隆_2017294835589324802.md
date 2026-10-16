---
key: 视频生成/图生视频/AA--Infinite Talk动态数字人+Qwen TTS声音克隆_2017294835589324802.json
name: AA--Infinite Talk动态数字人+Qwen TTS声音克隆_2017294835589324802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017294835589324802.json
hash: 4c53b24182e4829b
coverage: 0.9
learned_at: 2026-10-15 22:34:47
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, AudioEncoderEncode, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, easy seed, ModelPatchLoader, RH_GetAudioDuration, CastAnyToIntStringFloat, MathExpression|pysssss, easy showAnything, JWInteger, PainterAudioCut, MathExpression|pysssss, PreviewAny, LayerUtility: PurgeVRAM, easy cleanGpuUsed, LayerUtility: PurgeVRAM, AudioEncoderLoader, FB_Qwen3TTSVoiceClone, UNETLoader, ModelSamplingSD3, ColorMatch, RIFE VFI, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, SaveAudio, easy showAnything, easy showAnything, WhisperSTT, JWInteger, Note, CR Prompt Text, CR Prompt Text, LoadAudio, JWInteger, JWInteger, LoadImage, PainterAI2V]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "dpmpp_sde", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/AA--Infinite Talk动态数字人+Qwen TTS声音克隆_2017294835589324802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017294835589324802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `AudioEncoderEncode`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy seed`
- `ModelPatchLoader`
- `RH_GetAudioDuration`
- `CastAnyToIntStringFloat`
- `MathExpression|pysssss`
- `easy showAnything`
- `JWInteger`
- `PainterAudioCut`
- `MathExpression|pysssss`
- `PreviewAny`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `AudioEncoderLoader`
- `FB_Qwen3TTSVoiceClone`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ColorMatch`
- `RIFE VFI`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `SaveAudio`
- `easy showAnything`
- `easy showAnything`
- `WhisperSTT`
- `JWInteger`
- `Note`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadAudio`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `PainterAI2V`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_sde`
- `denoise` = `normal`

## 知识

覆盖率 **90%**（45/50）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`AudioEncoderEncode`、`VAEDecode`、`easy cleanGpuUsed`、`easy seed`、`ModelPatchLoader`、`RH_GetAudioDuration`、`CastAnyToIntStringFloat`、`MathExpression|pysssss`、`JWInteger`、`PainterAudioCut`、`LayerUtility: PurgeVRAM`、`AudioEncoderLoader`、`FB_Qwen3TTSVoiceClone`、`ColorMatch`、`RIFE VFI`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveAudio`、`WhisperSTT`、`CR Prompt Text`、`LoadAudio`、`LoadImage`、`PainterAI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
