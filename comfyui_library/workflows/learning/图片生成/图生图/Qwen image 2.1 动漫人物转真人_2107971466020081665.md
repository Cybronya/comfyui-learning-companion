---
key: 图片生成/图生图/Qwen image 2.1 动漫人物转真人_2107971466020081665.json
name: Qwen image 2.1 动漫人物转真人_2107971466020081665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 动漫人物转真人_2107971466020081665.json
hash: c36fcdfa8e159077
coverage: 0.846154
learned_at: 2026-10-21 00:42:55
nodes: [UNETLoader, VAELoader, LoraLoaderModelOnly, CLIPLoader, TextEncodeQwenImage21, KSampler, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, ImpactInt, Image Comparer (rgthree), LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 805995034959772, "steps": 25}
---

# 图片生成/图生图/Qwen image 2.1 动漫人物转真人_2107971466020081665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 动漫人物转真人_2107971466020081665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `ImpactInt`
- `Image Comparer (rgthree)`
- `LoadImage`

## 关键参数

- `seed` = `805995034959772`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
