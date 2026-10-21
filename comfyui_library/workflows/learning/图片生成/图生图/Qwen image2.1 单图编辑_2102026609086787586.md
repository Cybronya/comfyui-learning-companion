---
key: 图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json
name: Qwen image2.1 单图编辑_2102026609086787586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json
hash: 4b6756eb727856c6
coverage: 0.875
learned_at: 2026-10-21 00:43:01
nodes: [LoadImage, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, VAEDecode, SaveImage, ResizeLongestToNode, UNETLoader, VAELoader, CLIPLoader, QwenImage21Cache, TextEncodeQwenImage21, RHLLMChatNode, ShowText|pysssss, CR Prompt Text, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 63986011365916, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `SaveImage`
- `ResizeLongestToNode`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `RHLLMChatNode`
- `ShowText|pysssss`
- `CR Prompt Text`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `63986011365916`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`ResizeLongestToNode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`RHLLMChatNode`、`CR Prompt Text`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
