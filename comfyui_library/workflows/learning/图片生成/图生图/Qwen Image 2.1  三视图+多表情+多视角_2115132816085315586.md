---
key: 图片生成/图生图/Qwen Image 2.1  三视图+多表情+多视角_2115132816085315586.json
name: Qwen Image 2.1  三视图+多表情+多视角_2115132816085315586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1  三视图+多表情+多视角_2115132816085315586.json
hash: 1ac16638547646b5
coverage: 0.703704
learned_at: 2026-10-30 17:50:49
nodes: [VAEDecode, VAEDecode, UNETLoader, CLIPLoader, JjkText, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, ImageStitch, ImageStitch, KSampler, VAEDecode, KSampler, KSampler, ComfySwitchNode, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, JjkText, JjkText, SaveImage, EmptyLatentImage, ResolutionSelector, PrimitiveFloat, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 286793317872171, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1  三视图+多表情+多视角_2115132816085315586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1  三视图+多表情+多视角_2115132816085315586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ImageStitch`
- `ImageStitch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `JjkText`
- `JjkText`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `286793317872171`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageStitch`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`ResolutionSelector`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
