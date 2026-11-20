---
key: 平台全量/Flux Consistent Character Sheet_1868838232778752001.json
name: Flux Consistent Character Sheet_1868838232778752001
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Consistent Character Sheet_1868838232778752001.json
hash: f36c14382cf5aff1
coverage: 0.878788
learned_at: 2026-11-14 00:27:33
nodes: [IPAdapterModelLoader, CLIPVisionLoader, IPAdapterAdvanced, ControlNetLoader, ControlNetApplyAdvanced, CLIPTextEncode, UNETLoader, PreviewImage, OpenposePreprocessor, PreviewImage, CheckpointLoaderSimple, LoadImage, KSampler, SDXLEmptyLatentSizePicker+, SaveImage, PreviewImage, BasicGuider, SamplerCustomAdvanced, VAEDecode, RandomNoise, VAEEncode, VAEDecode, VAELoader, DualCLIPLoader, KSamplerSelect, PreviewImage, BasicScheduler, UpscaleModelLoader, UltimateSDUpscale, CLIPTextEncode, CLIPTextEncode, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 0, "cfg": 2, "checkpoint": "dreamshaperXL_lightningDPMSDE.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 744820591938151, "steps": 4, "width": "1280x768 (1.67)"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux Consistent Character Sheet_1868838232778752001.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Consistent Character Sheet_1868838232778752001.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `IPAdapterModelLoader`
- `CLIPVisionLoader`
- `IPAdapterAdvanced`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `OpenposePreprocessor`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `KSampler` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `SaveImage`
- `PreviewImage`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `PreviewImage`
- `BasicScheduler`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `checkpoint` = `dreamshaperXL_lightningDPMSDE.safetensors`
- `seed` = `744820591938151`
- `steps` = `4`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1280x768 (1.67)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`IPAdapterModelLoader`、`CLIPVisionLoader`、`IPAdapterAdvanced`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`CLIPTextEncode`、`UNETLoader`、`OpenposePreprocessor`、`CheckpointLoaderSimple`、`LoadImage`、`KSampler`、`SDXLEmptyLatentSizePicker+`、`SaveImage`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`VAEEncode`、`VAELoader`、`DualCLIPLoader`、`KSamplerSelect`、`BasicScheduler`、`UpscaleModelLoader`、`UltimateSDUpscale`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
