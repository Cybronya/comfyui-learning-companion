---
key: 图片生成/文生图/QWen2.1文生图_2102420206202216450.json
name: QWen2.1文生图_2102420206202216450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWen2.1文生图_2102420206202216450.json
hash: 78a25c2979e0d2b1
coverage: 0.615385
learned_at: 2026-10-06 22:39:02
nodes: [KSampler, QwenImage21Cache, MarkdownNote, MarkdownNote, EmptyLatentImage, TextEncodeQwenImage21, TextGenerate, ComfySwitchNode, PreviewAny, CLIPLoader, PrimitiveStringMultiline, CR Prompt Text, UNETLoader, UNETLoader, MarkdownNote, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, CLIPLoader, CLIPLoader, VAELoader, ResolutionSelector, PrimitiveBoolean, PrimitiveInt, VAEDecode, SaveImage]
patterns: []
missing: [CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/QWen2.1文生图_2102420206202216450.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWen2.1文生图_2102420206202216450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `KSampler` ★核心
- `QwenImage21Cache`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextGenerate`
- `ComfySwitchNode`
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（16/26）

**有卡**：`KSampler`、`QwenImage21Cache`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerate`、`CLIPLoader`、`UNETLoader`、`PrimitiveBoolean`、`VAELoader`、`ResolutionSelector`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
