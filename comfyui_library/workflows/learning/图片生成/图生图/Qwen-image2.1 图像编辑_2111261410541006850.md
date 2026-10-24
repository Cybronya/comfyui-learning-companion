---
key: 图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json
name: Qwen-image2.1 图像编辑_2111261410541006850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json
hash: 1a3653fe8e15ed6f
coverage: 0.894737
learned_at: 2026-10-23 11:18:20
nodes: [CLIPLoader, CLIPLoader, VAELoader, UNETLoader, ComfySwitchNode, EmptyLatentImage, KSampler, VAEDecode, SaveImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, CR Prompt Text, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 757814948396470, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `757814948396470`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`LoadImage`、`ResolutionSelector`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
