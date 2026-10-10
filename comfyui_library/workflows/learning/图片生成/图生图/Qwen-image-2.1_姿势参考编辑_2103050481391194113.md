---
key: 图片生成/图生图/Qwen-image-2.1_姿势参考编辑_2103050481391194113.json
name: Qwen-image-2.1_姿势参考编辑_2103050481391194113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1_姿势参考编辑_2103050481391194113.json
hash: 99839730d306e019
coverage: 0.681818
learned_at: 2026-10-10 20:48:09
nodes: [UNETLoader, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, CLIPLoader, SetNode, VAELoader, SetNode, QwenImage21SpectrumT8, SetNode, QwenPERewriteT8, GetNode, GetNode, GetNode, KSampler, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, JjkText, ResolutionSelector, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 178454469908951, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen-image-2.1_姿势参考编辑_2103050481391194113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1_姿势参考编辑_2103050481391194113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `QwenImage21SpectrumT8`
- `SetNode`
- `QwenPERewriteT8`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `ResolutionSelector`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `178454469908951`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`UNETLoader`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`CLIPLoader`、`VAELoader`、`QwenImage21SpectrumT8`、`QwenPERewriteT8`、`KSampler`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`ResolutionSelector`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
