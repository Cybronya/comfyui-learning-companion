---
key: 图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json
name: Qwen Image2.1文生图_2103745897376079874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json
hash: 9570295ca1f4cff4
coverage: 0.555556
learned_at: 2026-10-06 21:37:10
nodes: [CLIPLoader, VAELoader, TextGenerate, RegexExtract, ComfySwitchNode, UNETLoader, CLIPLoader, EmptyLatentImage, VAEDecode, PreviewAny, JsonExtractString, StringCompare, KSampler, SaveImage, TextEncodeQwenImage21, Text, SaveImageAdvanced, ResolutionSelector]
patterns: []
missing: [JsonExtractString, RegexExtract, StringCompare, Text, TextGenerate, PreviewAny, SaveImageAdvanced]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
discoveries: [次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识, 次要节点 `RegexExtract` 知识库中没有该节点类型的任何知识, 次要节点 `StringCompare` 知识库中没有该节点类型的任何知识, 次要节点 `Text` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `TextGenerate`
- `RegexExtract`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `JsonExtractString`
- `StringCompare`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `Text`
- `SaveImageAdvanced`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **56%**（10/18）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`ResolutionSelector`

**缺卡**（7）：`JsonExtractString`、`RegexExtract`、`StringCompare`、`Text`、`TextGenerate`、`PreviewAny`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexExtract` 知识库中没有该节点类型的任何知识
- 次要节点 `StringCompare` 知识库中没有该节点类型的任何知识
- 次要节点 `Text` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
