---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json
name: Flux.1-Krea-Dev文生图&图生图_1951146810876305409
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json
hash: 1eff3e074f219010
coverage: 0.903226
learned_at: 2026-10-15 22:26:25
nodes: [DualCLIPLoader, VAELoader, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, VAEDecode, easy showAnything, UNETLoader, RH_Translator, DualCLIPLoader, VAELoader, VAEDecode, UNETLoader, KSampler, SDXL Empty Latent Image (rgthree), RepeatLatentBatch, VAEEncode, RH_Translator, RH_Captioner, Text Concatenate, easy showAnything, LoadImage, LayerUtility: TextBox, KSampler, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, LayerUtility: TextBox, SaveImage, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 202412543674784, "steps": 20}
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `DualCLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `UNETLoader` ★核心
- `RH_Translator`
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SDXL Empty Latent Image (rgthree)`
- `RepeatLatentBatch`
- `VAEEncode` ★核心
- `RH_Translator`
- `RH_Captioner`
- `Text Concatenate`
- `easy showAnything`
- `LoadImage`
- `LayerUtility: TextBox`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `LayerUtility: TextBox`
- `SaveImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `202412543674784`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`DualCLIPLoader`、`VAELoader`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`RH_Translator`、`KSampler`、`SDXL Empty Latent Image (rgthree)`、`RepeatLatentBatch`、`VAEEncode`、`RH_Captioner`、`Text Concatenate`、`LoadImage`、`LayerUtility: TextBox`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
