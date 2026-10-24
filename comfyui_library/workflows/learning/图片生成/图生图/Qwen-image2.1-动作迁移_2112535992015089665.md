---
key: 图片生成/图生图/Qwen-image2.1-动作迁移_2112535992015089665.json
name: Qwen-image2.1-动作迁移_2112535992015089665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动作迁移_2112535992015089665.json
hash: fdb882d7af0b7e5a
coverage: 0.875
learned_at: 2026-10-23 11:18:25
nodes: [VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Image Comparer (rgthree), SaveImage, LoadImage, VAELoader, UNETLoader, Int, CheckpointLoaderSimple, SDPoseKeypointExtractor, PreviewImage, BodyRatioMapperSDPoseRender, LoadImage, KSampler, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 301667708009254, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-动作迁移_2112535992015089665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动作迁移_2112535992015089665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `VAELoader`
- `UNETLoader` ★核心
- `Int`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `PreviewImage`
- `BodyRatioMapperSDPoseRender`
- `LoadImage`
- `KSampler` ★核心
- `TextEncodeQwenImage21`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`
- `seed` = `301667708009254`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`SaveImage`、`LoadImage`、`VAELoader`、`UNETLoader`、`Int`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`KSampler`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage
