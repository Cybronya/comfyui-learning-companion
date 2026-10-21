---
key: 图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json
name: MJ风格工作流V2.0_2112169962583445506
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json
hash: 304dce5781fb1371
coverage: 0.913043
learned_at: 2026-10-21 02:53:33
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), CLIPLoader, EmptyLatentImage, CLIPTextEncode, ConditioningZeroOut, VAELoader, VAEDecode, SetNode, ResolutionSelector, UNETLoader, MarkdownNote, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ConditioningKrea2Rebalance, CR Prompt Text, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 602929029479328, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `VAEDecode` ★核心
- `SetNode`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MarkdownNote`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningKrea2Rebalance`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `602929029479328`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`Label (rgthree)`、`CLIPLoader`、`EmptyLatentImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAELoader`、`VAEDecode`、`ResolutionSelector`、`UNETLoader`、`SaveImage`、`LoraLoaderModelOnly`、`ConditioningKrea2Rebalance`、`CR Prompt Text`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
