---
key: 图片生成/文生图/qwen3.8 反推、扩写整合 Z-IMAGE 最新_2093885443392757762.json
name: qwen3.8 反推、扩写整合 Z-IMAGE 最新_2093885443392757762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen3.8 反推、扩写整合 Z-IMAGE 最新_2093885443392757762.json
hash: e8ddec10402ac9d7
coverage: 0.638298
learned_at: 2026-10-20 01:19:48
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LayerFilter: HDREffects, GetNode, ConditioningZeroOut, GetNode, GetNode, GetNode, CR Seed, QwenTE_ImageInfer, KSampler (Efficient), VAELoader, ClipLoaderGGUF, CLIPTextEncode, GetNode, SetNode, SetNode, SetNode, QwenTE_ModelLoader, LoraLoaderModelOnly, EmptySD3LatentImage, SetNode, LatentSwitch, QwenTE_ImageInfer, CR Text, KOOK_SaveJPGImage, SeedVR2VideoUpscaler, CR Text Concatenate, ResolutionSelector, SetNode, EmptySD3LatentImage, Note, easy showAnything, CR Text Input Switch, LoadImage, PreviewImage, QwenTE_ModelLoader, Text Multiline, Fast Groups Bypasser (rgthree), easy showAnything, Text Multiline, Note, LoraLoaderModelOnly, UNETLoader, SaveImage, Note, easy imageChooser]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 403214011463433, "steps": 8}
---

# 图片生成/文生图/qwen3.8 反推、扩写整合 Z-IMAGE 最新_2093885443392757762.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen3.8 反推、扩写整合 Z-IMAGE 最新_2093885443392757762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Output → Other

**节点**（47 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LayerFilter: HDREffects`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Seed`
- `QwenTE_ImageInfer`
- `KSampler (Efficient)` ★核心
- `VAELoader`
- `ClipLoaderGGUF`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `QwenTE_ModelLoader`
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `SetNode`
- `LatentSwitch`
- `QwenTE_ImageInfer`
- `CR Text`
- `KOOK_SaveJPGImage`
- `SeedVR2VideoUpscaler`
- `CR Text Concatenate`
- `ResolutionSelector`
- `SetNode`
- `EmptySD3LatentImage`
- `Note`
- `easy showAnything`
- `CR Text Input Switch`
- `LoadImage`
- `PreviewImage`
- `QwenTE_ModelLoader`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `Text Multiline`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `Note`
- `easy imageChooser`

## 关键参数

- `seed` = `403214011463433`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（30/47）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LayerFilter: HDREffects`、`ConditioningZeroOut`、`CR Seed`、`QwenTE_ImageInfer`、`KSampler (Efficient)`、`VAELoader`、`ClipLoaderGGUF`、`CLIPTextEncode`、`QwenTE_ModelLoader`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`LatentSwitch`、`CR Text`、`KOOK_SaveJPGImage`、`SeedVR2VideoUpscaler`、`CR Text Concatenate`、`ResolutionSelector`、`CR Text Input Switch`、`LoadImage`、`Text Multiline`、`UNETLoader`、`SaveImage`、`easy imageChooser`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、SeedVR2LoadDiTModel
