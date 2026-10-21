---
key: 图片生成/文生图/qwen image2.1多图编辑_2101927769339940865.json
name: qwen image2.1多图编辑_2101927769339940865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image2.1多图编辑_2101927769339940865.json
hash: 004ea78147847c6e
coverage: 0.961538
learned_at: 2026-10-20 01:51:55
nodes: [UNETLoader, LoadImage, LoadImage, LoadImage, KSampler, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, TextEncodeQwenImage21, VAEDecode, EmptyLatentImage, QwenImage21Cache, TextGenerateLTX2Prompt, easy showAnything, JDCN_StringToList, CR Text, BatchImagesNode, LoadImage, SaveImageAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 983359857712260, "steps": 50, "width": 1920}
---

# 图片生成/文生图/qwen image2.1多图编辑_2101927769339940865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image2.1多图编辑_2101927769339940865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `JDCN_StringToList`
- `CR Text`
- `BatchImagesNode`
- `LoadImage`
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `seed` = `983359857712260`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`UNETLoader`、`LoadImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`VAEDecode`、`EmptyLatentImage`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`JDCN_StringToList`、`CR Text`、`BatchImagesNode`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
