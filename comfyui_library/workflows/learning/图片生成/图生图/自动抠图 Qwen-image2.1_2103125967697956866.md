---
key: 图片生成/图生图/自动抠图 Qwen-image2.1_2103125967697956866.json
name: 自动抠图 Qwen-image2.1_2103125967697956866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/自动抠图 Qwen-image2.1_2103125967697956866.json
hash: 486aacd09e6b0c0e
coverage: 0.882353
learned_at: 2026-10-21 00:56:01
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, VAEDecode, SaveImage, 孤海注释, MultiTextConcatenate, CR Text, MultiTextConcatenate, CR Text, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 232705038565607, "steps": 25, "width": 1024}
---

# 图片生成/图生图/自动抠图 Qwen-image2.1_2103125967697956866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/自动抠图 Qwen-image2.1_2103125967697956866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `孤海注释`
- `MultiTextConcatenate`
- `CR Text`
- `MultiTextConcatenate`
- `CR Text`
- `CR Text`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `232705038565607`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`MultiTextConcatenate`、`CR Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
