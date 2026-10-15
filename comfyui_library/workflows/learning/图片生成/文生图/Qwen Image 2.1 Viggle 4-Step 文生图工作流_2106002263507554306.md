---
key: 图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json
name: Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json
hash: 12e15ebeb6f75497
coverage: 0.928571
learned_at: 2026-10-10 20:58:51
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, ResolutionSelector, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, VAEDecode, SaveImage, QwenImage21Cache, ModelSamplingFlux, ModelAttentionBackend]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 314159268, "steps": 25, "width": 2048}
---

# 图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json`

## 结构

**节点**（14 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `MarkdownNote`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `SaveImage`
- `QwenImage21Cache`
- `ModelSamplingFlux`
- `ModelAttentionBackend`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `2048`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `314159268`
- `steps` = `25`
- `width` = `2048`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`MarkdownNote`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`ModelSamplingFlux`
