---
key: 图片生成/文生图/Z-image-base 兼顾 Z-image-turbo lora 双采样工作流_2067512561997795329.json
name: Z-image-base 兼顾 Z-image-turbo lora 双采样工作流_2067512561997795329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-base 兼顾 Z-image-turbo lora 双采样工作流_2067512561997795329.json
hash: d4f458fc6809f10e
coverage: 0.882353
learned_at: 2026-10-19 23:21:58
nodes: [Text, ImpactInt, EmptySD3LatentImage, SaveImage, ModelSamplingAuraFlow, CLIPTextEncode, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPTextEncode, ConditioningZeroOut, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, PreviewImage, CLIPLoaderGGUF, VAELoader, LayerUtility: PurgeVRAM, VAEDecode, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, PreviewImage, SeedVR2LoadVAEModel, Text Concatenate, Text, Lora Loader Stack (rgthree), Lora Loader Stack (rgthree), UNETLoader, UNETLoader, 孤海注释, 孤海注释, Text, Text, Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "beta57", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 图片生成/文生图/Z-image-base 兼顾 Z-image-turbo lora 双采样工作流_2067512561997795329.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-base 兼顾 Z-image-turbo lora 双采样工作流_2067512561997795329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `Text`
- `ImpactInt`
- `EmptySD3LatentImage`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `CLIPLoaderGGUF`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `Text Concatenate`
- `Text`
- `Lora Loader Stack (rgthree)`
- `Lora Loader Stack (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `孤海注释`
- `孤海注释`
- `Text`
- `Text`
- `Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `beta57`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`Text`、`ImpactInt`、`EmptySD3LatentImage`、`SaveImage`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`ConditioningZeroOut`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LayerUtility: PurgeVRAM`、`CLIPLoaderGGUF`、`VAELoader`、`VAEDecode`、`KSamplerAdvanced`、`SeedVR2LoadVAEModel`、`Text Concatenate`、`Lora Loader Stack (rgthree)`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader、KSamplerAdvanced、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel
