---
key: 图片生成/图生图/Qwen-image2.1-图像角色多角度lora_2111388449549930497.json
name: Qwen-image2.1-图像角色多角度lora_2111388449549930497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像角色多角度lora_2111388449549930497.json
hash: 37e926ed8ef51e5c
coverage: 0.846154
learned_at: 2026-10-23 11:18:26
nodes: [CLIPLoader, VAELoader, UNETLoader, KSampler, VAEDecode, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Int, SaveImage, LoraLoaderModelOnly, Note, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1038837703577203, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-图像角色多角度lora_2111388449549930497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像角色多角度lora_2111388449549930497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Int`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `1038837703577203`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Int`、`SaveImage`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
