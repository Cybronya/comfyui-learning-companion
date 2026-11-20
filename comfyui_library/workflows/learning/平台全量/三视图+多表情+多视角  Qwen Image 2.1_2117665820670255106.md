---
key: 平台全量/三视图+多表情+多视角  Qwen Image 2.1_2117665820670255106.json
name: 三视图+多表情+多视角  Qwen Image 2.1_2117665820670255106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/三视图+多表情+多视角  Qwen Image 2.1_2117665820670255106.json
hash: 8e98a00dce0c9ca4
coverage: 0.633333
learned_at: 2026-11-14 01:33:09
nodes: [VAEDecode, VAEDecode, UNETLoader, CLIPLoader, JjkText, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, ImageStitch, ImageStitch, KSampler, VAEDecode, KSampler, KSampler, ComfySwitchNode, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, JjkText, JjkText, SaveImage, EmptyLatentImage, ResolutionSelector, PrimitiveFloat, LoadImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 1066785694428613, "steps": 25, "width": 1024}
---

# 平台全量/三视图+多表情+多视角  Qwen Image 2.1_2117665820670255106.json

> 来源文件 `comfyui_library/workflows/平台全量/三视图+多表情+多视角  Qwen Image 2.1_2117665820670255106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
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
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`

## 关键参数

- `seed` = `1066785694428613`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（19/30）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageStitch`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`ResolutionSelector`、`LoadImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
