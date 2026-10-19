---
key: 图片生成/文生图/Z image的Controlnet的Depth_1996388981573042178.json
name: Z image的Controlnet的Depth_1996388981573042178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z image的Controlnet的Depth_1996388981573042178.json
hash: 61858f75f0ac5084
coverage: 1
learned_at: 2026-10-19 21:32:47
nodes: [CLIPLoader, UNETLoader, KSampler, ConditioningZeroOut, ModelSamplingAuraFlow, VAELoader, ModelPatchLoader, QwenImageDiffsynthControlnet, CLIPTextEncode, LoadImage, VAEDecode, SaveImage, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 219058592691350, "steps": 10, "width": 1824}
---

# 图片生成/文生图/Z image的Controlnet的Depth_1996388981573042178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z image的Controlnet的Depth_1996388981573042178.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `219058592691350`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1824`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAELoader`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`CLIPTextEncode`、`LoadImage`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
