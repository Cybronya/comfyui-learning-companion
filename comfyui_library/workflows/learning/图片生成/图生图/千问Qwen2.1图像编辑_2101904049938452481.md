---
key: 图片生成/图生图/千问Qwen2.1图像编辑_2101904049938452481.json
name: 千问Qwen2.1图像编辑_2101904049938452481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问Qwen2.1图像编辑_2101904049938452481.json
hash: ecbcbdf6016958d9
coverage: 0.857143
learned_at: 2026-10-21 00:50:37
nodes: [VAELoader, EmptyLatentImage, KSampler, QwenImage21Cache, UNETLoader, CLIPLoader, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, Text, LoadImage, MarkdownNote, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 822586715506996, "steps": 25, "width": 1024}
---

# 图片生成/图生图/千问Qwen2.1图像编辑_2101904049938452481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问Qwen2.1图像编辑_2101904049938452481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `Text`
- `LoadImage`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `822586715506996`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`Text`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
