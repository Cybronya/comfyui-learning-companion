---
key: 图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json
name: Qwen Image 2.1 PE 文生图_2102401855983808514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json
hash: eded267f4a93f25e
coverage: 0.8125
learned_at: 2026-10-15 22:25:01
nodes: [CLIPLoader, Note, UNETLoader, VAELoader, QwenImage21Cache, KSampler, VAEDecode, easy cleanGpuUsed, EmptyLatentImage, SaveImage, easy showAnything, QwenPERewriteT8, CR Prompt Text, TextEncodeQwenImage21, ComfySwitchNode, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `Note`
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `easy showAnything`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ResolutionSelector`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`EmptyLatentImage`、`SaveImage`、`QwenPERewriteT8`、`CR Prompt Text`、`TextEncodeQwenImage21`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
