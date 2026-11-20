---
key: 平台全量/QwenImage2.1东方神话 T2I_2118695548684431362.json
name: QwenImage2.1东方神话 T2I_2118695548684431362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/QwenImage2.1东方神话 T2I_2118695548684431362.json
hash: 3d3afb07e69584d5
coverage: 0.777778
learned_at: 2026-11-14 00:53:23
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, TextGenerate, CLIPLoader, JsonExtractString, PrimitiveStringMultiline, PrimitiveStringMultiline, Any Switch (rgthree), easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 614429537913182, "steps": 30, "width": 1088}
---

# 平台全量/QwenImage2.1东方神话 T2I_2118695548684431362.json

> 来源文件 `comfyui_library/workflows/平台全量/QwenImage2.1东方神话 T2I_2118695548684431362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextGenerate`
- `CLIPLoader`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Any Switch (rgthree)`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

## 关键参数

- `width` = `1088`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `614429537913182`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`TextGenerate`、`JsonExtractString`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、UNETLoader
