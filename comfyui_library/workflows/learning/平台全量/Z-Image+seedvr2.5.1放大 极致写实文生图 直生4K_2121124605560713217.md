---
key: 平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121124605560713217.json
name: Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121124605560713217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121124605560713217.json
hash: b9b5536fbbbe5d1a
coverage: 0.904762
learned_at: 2026-11-14 01:08:11
nodes: [ModelSamplingAuraFlow, ConditioningZeroOut, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAELoader, CLIPTextEncode, CR Text Concatenate, ImpactInt, Text, CR SDXL Aspect Ratio, UNETLoader, CLIPLoader, SaveImage, Note, Text, PreviewImage, KSampler, VAEDecode, SeedVR2LoadDiTModel, LayerUtility: PurgeVRAM V2, Lora Loader Stack (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "sgm_uniform", "seed": 253126799421128, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121124605560713217.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121124605560713217.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `ImpactInt`
- `Text`
- `CR SDXL Aspect Ratio`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `Note`
- `Text`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `LayerUtility: PurgeVRAM V2`
- `Lora Loader Stack (rgthree)`

## 关键参数

- `seed` = `253126799421128`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VAELoader`、`CLIPTextEncode`、`CR Text Concatenate`、`ImpactInt`、`Text`、`CR SDXL Aspect Ratio`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`KSampler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`LayerUtility: PurgeVRAM V2`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
