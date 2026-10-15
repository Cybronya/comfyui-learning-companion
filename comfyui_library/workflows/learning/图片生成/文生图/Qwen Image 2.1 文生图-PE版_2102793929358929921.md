---
key: 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json
name: Qwen Image 2.1 文生图-PE版_2102793929358929921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json
hash: 428ce7a9815eb97a
coverage: 0.8125
learned_at: 2026-10-15 22:26:58
nodes: [QwenImage21Cache, CLIPLoader, UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, VAELoader, easy showAnything, QwenPERewriteT8, KSampler, easy cleanGpuUsed, VAEDecode, Note, SaveImage, ResolutionSelector, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 360346436452785, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `easy showAnything`
- `QwenPERewriteT8`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Note`
- `SaveImage`
- `ResolutionSelector`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `360346436452785`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAELoader`、`QwenPERewriteT8`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
