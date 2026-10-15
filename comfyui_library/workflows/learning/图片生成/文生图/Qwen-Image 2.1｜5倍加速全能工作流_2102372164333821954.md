---
key: 图片生成/文生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json
name: Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json
hash: 0b5a6d94d20916ad
coverage: 0.68
learned_at: 2026-10-10 21:27:53
nodes: [EmptyLatentImage, VAEDecode, KSampler, QwenImage21Cache, LoadImage, DrawMaskOnImage, LoadImage, easy int, LoadImage, ComfySwitchNode, CR Seed, ResolutionSelector, MarkdownNote, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, TextGenerateLTX2Prompt, easy showAnything, TextEncodeQwenImage21, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: [easy int, CR Seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 8, "width": 1024}
discoveries: [次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json`

## 结构

**节点**（25 个）：
- `EmptyLatentImage`
- `VAEDecode`
- `KSampler`
- `QwenImage21Cache`
- `LoadImage`
- `DrawMaskOnImage`
- `LoadImage`
- `easy int`
- `LoadImage`
- `ComfySwitchNode`
- `CR Seed`
- `ResolutionSelector`
- `MarkdownNote`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1`
- `steps` = `8`
- `width` = `1024`

## 知识

覆盖率 **68%**（17/25）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`DrawMaskOnImage`、`easy int`、`ComfySwitchNode`、`CR Seed`、`ResolutionSelector`、`MarkdownNote`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`

**缺卡**（2）：`easy int`、`CR Seed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
