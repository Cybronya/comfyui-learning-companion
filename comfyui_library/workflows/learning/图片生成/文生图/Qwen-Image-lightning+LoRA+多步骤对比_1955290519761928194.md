---
key: 图片生成/文生图/Qwen-Image-lightning+LoRA+多步骤对比_1955290519761928194.json
name: Qwen-Image-lightning+LoRA+多步骤对比_1955290519761928194.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-lightning+LoRA+多步骤对比_1955290519761928194.json
hash: 27408ef8bf5a3837
coverage: 0.857143
learned_at: 2026-10-07 23:24:21
nodes: [CLIPLoader, ConditioningZeroOut, KSampler, KSampler, ModelSamplingAuraFlow, UNETLoader, DF_Get_image_size, ConditioningZeroOut, KSampler, ConditioningZeroOut, VAELoader, EmptySD3LatentImage, PreviewImage, VAEDecode, SaveImage, SaveImage, SaveImage, LayerUtility: ImageReelComposit, SaveImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPTextEncode, ConditioningZeroOut, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, LoraLoaderModelOnly, VAEDecode, VAEDecode, VAEDecode, LayerUtility: ImageReel, ModelSamplingAuraFlow, Note, Note]
patterns: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 594059080621576, "steps": 8}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-lightning+LoRA+多步骤对比_1955290519761928194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1955290519761928194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `DF_Get_image_size`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `EmptySD3LatentImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `ModelSamplingAuraFlow`
- `Note`
- `Note`

## 关键参数

- `seed` = `594059080621576`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`KSampler`、`ModelSamplingAuraFlow`、`UNETLoader`、`DF_Get_image_size`、`VAELoader`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（2）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
