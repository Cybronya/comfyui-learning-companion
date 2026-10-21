---
key: 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112076292018495489.json
name: Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112076292018495489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112076292018495489.json
hash: 65a19115bf21385c
coverage: 0.666667
learned_at: 2026-10-21 02:54:10
nodes: [MarkdownNote, SaveImage, QwenImage21_T2IPromptRewrite, easy showAnything, easy showAnything, PreviewImage, SaveImageAdvanced, VAEDecode, KSampler, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, MarkdownNote, CLIPLoader, UNETLoader, RH_QwenImagePromptEnhancer, ComfySwitchNode, PrimitiveBoolean, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112076292018495489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112076292018495489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `MarkdownNote`
- `SaveImage`
- `QwenImage21_T2IPromptRewrite`
- `easy showAnything`
- `easy showAnything`
- `PreviewImage`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `RH_QwenImagePromptEnhancer`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（14/21）

**有卡**：`SaveImage`、`QwenImage21_T2IPromptRewrite`、`SaveImageAdvanced`、`VAEDecode`、`KSampler`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`CLIPLoader`、`UNETLoader`、`RH_QwenImagePromptEnhancer`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
