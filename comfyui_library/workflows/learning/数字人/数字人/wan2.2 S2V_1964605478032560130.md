---
key: 数字人/数字人/wan2.2 S2V_1964605478032560130.json
name: wan2.2 S2V_1964605478032560130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2 S2V_1964605478032560130.json
hash: 8236820187311ce4
coverage: 0.966667
learned_at: 2026-10-26 01:59:25
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, VAEDecode, WanSoundImageToVideo, ImpactInt, ImpactInt, ImpactInt, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Mute / Bypass Repeater (rgthree), PreviewImage, VHS_LoadAudioUpload, VHS_VideoCombine, ModelSamplingSD3, LoadImage, Fast Bypasser (rgthree), VHS_LoadVideo, Int, DWPreprocessor, AIO_Preprocessor, UNETLoader, LoraLoaderModelOnly, SimpleMath+, Display Int (rgthree), CLIPLoader, VAELoader, AudioEncoderLoader, AudioEncoderEncode, PreviewAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 699297360104631, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/wan2.2 S2V_1964605478032560130.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2 S2V_1964605478032560130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanSoundImageToVideo`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `VHS_LoadAudioUpload`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `LoadImage`
- `Fast Bypasser (rgthree)`
- `VHS_LoadVideo`
- `Int`
- `DWPreprocessor`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `Display Int (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `AudioEncoderLoader`
- `AudioEncoderEncode`
- `PreviewAudio`

## 关键参数

- `seed` = `699297360104631`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`KSampler`、`CLIPTextEncode`、`VAEDecode`、`WanSoundImageToVideo`、`ImpactInt`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Mute / Bypass Repeater (rgthree)`、`VHS_LoadAudioUpload`、`VHS_VideoCombine`、`ModelSamplingSD3`、`Fast Bypasser (rgthree)`、`VHS_LoadVideo`、`Int`、`DWPreprocessor`、`AIO_Preprocessor`、`UNETLoader`、`LoraLoaderModelOnly`、`SimpleMath+`、`Display Int (rgthree)`、`CLIPLoader`、`VAELoader`、`AudioEncoderLoader`、`AudioEncoderEncode`、`PreviewAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
