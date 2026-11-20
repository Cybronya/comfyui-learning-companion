---
key: 平台全量/09-image2.1文生图系列图_2119365576085827586.json
name: 09-image2.1文生图系列图_2119365576085827586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/09-image2.1文生图系列图_2119365576085827586.json
hash: 992373c963ec631f
coverage: 0.909091
learned_at: 2026-11-14 00:10:02
nodes: [CLIPLoader, UNETLoader, KSampler, VAELoader, SaveImage, TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, VAEDecode, PrimitiveStringMultiline, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 869732124356504, "steps": 30, "width": 1024}
---

# 平台全量/09-image2.1文生图系列图_2119365576085827586.json

> 来源文件 `comfyui_library/workflows/平台全量/09-image2.1文生图系列图_2119365576085827586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAELoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `869732124356504`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAELoader`、`SaveImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
