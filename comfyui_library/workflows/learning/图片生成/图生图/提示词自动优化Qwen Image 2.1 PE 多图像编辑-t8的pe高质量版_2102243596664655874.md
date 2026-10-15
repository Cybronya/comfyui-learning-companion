---
key: 图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json
name: 提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json
hash: b7b0f82e3d453ecd
coverage: 0.851852
learned_at: 2026-10-15 22:25:55
nodes: [CLIPLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, easy cleanGpuUsed, UNETLoader, easy showAnything, ComfySwitchNode, EmptyLatentImage, PrimitiveBoolean, ResolutionSelector, QwenPERewriteT8, 孤海注释, SaveImage, 孤海注释, LoadImage, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 109764000142089, "steps": 40, "width": 1024}
---

# 图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `easy showAnything`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `PrimitiveBoolean`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `孤海注释`
- `SaveImage`
- `孤海注释`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `109764000142089`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`EmptyLatentImage`、`PrimitiveBoolean`、`ResolutionSelector`、`QwenPERewriteT8`、`SaveImage`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
