---
key: 图片生成/图生图/BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json
name: BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json
hash: 130015e8eb506cf0
coverage: 0.857143
learned_at: 2026-10-09 22:27:11
nodes: [VAELoader, VAEDecode, QwenImage21Cache, TextEncodeQwenImage21, KSampler, ComfySwitchNode, CLIPLoader, LoadImage, ResolutionSelector, CR Prompt Text, EmptyLatentImage, SaveImageAdvanced, UNETLoader, SaveImage]
patterns: []
missing: [CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102282925260759042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `SaveImage`

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

覆盖率 **86%**（12/14）

**有卡**：`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`CLIPLoader`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImageAdvanced`、`UNETLoader`、`SaveImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
