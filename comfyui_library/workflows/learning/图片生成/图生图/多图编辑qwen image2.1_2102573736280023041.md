---
key: 图片生成/图生图/多图编辑qwen image2.1_2102573736280023041.json
name: 多图编辑qwen image2.1_2102573736280023041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑qwen image2.1_2102573736280023041.json
hash: 3f0688b9880d6af8
coverage: 0.962963
learned_at: 2026-10-15 22:25:50
nodes: [UNETLoader, KSampler, CLIPLoader, VAELoader, CLIPLoader, VAEDecode, easy showAnything, BatchImagesNode, JDCN_StringToList, EmptyLatentImage, SaveImageAdvanced, SaveImage, QwenImage21Cache, TextGenerateLTX2Prompt, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2560, "sampler_name": "euler", "scheduler": "simple", "seed": 477611766384635, "steps": 50, "width": 1440}
---

# 图片生成/图生图/多图编辑qwen image2.1_2102573736280023041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑qwen image2.1_2102573736280023041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `easy showAnything`
- `BatchImagesNode`
- `JDCN_StringToList`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `TextEncodeQwenImage21`
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

- `seed` = `477611766384635`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1440`
- `height` = `2560`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`UNETLoader`、`KSampler`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`BatchImagesNode`、`JDCN_StringToList`、`EmptyLatentImage`、`SaveImageAdvanced`、`SaveImage`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`LoadImage`、`TextEncodeQwenImage21`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
