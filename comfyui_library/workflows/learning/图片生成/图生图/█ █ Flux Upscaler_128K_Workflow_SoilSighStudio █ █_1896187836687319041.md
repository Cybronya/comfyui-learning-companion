---
key: 图片生成/图生图/█ █ Flux Upscaler_128K_Workflow_SoilSighStudio █ █_1896187836687319041.json
name: █ █ Flux Upscaler_128K_Workflow_SoilSighStudio █ █_1896187836687319041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/█ █ Flux Upscaler_128K_Workflow_SoilSighStudio █ █_1896187836687319041.json
hash: a3e320a3afe28116
coverage: 0.301587
learned_at: 2026-10-23 11:47:16
nodes: [LoadImage, SetNode, SetNode, Note, Load Image Batch, SetNode, SetNode, SetNode, SetNode, BasicGuider, CLIPTextEncode, Latent Noise Injection, ModelSamplingFlux, VAEEncode, GetNode, GetImageSizeAndCount, GetNode, String Literal, GetNode, FluxGuidance, ConditioningZeroOut, GetNode, ControlNetApplySD3, SetNode, SetNode, KSamplerSelect, BasicScheduler, SetNode, SetNode, VAEDecode, SetNode, PlaySound|pysssss, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RandomNoise, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SaveImage, SaveImage, SaveImage, UltimateSDUpscaleCustomSample, UltimateSDUpscaleCustomSample, UltimateSDUpscaleCustomSample, UltimateSDUpscaleCustomSample, UltimateSDUpscaleCustomSample, UltimateSDUpscaleCustomSample, UltimateSDUpscaleCustomSample, DualCLIPLoader, VAELoader, Upscale Model Loader, ControlNetLoader, easy imageScaleDownToSize, UNETLoader, SaveImage, SaveImage, SaveImage, SaveImage, SamplerCustomAdvanced, Fast Groups Bypasser (rgthree), Reroute]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6}
---

# 图片生成/图生图/█ █ Flux Upscaler_128K_Workflow_SoilSighStudio █ █_1896187836687319041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/█ █ Flux Upscaler_128K_Workflow_SoilSighStudio █ █_1896187836687319041.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（126 个）：
- `LoadImage`
- `SetNode`
- `SetNode`
- `Note`
- `Load Image Batch`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `Latent Noise Injection`
- `ModelSamplingFlux`
- `VAEEncode` ★核心
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `String Literal`
- `GetNode`
- `FluxGuidance`
- `ConditioningZeroOut`
- `GetNode`
- `ControlNetApplySD3` ★核心
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `PlaySound|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `UltimateSDUpscaleCustomSample`
- `UltimateSDUpscaleCustomSample`
- `UltimateSDUpscaleCustomSample`
- `UltimateSDUpscaleCustomSample`
- `UltimateSDUpscaleCustomSample`
- `UltimateSDUpscaleCustomSample`
- `UltimateSDUpscaleCustomSample`
- `DualCLIPLoader`
- `VAELoader`
- `Upscale Model Loader`
- `ControlNetLoader`
- `easy imageScaleDownToSize`
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Reroute`

## 关键参数

- `controlnet_strength` = `0.6`

## 知识

覆盖率 **30%**（38/126）

**有卡**：`LoadImage`、`Load Image Batch`、`BasicGuider`、`CLIPTextEncode`、`Latent Noise Injection`、`ModelSamplingFlux`、`VAEEncode`、`GetImageSizeAndCount`、`String Literal`、`FluxGuidance`、`ConditioningZeroOut`、`ControlNetApplySD3`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`PlaySound|pysssss`、`RandomNoise`、`SaveImage`、`UltimateSDUpscaleCustomSample`、`DualCLIPLoader`、`VAELoader`、`Upscale Model Loader`、`ControlNetLoader`、`easy imageScaleDownToSize`、`UNETLoader`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、ControlNetApplySD3
