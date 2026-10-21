---
key: 图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json
name: BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json
hash: 6139e6130ad6540e
coverage: 0.875
learned_at: 2026-10-21 00:38:46
nodes: [VAELoader, VAEDecode, QwenImage21Cache, TextEncodeQwenImage21, KSampler, ComfySwitchNode, CLIPLoader, LoadImage, ResolutionSelector, EmptyLatentImage, SaveImageAdvanced, UNETLoader, SaveImage, CR Prompt Text, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `SaveImage`
- `CR Prompt Text`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`CLIPLoader`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImageAdvanced`、`UNETLoader`、`SaveImage`、`CR Prompt Text`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
