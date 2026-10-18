---
key: 视频生成/图生视频/AA--自动生成数字人-Infinite Talk动态数字人+Qwen TTS声音设计_2017509213773238274.json
name: AA--自动生成数字人-Infinite Talk动态数字人+Qwen TTS声音设计_2017509213773238274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AA--自动生成数字人-Infinite Talk动态数字人+Qwen TTS声音设计_2017509213773238274.json
hash: 3698044642d0d900
coverage: 0.890909
learned_at: 2026-10-15 22:34:49
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, AudioEncoderEncode, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, ModelPatchLoader, JWInteger, MathExpression|pysssss, PreviewAny, LayerUtility: PurgeVRAM, easy cleanGpuUsed, AudioEncoderLoader, UNETLoader, ColorMatch, RIFE VFI, VHS_VideoCombine, CLIPTextEncode, JWInteger, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, Qwen3TTSModelLoader, CR Prompt Text, SaveAudio, PainterAudioCut, Qwen3TTSVoiceDesign, RH_GetAudioDuration, CastAnyToIntStringFloat, MathExpression|pysssss, easy showAnything, easy showAnything, CR Prompt Text, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, easy saveText, LoadImage, Qwen3_VQA, easy showAnything, ModelSamplingSD3, easy seed, JWInteger, JWInteger, Note, Note, PainterAI2V, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/AA--自动生成数字人-Infinite Talk动态数字人+Qwen TTS声音设计_2017509213773238274.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017509213773238274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
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
- `ModelPatchLoader`
- `JWInteger`
- `MathExpression|pysssss`
- `PreviewAny`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `AudioEncoderLoader`
- `UNETLoader` ★核心
- `ColorMatch`
- `RIFE VFI`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Qwen3TTSModelLoader`
- `CR Prompt Text`
- `SaveAudio`
- `PainterAudioCut`
- `Qwen3TTSVoiceDesign`
- `RH_GetAudioDuration`
- `CastAnyToIntStringFloat`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ImageScaleToTotalPixels`
- `easy saveText`
- `LoadImage`
- `Qwen3_VQA`
- `easy showAnything`
- `ModelSamplingSD3`
- `easy seed`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `PainterAI2V`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **89%**（49/55）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`AudioEncoderEncode`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`ModelPatchLoader`、`JWInteger`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM`、`AudioEncoderLoader`、`ColorMatch`、`RIFE VFI`、`VHS_VideoCombine`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`Qwen3TTSModelLoader`、`SaveAudio`、`PainterAudioCut`、`Qwen3TTSVoiceDesign`、`RH_GetAudioDuration`、`CastAnyToIntStringFloat`、`ImageScaleToTotalPixels`、`easy saveText`、`LoadImage`、`Qwen3_VQA`、`easy seed`、`PainterAI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
