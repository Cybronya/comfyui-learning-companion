---
key: 图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json
name: Qwen image 2.1 文生图_2110328458579632130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json
hash: 0582ebf38347cc4a
coverage: 0.923077
learned_at: 2026-10-21 02:54:19
nodes: [CLIPLoader, VAEDecode, UNETLoader, CLIPLoader, SaveImage, TextGenerateLTX2Prompt, easy showAnything, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, CR Text, KSampler, EmptySD3LatentImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 541145788820043, "steps": 25}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2110328458579632130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `CR Text`
- `KSampler` ★核心
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `541145788820043`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`VAEDecode`、`UNETLoader`、`SaveImage`、`TextGenerateLTX2Prompt`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`CR Text`、`KSampler`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、QwenImage21Cache、UNETLoader、TextGenerateLTX2Prompt
