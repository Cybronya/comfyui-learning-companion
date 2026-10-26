---
key: 图片生成/图生图/Qwen Image 2.1 Turbo 图像编辑_2113964550642036738.json
name: Qwen Image 2.1 Turbo 图像编辑_2113964550642036738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo 图像编辑_2113964550642036738.json
hash: daad013325169074
coverage: 0.777778
learned_at: 2026-10-26 22:02:54
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, EmptyLatentImage, VAELoader, UNETLoader, CLIPLoader, ComfySwitchNode, QwenImage21Cache, ManualSigmas, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, TextEncodeQwenImage21, VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 Turbo 图像编辑_2113964550642036738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo 图像编辑_2113964550642036738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`ManualSigmas`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache、UNETLoader
