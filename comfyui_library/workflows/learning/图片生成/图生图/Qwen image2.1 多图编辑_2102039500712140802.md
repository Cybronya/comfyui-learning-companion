---
key: 图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json
name: Qwen image2.1 多图编辑_2102039500712140802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json
hash: 272017cbc2e62f05
coverage: 0.956522
learned_at: 2026-10-21 00:43:02
nodes: [EmptyLatentImage, VAEDecode, SaveImage, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, KSampler, ResolutionSelector, VAELoader, CLIPLoader, QwenImage21Cache, UNETLoader, RHLLMChatNode, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 114791873678654, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ResolutionSelector`
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `RHLLMChatNode`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `114791873678654`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`、`VAELoader`、`CLIPLoader`、`QwenImage21Cache`、`UNETLoader`、`RHLLMChatNode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
