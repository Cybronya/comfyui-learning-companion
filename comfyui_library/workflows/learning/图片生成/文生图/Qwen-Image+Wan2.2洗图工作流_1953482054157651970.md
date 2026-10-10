---
key: Qwen-Image+Wan2.2洗图工作流_1953482054157651970.json
name: Qwen-Image+Wan2.2洗图工作流_1953482054157651970
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image+Wan2.2洗图工作流_1953482054157651970.json
hash: 96176adde43ec733
coverage: 0.941176
learned_at: 2026-10-10 20:58:58
nodes: [VAELoader, CLIPLoader, SaveImage, UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, String Literal, VAEDecode, VAELoader, LoraLoaderModelOnly, PreviewBridge, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, SaveImage, Seed, ShowText|pysssss, CLIPTextEncode, ConditioningZeroOut, VAEEncode, EmptyLatentImage, DeepTranslatorTextNode, CLIPTextEncode, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, KSampler, KSampler, KSampler]
patterns: [text_to_image]
missing: [String Literal]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 217088130541187, "steps": 5, "width": 768}
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen-Image+Wan2.2洗图工作流_1953482054157651970.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image+Wan2.2洗图工作流_1953482054157651970.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `String Literal`
- `VAEDecode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PreviewBridge`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `Seed`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `EmptyLatentImage` ★核心
- `DeepTranslatorTextNode`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `217088130541187`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.1`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`VAELoader`、`CLIPLoader`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAEDecode`、`PreviewBridge`、`ModelSamplingSD3`、`Seed`、`ConditioningZeroOut`、`VAEEncode`、`EmptyLatentImage`、`DeepTranslatorTextNode`、`ModelSamplingAuraFlow`、`KSampler`

**缺卡**（1）：`String Literal`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
