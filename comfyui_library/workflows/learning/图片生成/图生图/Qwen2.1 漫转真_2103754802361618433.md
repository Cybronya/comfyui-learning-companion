---
key: 图片生成/图生图/Qwen2.1 漫转真_2103754802361618433.json
name: Qwen2.1 漫转真_2103754802361618433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1 漫转真_2103754802361618433.json
hash: 71eabccd2fc5c5d8
coverage: 1
learned_at: 2026-10-21 00:43:36
nodes: [CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, VAEDecode, TextEncodeQwenImage21, LoraLoaderModelOnly, UNETLoader, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1032307070954891, "steps": 40}
---

# 图片生成/图生图/Qwen2.1 漫转真_2103754802361618433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1 漫转真_2103754802361618433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `1032307070954891`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
