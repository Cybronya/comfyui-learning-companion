---
key: 图片生成/图生图/qwen image2.1多图编辑工作流_2112804506063949825.json
name: qwen image2.1多图编辑工作流_2112804506063949825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image2.1多图编辑工作流_2112804506063949825.json
hash: d4fededa3634e704
coverage: 0.961538
learned_at: 2026-10-23 11:42:03
nodes: [UNETLoader, KSampler, VAEDecode, easy showAnything, JDCN_StringToList, EmptyLatentImage, SaveImageAdvanced, SaveImage, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, CLIPLoader, VAELoader, CLIPLoader, BatchImagesNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2560, "sampler_name": "euler", "scheduler": "simple", "seed": 433730799828543, "steps": 50, "width": 1440}
---

# 图片生成/图生图/qwen image2.1多图编辑工作流_2112804506063949825.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image2.1多图编辑工作流_2112804506063949825.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `JDCN_StringToList`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `433730799828543`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1440`
- `height` = `2560`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`UNETLoader`、`KSampler`、`VAEDecode`、`JDCN_StringToList`、`EmptyLatentImage`、`SaveImageAdvanced`、`SaveImage`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`BatchImagesNode`、`LoadImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
