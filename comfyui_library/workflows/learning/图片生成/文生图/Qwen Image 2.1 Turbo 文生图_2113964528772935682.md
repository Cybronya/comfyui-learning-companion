---
key: 图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json
name: Qwen Image 2.1 Turbo 文生图_2113964528772935682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json
hash: d4d32d73756be50e
coverage: 0.823529
learned_at: 2026-10-26 22:08:37
nodes: [MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, ManualSigmas, QwenImage21Cache, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, CFGGuider, EmptyLatentImage, ResolutionSelector, MarkdownNote, TextEncodeQwenImage21, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ManualSigmas`
- `QwenImage21Cache`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ManualSigmas`、`QwenImage21Cache`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`CFGGuider`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache、UNETLoader
