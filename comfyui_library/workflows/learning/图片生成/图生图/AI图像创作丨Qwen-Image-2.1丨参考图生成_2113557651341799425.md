---
key: 图片生成/图生图/AI图像创作丨Qwen-Image-2.1丨参考图生成_2113557651341799425.json
name: AI图像创作丨Qwen-Image-2.1丨参考图生成_2113557651341799425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI图像创作丨Qwen-Image-2.1丨参考图生成_2113557651341799425.json
hash: 4fae184f067589d3
coverage: 0.962963
learned_at: 2026-10-26 22:01:19
nodes: [UNETLoader, KSampler, CLIPLoader, VAELoader, CLIPLoader, VAEDecode, easy showAnything, BatchImagesNode, JDCN_StringToList, EmptyLatentImage, SaveImageAdvanced, SaveImage, QwenImage21Cache, TextGenerateLTX2Prompt, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2560, "sampler_name": "euler", "scheduler": "simple", "seed": 455908098086932, "steps": 50, "width": 1440}
---

# 图片生成/图生图/AI图像创作丨Qwen-Image-2.1丨参考图生成_2113557651341799425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI图像创作丨Qwen-Image-2.1丨参考图生成_2113557651341799425.json`

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

- `seed` = `455908098086932`
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
