---
key: 图片生成/图生图/Qwen_image_2.1-图生图-角色四视图-V1.1_2114880341025574914.json
name: Qwen_image_2.1-图生图-角色四视图-V1.1_2114880341025574914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1-图生图-角色四视图-V1.1_2114880341025574914.json
hash: 8c60a88b9409bd9b
coverage: 0.78125
learned_at: 2026-10-30 17:51:15
nodes: [CLIPLoader, TextGenerateLTX2Prompt, QwenImage21Cache, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, ResolutionSelector, ComfySwitchNode, KSampler, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, easy showAnything, BatchImagesNode, LoadImage, PrimitiveStringMultiline, MarkdownNote, VAEDecode, SaveImage, StringConcatenate, PrimitiveStringMultiline, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1016887431955173, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen_image_2.1-图生图-角色四视图-V1.1_2114880341025574914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1-图生图-角色四视图-V1.1_2114880341025574914.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `ComfySwitchNode`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `BatchImagesNode`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `1016887431955173`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`CLIPLoader`、`TextGenerateLTX2Prompt`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`KSampler`、`EmptyLatentImage`、`UNETLoader`、`VAELoader`、`BatchImagesNode`、`VAEDecode`、`SaveImage`、`StringConcatenate`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
