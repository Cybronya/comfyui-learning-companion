---
key: 图片生成/图生图/Qwen2.1四视图生成器_2101145681154101249.json
name: Qwen2.1四视图生成器_2101145681154101249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1四视图生成器_2101145681154101249.json
hash: 351021f8183f04c6
coverage: 0.8
learned_at: 2026-10-21 00:43:37
nodes: [UNETLoader, CLIPLoader, VAELoader, MarkdownNote, Note, QwenImage21Cache, KSampler, LoadImage, LoadImage, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, ResolutionSelector, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 8152683795449, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen2.1四视图生成器_2101145681154101249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1四视图生成器_2101145681154101249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `Note`
- `QwenImage21Cache`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `8152683795449`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`LoadImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
