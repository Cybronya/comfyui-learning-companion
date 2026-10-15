---
key: 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102152565902368769.json
name: 开源最强图片模型 Qwen-image2.1  指定抠图模式_2102152565902368769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102152565902368769.json
hash: a845d0a036040c9e
coverage: 0.8
learned_at: 2026-10-15 22:25:52
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, 孤海注释, MarkdownNote, Note Plus (mtb), LoadImage, VAEDecode, CR Text, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1092705340770395, "steps": 25, "width": 1024}
---

# 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102152565902368769.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102152565902368769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `孤海注释`
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImage`
- `VAEDecode` ★核心
- `CR Text`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1092705340770395`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`Note Plus (mtb)`、`LoadImage`、`VAEDecode`、`CR Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
