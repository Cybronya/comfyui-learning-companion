---
key: 图片生成/文生图/Qwen2512 Vs Qwen Old Vs Z-image Turbo智能扩写对比工作流_2006323246228054018.json
name: Qwen2512 Vs Qwen Old Vs Z-image Turbo智能扩写对比工作流_2006323246228054018
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2512 Vs Qwen Old Vs Z-image Turbo智能扩写对比工作流_2006323246228054018.json
hash: bd2679de936a2d62
coverage: 0.906977
learned_at: 2026-10-19 22:00:52
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, CFGNorm, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingAuraFlow, easy showAnything, LayerUtility: PurgeVRAM, EmptySD3LatentImage, KSampler, PreviewImage, LayerUtility: PurgeVRAM, ModelSamplingAuraFlow, CFGNorm, LoraLoaderModelOnly, UNETLoader, CLIPLoader, ConditioningZeroOut, UNETLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, LayerUtility: PurgeVRAM, VAEDecode, PreviewImage, VAEDecode, VAEDecode, AddLabel, AddLabel, AddLabel, RH_LLMAPI_NODE, ImageConcatMulti, UnetLoaderGGUF, KSampler, SaveImage, easy showAnything, CR Prompt Text, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 397623419622816, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2512 Vs Qwen Old Vs Z-image Turbo智能扩写对比工作流_2006323246228054018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2512 Vs Qwen Old Vs Z-image Turbo智能扩写对比工作流_2006323246228054018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `easy showAnything`
- `LayerUtility: PurgeVRAM`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `RH_LLMAPI_NODE`
- `ImageConcatMulti`
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `SaveImage`
- `easy showAnything`
- `CR Prompt Text`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `397623419622816`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingAuraFlow`、`LayerUtility: PurgeVRAM`、`EmptySD3LatentImage`、`KSampler`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`AddLabel`、`RH_LLMAPI_NODE`、`ImageConcatMulti`、`UnetLoaderGGUF`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
