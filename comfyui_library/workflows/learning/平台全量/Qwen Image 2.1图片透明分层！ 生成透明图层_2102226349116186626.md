---
key: 平台全量/Qwen Image 2.1图片透明分层！ 生成透明图层_2102226349116186626.json
name: Qwen Image 2.1图片透明分层！ 生成透明图层_2102226349116186626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1图片透明分层！ 生成透明图层_2102226349116186626.json
hash: b7a0f5c91cf0d02d
coverage: 0.842105
learned_at: 2026-11-14 00:50:04
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, QwenImage21Cache, UNETLoader, VAELoader, SaveImage, ResolutionSelector, LoadImage, TextEncodeQwenImage21, Text Multiline, TextCombinerSix, PreviewAny, KSampler, TextGenerateLTX2Prompt, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 413839531630457, "steps": 50, "width": 1024}
---

# 平台全量/Qwen Image 2.1图片透明分层！ 生成透明图层_2102226349116186626.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1图片透明分层！ 生成透明图层_2102226349116186626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
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
- `seed` = `413839531630457`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`UNETLoader`、`VAELoader`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`TextEncodeQwenImage21`、`Text Multiline`、`TextCombinerSix`、`KSampler`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
