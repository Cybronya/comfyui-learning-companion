---
key: 图片生成/图生图/Qwen image 2.1 人物姿势图转白模_2107830881904848898.json
name: Qwen image 2.1 人物姿势图转白模_2107830881904848898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 人物姿势图转白模_2107830881904848898.json
hash: 718d1e700c7814d4
coverage: 0.846154
learned_at: 2026-10-21 00:42:54
nodes: [LoadImage, CLIPLoader, KSampler, TextEncodeQwenImage21, LoraLoaderModelOnly, UNETLoader, VAELoader, VAEDecode, SaveImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 438983592173977, "steps": 25}
---

# 图片生成/图生图/Qwen image 2.1 人物姿势图转白模_2107830881904848898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 人物姿势图转白模_2107830881904848898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `LoadImage`
- `CLIPLoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `ImpactInt`

## 关键参数

- `seed` = `438983592173977`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`LoadImage`、`CLIPLoader`、`KSampler`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
