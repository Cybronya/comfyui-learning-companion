---
key: 图片生成/图生图/Qwen-image2.1-动作迁移2_2107475110847401986.json
name: Qwen-image2.1-动作迁移2_2107475110847401986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动作迁移2_2107475110847401986.json
hash: 63d068cc9a54bb63
coverage: 0.916667
learned_at: 2026-10-21 00:43:25
nodes: [CLIPLoader, VAELoader, UNETLoader, PreviewImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, LoraLoaderModelOnly, KSampler, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 670515868032100, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-动作迁移2_2107475110847401986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动作迁移2_2107475110847401986.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `670515868032100`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
