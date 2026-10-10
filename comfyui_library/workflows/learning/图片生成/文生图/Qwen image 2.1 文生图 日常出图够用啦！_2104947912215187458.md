---
key: Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json
name: Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json
hash: 73e8bb2ea00ee9e7
coverage: 0.866667
learned_at: 2026-10-10 20:58:57
nodes: [CLIPLoader, VAELoader, VAEDecode, SaveImageAdvanced, KSampler, QwenImage21Cache, TextEncodeQwenImage21, easy showAnything, SaveImage, ResolutionSelector, TextGenerateLTX2Prompt, UNETLoader, EmptyLatentImage, CLIPLoader, CR Text]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 752481211193662, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图 日常出图够用啦！_2104947912215187458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `SaveImage`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CR Text`

## 关键参数

- `seed` = `752481211193662`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImageAdvanced`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`UNETLoader`、`EmptyLatentImage`

**缺卡**（1）：`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
