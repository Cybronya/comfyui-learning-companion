---
key: 图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json
name: Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json
hash: 27b85149986677fa
coverage: 0.807692
learned_at: 2026-10-15 22:26:57
nodes: [UNETLoader, CLIPLoader, VAEDecode, easy cleanGpuUsed, PreviewImage, Image Remove Alpha JK, VOSR2Upscale, VOSR2ModelLoader, ImageApplyLUT+, SaveImage, UNETLoader, CLIPLoader, TextEncodeQwenImage21, SaveImage, QwenImage21Cache, KSampler, Note, ComfySwitchNode, EmptyLatentImage, VAELoader, ResolutionSelector, PlaySound|pysssss, Lora Loader Stack (rgthree), MarkdownNote, PrimitiveStringMultiline, easy imageChooser]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills文生图+放大2K,4K_2102657150928642049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `Image Remove Alpha JK`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `ImageApplyLUT+`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `SaveImage`
- `QwenImage21Cache`
- `KSampler` ★核心
- `Note`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ResolutionSelector`
- `PlaySound|pysssss`
- `Lora Loader Stack (rgthree)`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `easy imageChooser`

## 关键参数

- `seed` = `3`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`easy cleanGpuUsed`、`Image Remove Alpha JK`、`VOSR2Upscale`、`VOSR2ModelLoader`、`ImageApplyLUT+`、`SaveImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`ResolutionSelector`、`PlaySound|pysssss`、`Lora Loader Stack (rgthree)`、`easy imageChooser`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
