---
key: 图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json
name: Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json
hash: 0ab5229d2adbd27a
coverage: 0.833333
learned_at: 2026-10-21 00:43:01
nodes: [孤海注释, JoinStrings, MarkdownNote, ResolutionSelector, PrimitiveBoolean, ComfySwitchNode, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, TextEncodeQwenImage21, QwenImage21Cache, VAEDecode, EmptyLatentImage, BatchImagesNode, easy positive, TextGenerate, ShowText|pysssss, SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, easy positive, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 235134537213024, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1漫转真工作流（AIGC特异点）_2104062048404590594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `孤海注释`
- `JoinStrings`
- `MarkdownNote`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `BatchImagesNode`
- `easy positive`
- `TextGenerate`
- `ShowText|pysssss`
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy positive`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `235134537213024`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`JoinStrings`、`ResolutionSelector`、`PrimitiveBoolean`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`EmptyLatentImage`、`BatchImagesNode`、`easy positive`、`TextGenerate`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
