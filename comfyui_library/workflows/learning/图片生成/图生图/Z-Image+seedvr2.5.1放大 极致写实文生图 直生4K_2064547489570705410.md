---
key: 图片生成/图生图/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2064547489570705410.json
name: Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2064547489570705410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2064547489570705410.json
hash: 6f34eb4d660249c4
coverage: 0.95
learned_at: 2026-10-23 11:29:31
nodes: [ModelSamplingAuraFlow, ConditioningZeroOut, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAELoader, CLIPTextEncode, CR Text Concatenate, Text, UNETLoader, CLIPLoader, SaveImage, PreviewImage, KSampler, VAEDecode, SeedVR2LoadDiTModel, LayerUtility: PurgeVRAM V2, Lora Loader Stack (rgthree), CR SDXL Aspect Ratio, ImpactInt, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "sgm_uniform", "seed": 588995414646609, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2064547489570705410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2064547489570705410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `LayerUtility: PurgeVRAM V2`
- `Lora Loader Stack (rgthree)`
- `CR SDXL Aspect Ratio`
- `ImpactInt`
- `Text`

## 关键参数

- `seed` = `588995414646609`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VAELoader`、`CLIPTextEncode`、`CR Text Concatenate`、`Text`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`KSampler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`LayerUtility: PurgeVRAM V2`、`Lora Loader Stack (rgthree)`、`CR SDXL Aspect Ratio`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
