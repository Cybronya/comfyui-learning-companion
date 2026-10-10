---
key: 图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json
name: Qwen Image 2.1去除ai感_2102264547909390337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json
hash: b72d6332e2dd1251
coverage: 0.815789
learned_at: 2026-10-10 20:48:06
nodes: [CLIPLoader, VAELoader, LoadImage, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAEDecode, ImageStitch, KSampler, SaveImage, TextEncodeQwenImage21, LoraLoaderModelOnly, MarkdownNote, Note, CLIPLoader, VAELoader, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAEDecode, ImageStitch, KSampler, SaveImage, LoraLoaderModelOnly, UNETLoader, SaveImage, UNETLoader, ComfySwitchNode, ComfySwitchNode, MarkdownNote, LoadImage, TextEncodeQwenImage21, SaveImage, SaveImage, SaveImage, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 651972595901419, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `ResolutionSelector`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MarkdownNote`
- `LoadImage`
- `TextEncodeQwenImage21`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PrimitiveBoolean`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `651972595901419`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`ResolutionSelector`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`ImageStitch`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
