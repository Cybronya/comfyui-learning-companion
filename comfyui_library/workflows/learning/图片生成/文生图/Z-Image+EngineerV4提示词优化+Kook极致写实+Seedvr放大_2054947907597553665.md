---
key: 图片生成/文生图/Z-Image+EngineerV4提示词优化+Kook极致写实+Seedvr放大_2054947907597553665.json
name: Z-Image+EngineerV4提示词优化+Kook极致写实+Seedvr放大_2054947907597553665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image+EngineerV4提示词优化+Kook极致写实+Seedvr放大_2054947907597553665.json
hash: 59138f9cb30525f5
coverage: 0.869565
learned_at: 2026-10-21 02:55:44
nodes: [ModelSamplingAuraFlow, ConditioningZeroOut, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAELoader, CLIPTextEncode, CR Text Concatenate, ImpactInt, Text, CR SDXL Aspect Ratio, UNETLoader, SaveImage, Note, PreviewImage, KSampler, VAEDecode, SeedVR2LoadDiTModel, LayerUtility: PurgeVRAM V2, CLIPLoaderGGUF, Lora Loader Stack (rgthree), LoadImage, MarkdownNote, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "sgm_uniform", "seed": 252143612252416, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image+EngineerV4提示词优化+Kook极致写实+Seedvr放大_2054947907597553665.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image+EngineerV4提示词优化+Kook极致写实+Seedvr放大_2054947907597553665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
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
- `SaveImage`
- `Note`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoaderGGUF`
- `Lora Loader Stack (rgthree)`
- `LoadImage`
- `MarkdownNote`
- `Text`

## 关键参数

- `seed` = `252143612252416`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VAELoader`、`CLIPTextEncode`、`CR Text Concatenate`、`ImpactInt`、`Text`、`CR SDXL Aspect Ratio`、`UNETLoader`、`SaveImage`、`KSampler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`LayerUtility: PurgeVRAM V2`、`CLIPLoaderGGUF`、`Lora Loader Stack (rgthree)`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
