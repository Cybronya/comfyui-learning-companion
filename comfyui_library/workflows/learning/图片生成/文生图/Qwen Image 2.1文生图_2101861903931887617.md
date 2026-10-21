---
key: 图片生成/文生图/Qwen Image 2.1文生图_2101861903931887617.json
name: Qwen Image 2.1文生图_2101861903931887617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图_2101861903931887617.json
hash: e2518d8564e68fda
coverage: 1
learned_at: 2026-10-20 01:50:58
nodes: [VAEDecode, KSampler, TextEncodeQwenImage21, CLIPLoader, VAELoader, PathchSageAttentionKJ, QwenImage21Cache, UNETLoader, CR Text, SaveImage, EmptyLatentImage, ResolutionSelector, Int]
patterns: []
missing: []
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 946260776034835, "steps": 30, "width": 864}
---

# 图片生成/文生图/Qwen Image 2.1文生图_2101861903931887617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图_2101861903931887617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CR Text`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `Int`

## 关键参数

- `seed` = `946260776034835`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `864`
- `height` = `1536`
- `batch_size` = `4`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`VAEDecode`、`KSampler`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`UNETLoader`、`CR Text`、`SaveImage`、`EmptyLatentImage`、`ResolutionSelector`、`Int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
