---
key: 图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json
name: Qwen Image 2.1 Turbo：文生图_2110484342584733697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json
hash: 22b50e109242c747
coverage: 0.708333
learned_at: 2026-10-21 02:54:05
nodes: [ResolutionSelector, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, PreviewAny, CLIPLoader, PrimitiveStringMultiline, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, CFGGuider, QwenImage21Cache, SaveImage, SaveImageAdvanced, ComfySwitchNode, TextGenerate, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `QwenImage21Cache`
- `SaveImage`
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `TextGenerate`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`ResolutionSelector`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`ManualSigmas`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`QwenImage21Cache`、`SaveImage`、`SaveImageAdvanced`、`TextGenerate`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache、UNETLoader
