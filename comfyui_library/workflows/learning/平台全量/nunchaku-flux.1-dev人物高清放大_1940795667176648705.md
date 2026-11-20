---
key: 平台全量/nunchaku-flux.1-dev人物高清放大_1940795667176648705.json
name: nunchaku-flux.1-dev人物高清放大_1940795667176648705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/nunchaku-flux.1-dev人物高清放大_1940795667176648705.json
hash: 7808415dcce3c572
coverage: 0.942857
learned_at: 2026-11-14 01:15:32
nodes: [UNETLoader, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, EmptyLatentImage, FluxResolutionNode, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, VAELoader, FluxGuidance, ReferenceLatent, VAEEncode, ImageResize+, VAEDecode, SamplerCustomAdvanced, LoadImage, ModelSamplingFlux, SaveImage, UpscaleModelLoader, Note, UNETLoader, VAELoader, UpscaleModelLoader, UltimateSDUpscale, SaveImage, DualCLIPLoader, DualCLIPLoader, ConditioningZeroOut, CLIPTextEncode, LoraLoader, CLIPTextEncode, Image Comparer (rgthree)]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1280, "lora_name": "my_first_Kontext_lora_v1.safetensors", "strength_clip": 1, "strength_model": 1, "width": 1024}
---

# 平台全量/nunchaku-flux.1-dev人物高清放大_1940795667176648705.json

> 来源文件 `comfyui_library/workflows/平台全量/nunchaku-flux.1-dev人物高清放大_1940795667176648705.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `EmptyLatentImage` ★核心
- `FluxResolutionNode`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAELoader`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageResize+`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `ModelSamplingFlux`
- `SaveImage`
- `UpscaleModelLoader`
- `Note`
- `UNETLoader` ★核心
- `VAELoader`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `SaveImage`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `lora_name` = `my_first_Kontext_lora_v1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`UNETLoader`、`MathExpression|pysssss`、`EmptyLatentImage`、`FluxResolutionNode`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`VAELoader`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`ImageResize+`、`VAEDecode`、`SamplerCustomAdvanced`、`LoadImage`、`ModelSamplingFlux`、`SaveImage`、`UpscaleModelLoader`、`UltimateSDUpscale`、`DualCLIPLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、FluxGuidance
