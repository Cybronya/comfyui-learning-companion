---
key: 图片生成/图生图/Qwen-image2.1-动作迁移_2102372877952704514.json
name: Qwen-image2.1-动作迁移_2102372877952704514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动作迁移_2102372877952704514.json
hash: 474f973873ac8a79
coverage: 0.8
learned_at: 2026-10-10 20:48:09
nodes: [SaveImage, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, VAEDecode, LoadImage, LoadImage, PreviewImage, KSampler, BodyRatioMapperSDPoseRender, CheckpointLoaderSimple, SDPoseKeypointExtractor, PreviewImage, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
parameters: {"cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 275058316679795, "steps": 25}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen-image2.1-动作迁移_2102372877952704514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动作迁移_2102372877952704514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `KSampler` ★核心
- `BodyRatioMapperSDPoseRender`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `PreviewImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `275058316679795`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`VAEDecode`、`LoadImage`、`KSampler`、`BodyRatioMapperSDPoseRender`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
