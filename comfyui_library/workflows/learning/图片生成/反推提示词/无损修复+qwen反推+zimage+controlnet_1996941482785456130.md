---
key: 图片生成/反推提示词/无损修复+qwen反推+zimage+controlnet_1996941482785456130.json
name: 无损修复+qwen反推+zimage+controlnet_1996941482785456130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/无损修复+qwen反推+zimage+controlnet_1996941482785456130.json
hash: 5fc9af685d28c93d
coverage: 0.8
learned_at: 2026-10-26 01:48:18
nodes: [ModelSamplingAuraFlow, ConditioningZeroOut, EmptySD3LatentImage, SaveImage, CLIPTextEncode, KSampler, VAEDecodeTiled, QwenImageDiffsynthControlnet, LayerUtility: PurgeVRAM, PreviewImage, ImageScaleToTotalPixels, Note, AIO_Preprocessor, AIO_Preprocessor, Note, Note, AIO_Preprocessor, ImpactSwitch, UNETLoader, CLIPLoader, VAELoader, LoadImage, AILab_QwenVL, ModelPatchLoader, DyPE_FLUX]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 828357727399425, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/反推提示词/无损修复+qwen反推+zimage+controlnet_1996941482785456130.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/无损修复+qwen反推+zimage+controlnet_1996941482785456130.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `QwenImageDiffsynthControlnet`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `Note`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `Note`
- `Note`
- `AIO_Preprocessor`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `AILab_QwenVL`
- `ModelPatchLoader`
- `DyPE_FLUX`

## 关键参数

- `seed` = `828357727399425`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`SaveImage`、`CLIPTextEncode`、`KSampler`、`VAEDecodeTiled`、`QwenImageDiffsynthControlnet`、`LayerUtility: PurgeVRAM`、`ImageScaleToTotalPixels`、`AIO_Preprocessor`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`AILab_QwenVL`、`ModelPatchLoader`、`DyPE_FLUX`

**用到的条目**：KSampler、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、QwenImageDiffsynthControlnet

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
