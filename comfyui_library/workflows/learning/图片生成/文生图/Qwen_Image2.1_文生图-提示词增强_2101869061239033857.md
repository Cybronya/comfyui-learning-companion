---
key: Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json
name: Qwen_Image2.1_文生图-提示词增强_2101869061239033857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json
hash: e15da4e1cec6ce1e
coverage: 0.666667
learned_at: 2026-10-10 20:59:08
nodes: [MarkdownNote, PreviewAny, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, CLIPLoader, 忽略多组孤海, KSampler, VAEDecode, SaveImageAdvanced, SaveImage, TextGenerate, Note, ResolutionSelector, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: [忽略多组孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 407992822506572, "steps": 50, "width": 1024}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `MarkdownNote`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `忽略多组孤海`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `TextGenerate`
- `Note`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `407992822506572`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（12/18）

**有卡**：`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`TextGenerate`、`ResolutionSelector`

**缺卡**（1）：`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
