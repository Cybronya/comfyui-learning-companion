---
key: 图片生成/文生图/Z-Image+EngineerV4提示词优化+fdpo光影优化+Kook极致写实+Seedvr放大_2054738492026048513.json
name: Z-Image+EngineerV4提示词优化+fdpo光影优化+Kook极致写实+Seedvr放大_2054738492026048513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image+EngineerV4提示词优化+fdpo光影优化+Kook极致写实+Seedvr放大_2054738492026048513.json
hash: 6b166630a594b09f
coverage: 0.904762
learned_at: 2026-10-19 22:45:47
nodes: [ModelSamplingAuraFlow, ConditioningZeroOut, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAELoader, CLIPTextEncode, CR Text Concatenate, ImpactInt, Text, CR SDXL Aspect Ratio, UNETLoader, SaveImage, Note, PreviewImage, KSampler, VAEDecode, SeedVR2LoadDiTModel, LayerUtility: PurgeVRAM V2, CLIPLoaderGGUF, Lora Loader Stack (rgthree), Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "sgm_uniform", "seed": 286274340096384, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image+EngineerV4提示词优化+fdpo光影优化+Kook极致写实+Seedvr放大_2054738492026048513.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image+EngineerV4提示词优化+fdpo光影优化+Kook极致写实+Seedvr放大_2054738492026048513.json`

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
- `SaveImage`
- `Note`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoaderGGUF`
- `Lora Loader Stack (rgthree)`
- `Text`

## 关键参数

- `seed` = `286274340096384`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VAELoader`、`CLIPTextEncode`、`CR Text Concatenate`、`ImpactInt`、`Text`、`CR SDXL Aspect Ratio`、`UNETLoader`、`SaveImage`、`KSampler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`LayerUtility: PurgeVRAM V2`、`CLIPLoaderGGUF`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
