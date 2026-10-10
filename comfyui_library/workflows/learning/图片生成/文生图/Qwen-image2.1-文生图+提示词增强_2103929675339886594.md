---
key: Qwen-image2.1-文生图+提示词增强_2103929675339886594.json
name: Qwen-image2.1-文生图+提示词增强_2103929675339886594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json
hash: a992076d561d6562
coverage: 0.73913
learned_at: 2026-10-10 20:59:05
nodes: [PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, StringConcatenate, TextGenerate, SeedNode, JsonExtractString, ComfySwitchNode, PreviewAny, PrimitiveBoolean, VAELoader, UNETLoader, CLIPLoader, ModelAttentionBackend, TextEncodeQwenImage21, VAEDecode, SeedNode, PrimitiveStringMultiline, EmptyLatentImage, LoraLoaderModelOnly, KSampler, SaveImageAdvanced, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1062834340239450, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen-image2.1-文生图+提示词增强_2103929675339886594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `StringConcatenate`
- `TextGenerate`
- `SeedNode`
- `JsonExtractString`
- `ComfySwitchNode`
- `PreviewAny`
- `PrimitiveBoolean`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SeedNode`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1062834340239450`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`StringConcatenate`、`TextGenerate`、`SeedNode`、`JsonExtractString`、`PrimitiveBoolean`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`ModelAttentionBackend`、`TextEncodeQwenImage21`、`VAEDecode`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`KSampler`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
