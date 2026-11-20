---
key: 平台全量/QWen2.1文生图基础版_2121106526541803522.json
name: QWen2.1文生图基础版_2121106526541803522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/QWen2.1文生图基础版_2121106526541803522.json
hash: 02eb59996bde2066
coverage: 1
learned_at: 2026-11-14 00:49:04
nodes: [EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, VAEDecode, SaveImage, TextEncodeQwenImage21, CR Prompt Text, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 914221617184798, "steps": 25, "width": 1536}
---

# 平台全量/QWen2.1文生图基础版_2121106526541803522.json

> 来源文件 `comfyui_library/workflows/平台全量/QWen2.1文生图基础版_2121106526541803522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（9 个）：
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `KSampler` ★核心

## 关键参数

- `width` = `1536`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `914221617184798`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`CR Prompt Text`、`KSampler`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
