---
key: 平台全量/[Krea 2 · 08.1] 风格迁移：不用 LoRA，一张参考图直接迁移视觉风格_2095752635822460930.json
name: [Krea 2 · 08.1] 风格迁移：不用 LoRA，一张参考图直接迁移视觉风格_2095752635822460930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/[Krea 2 · 08.1] 风格迁移：不用 LoRA，一张参考图直接迁移视觉风格_2095752635822460930.json
hash: 4acd81ed78855dc9
coverage: 0.535714
learned_at: 2026-11-14 01:08:49
nodes: [ConditioningZeroOut, Anything Everywhere, ImageStitch, SetNode, SetNode, VAELoader, GetNode, GetNode, LoraLoaderModelOnly, Reroute, PreviewImage, Seed (rgthree), Krea2StyleReference, UNETLoader, CLIPLoader, CLIPTextEncode, SetNode, SetNode, GetNode, KSampler, Krea2StyleTransfer, VAEDecode, PreviewImage, Krea2SizePreset, LoadImage, SaveImage, GetNode, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 353762650284629, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/[Krea 2 · 08.1] 风格迁移：不用 LoRA，一张参考图直接迁移视觉风格_2095752635822460930.json

> 来源文件 `comfyui_library/workflows/平台全量/[Krea 2 · 08.1] 风格迁移：不用 LoRA，一张参考图直接迁移视觉风格_2095752635822460930.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `ConditioningZeroOut`
- `Anything Everywhere`
- `ImageStitch`
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `PreviewImage`
- `Seed (rgthree)`
- `Krea2StyleReference`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `KSampler` ★核心
- `Krea2StyleTransfer`
- `VAEDecode` ★核心
- `PreviewImage`
- `Krea2SizePreset`
- `LoadImage`
- `SaveImage`
- `GetNode`
- `MarkdownNote`

## 关键参数

- `seed` = `353762650284629`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（15/28）

**有卡**：`ConditioningZeroOut`、`ImageStitch`、`VAELoader`、`LoraLoaderModelOnly`、`Seed (rgthree)`、`Krea2StyleReference`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`Krea2StyleTransfer`、`VAEDecode`、`Krea2SizePreset`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
