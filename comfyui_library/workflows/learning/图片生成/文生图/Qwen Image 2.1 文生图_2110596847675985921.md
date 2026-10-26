---
key: 图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json
name: Qwen Image 2.1 文生图_2110596847675985921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json
hash: f7b5b5e102d7ac7d
coverage: 0.7
learned_at: 2026-10-26 22:08:39
nodes: [PrimitiveStringMultiline, QwenImage21Cache, VAEDecode, CLIPLoader, PrimitiveStringMultiline, CLIPLoader, VAELoader, UNETLoader, PreviewAny, ComfySwitchNode, PrimitiveStringMultiline, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, KSampler, TextGenerate, PrimitiveBoolean, SaveText, SaveImageAdvanced, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1051178816031701, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `PreviewAny`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `KSampler` ★核心
- `TextGenerate`
- `PrimitiveBoolean`
- `SaveText`
- `SaveImageAdvanced`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1051178816031701`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（14/20）

**有卡**：`QwenImage21Cache`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`KSampler`、`TextGenerate`、`PrimitiveBoolean`、`SaveText`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
