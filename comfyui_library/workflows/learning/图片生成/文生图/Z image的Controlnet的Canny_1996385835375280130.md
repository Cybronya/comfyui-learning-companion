---
key: 图片生成/文生图/Z image的Controlnet的Canny_1996385835375280130.json
name: Z image的Controlnet的Canny_1996385835375280130
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z image的Controlnet的Canny_1996385835375280130.json
hash: aff5058391b5b24f
coverage: 1
learned_at: 2026-10-19 21:32:46
nodes: [CLIPLoader, UNETLoader, KSampler, ConditioningZeroOut, ModelSamplingAuraFlow, VAELoader, ModelPatchLoader, QwenImageDiffsynthControlnet, EmptyLatentImage, LoadImage, CLIPTextEncode, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1066131788985918, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Z image的Controlnet的Canny_1996385835375280130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z image的Controlnet的Canny_1996385835375280130.json`

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
- `EmptyLatentImage` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1066131788985918`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAELoader`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`EmptyLatentImage`、`LoadImage`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
