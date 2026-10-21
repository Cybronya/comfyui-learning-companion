---
key: 图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json
name: Qwen+image+2.1图片编辑.九宫格_2101870838822817793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json
hash: dbd70f79e0cbcae6
coverage: 0.928571
learned_at: 2026-10-21 00:43:04
nodes: [VAELoader, VAEDecode, QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, KSampler, SaveImage, UNETLoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoadImage, SaveImageAdvanced, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `SaveImageAdvanced`
- `CR Prompt Text`

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

覆盖率 **93%**（13/14）

**有卡**：`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`CLIPLoader`、`KSampler`、`SaveImage`、`UNETLoader`、`ResolutionSelector`、`EmptyLatentImage`、`LoadImage`、`SaveImageAdvanced`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
