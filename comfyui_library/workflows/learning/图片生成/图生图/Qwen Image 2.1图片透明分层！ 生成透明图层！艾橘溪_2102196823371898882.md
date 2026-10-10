---
key: 图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json
name: Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json
hash: 68ad9a3778b07c85
coverage: 0.75
learned_at: 2026-10-10 20:48:06
nodes: [MarkdownNote, CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, QwenImage21Cache, UNETLoader, VAELoader, SaveImage, ResolutionSelector, LoadImage, TextEncodeQwenImage21, Text Multiline, TextCombinerSix, PreviewAny, KSampler, TextGenerateLTX2Prompt, JjkText]
patterns: []
missing: [Text Multiline]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 636737422437890, "steps": 50, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `MarkdownNote`
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `ResolutionSelector`
- `LoadImage`
- `TextEncodeQwenImage21`
- `Text Multiline`
- `TextCombinerSix`
- `PreviewAny`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `636737422437890`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`UNETLoader`、`VAELoader`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`TextEncodeQwenImage21`、`TextCombinerSix`、`KSampler`、`TextGenerateLTX2Prompt`

**缺卡**（1）：`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
