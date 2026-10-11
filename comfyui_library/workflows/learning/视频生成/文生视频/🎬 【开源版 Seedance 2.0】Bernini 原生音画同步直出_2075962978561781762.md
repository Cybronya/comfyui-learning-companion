---
key: 视频生成/文生视频/🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762.json
name: 🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762.json
hash: 34d80626dedbdfb6
coverage: 0.882353
learned_at: 2026-10-11 20:38:49
nodes: [Reroute, CLIPLoader, VAELoader, LoraLoaderModelOnly, AudioEncoderLoader, UNETLoader, UNETLoader, AudioConcat, LoraLoaderModelOnly, AudioSeparation, ComfyNumberConvert, SoundFlow_GetLength, ComfyMathExpression, AudioEncoderEncode, VAEDecode, CLIPTextEncode, RIFEInterpolation, Reroute, LoadAudio, TrimAudioDuration, INTConstant, INTConstant, CLIPTextEncode, LoadImage, PrimitiveStringMultiline, PrimitiveFloat, KSamplerAdvanced, KSamplerAdvanced, TrimAudioDuration, LoadAudio, VHS_VideoCombine, BerniniS2VConditioning, BerniniS2VConditioningV2, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "dpmpp_2m_sde", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（34 个）：
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `AudioConcat`
- `LoraLoaderModelOnly` ★核心
- `AudioSeparation`
- `ComfyNumberConvert`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `AudioEncoderEncode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `RIFEInterpolation`
- `Reroute`
- `LoadAudio`
- `TrimAudioDuration`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `TrimAudioDuration`
- `LoadAudio`
- `VHS_VideoCombine`
- `BerniniS2VConditioning`
- `BerniniS2VConditioningV2`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m_sde`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`UNETLoader`、`AudioConcat`、`AudioSeparation`、`ComfyNumberConvert`、`SoundFlow_GetLength`、`ComfyMathExpression`、`AudioEncoderEncode`、`VAEDecode`、`CLIPTextEncode`、`RIFEInterpolation`、`LoadAudio`、`TrimAudioDuration`、`INTConstant`、`LoadImage`、`KSamplerAdvanced`、`VHS_VideoCombine`、`BerniniS2VConditioning`、`BerniniS2VConditioningV2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
