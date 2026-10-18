---
key: 音频生成/音频生成/自动生成数字人V2-OmniVoice声音设计（方言支持！）-Infinite Talk动态数字人_2041718633499467778.json
name: 自动生成数字人V2-OmniVoice声音设计（方言支持！）-Infinite Talk动态数字人_2041718633499467778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/自动生成数字人V2-OmniVoice声音设计（方言支持！）-Infinite Talk动态数字人_2041718633499467778.json
hash: 4ff7ad8166f39914
coverage: 0.882353
learned_at: 2026-10-18 02:28:49
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, AudioEncoderEncode, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, ModelPatchLoader, JWInteger, PreviewAny, LayerUtility: PurgeVRAM, AudioEncoderLoader, UNETLoader, ColorMatch, RIFE VFI, VHS_VideoCombine, CLIPTextEncode, CR Prompt Text, PainterAudioCut, RH_GetAudioDuration, easy showAnything, easy showAnything, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy saveText, ModelSamplingSD3, easy seed, PainterAI2V, KSamplerAdvanced, CastAnyToIntStringFloat, OmniVoiceVoiceDesignTTS, Note, CR Prompt Text, CR Text, easy showAnything, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, SaveAudio, MathExpression|pysssss, MathExpression|pysssss, Note, Qwen3_VQA, ImageScaleToTotalPixels]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 音频生成/音频生成/自动生成数字人V2-OmniVoice声音设计（方言支持！）-Infinite Talk动态数字人_2041718633499467778.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/自动生成数字人V2-OmniVoice声音设计（方言支持！）-Infinite Talk动态数字人_2041718633499467778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
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
- `PreviewAny`
- `LayerUtility: PurgeVRAM`
- `AudioEncoderLoader`
- `UNETLoader` ★核心
- `ColorMatch`
- `RIFE VFI`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `PainterAudioCut`
- `RH_GetAudioDuration`
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy saveText`
- `ModelSamplingSD3`
- `easy seed`
- `PainterAI2V`
- `KSamplerAdvanced` ★核心
- `CastAnyToIntStringFloat`
- `OmniVoiceVoiceDesignTTS`
- `Note`
- `CR Prompt Text`
- `CR Text`
- `easy showAnything`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `SaveAudio`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Note`
- `Qwen3_VQA`
- `ImageScaleToTotalPixels`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **88%**（45/51）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`AudioEncoderEncode`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`ModelPatchLoader`、`JWInteger`、`LayerUtility: PurgeVRAM`、`AudioEncoderLoader`、`ColorMatch`、`RIFE VFI`、`VHS_VideoCombine`、`CR Prompt Text`、`PainterAudioCut`、`RH_GetAudioDuration`、`easy saveText`、`easy seed`、`PainterAI2V`、`CastAnyToIntStringFloat`、`OmniVoiceVoiceDesignTTS`、`CR Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveAudio`、`MathExpression|pysssss`、`Qwen3_VQA`、`ImageScaleToTotalPixels`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
