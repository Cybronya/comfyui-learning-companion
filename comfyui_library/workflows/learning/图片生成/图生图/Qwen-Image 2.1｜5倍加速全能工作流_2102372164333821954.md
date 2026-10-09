---
key: 图片生成/图生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json
name: Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json
hash: 955c78a9aadc2e71
coverage: 0.68
learned_at: 2026-10-09 22:19:27
nodes: [EmptyLatentImage, VAEDecode, KSampler, QwenImage21Cache, LoadImage, DrawMaskOnImage, LoadImage, easy int, LoadImage, ComfySwitchNode, CR Seed, ResolutionSelector, MarkdownNote, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, TextGenerateLTX2Prompt, easy showAnything, TextEncodeQwenImage21, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: [easy int, CR Seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 8, "width": 1024}
discoveries: [次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102372164333821954.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
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
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
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

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（17/25）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`DrawMaskOnImage`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`SaveImage`

**缺卡**（2）：`easy int`、`CR Seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
