---
key: 图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2102954366490734594.json
name: （稳定加速版）Qwen Image 2.1 PE 图像编辑_2102954366490734594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2102954366490734594.json
hash: dde1dadbf9630b04
coverage: 0.833333
learned_at: 2026-10-21 00:57:14
nodes: [Note, CLIPLoader, VAELoader, Note, LoadImage, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, CR Prompt Text, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, UNETLoader, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, Note, KSampler, VAEDecode, easy cleanGpuUsed, SaveImage, QwenPERewriteT8]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2102954366490734594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2102954366490734594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `LoadImage`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `Note`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `QwenPERewriteT8`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`EmptyLatentImage`、`ResolutionSelector`、`CR Prompt Text`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`UNETLoader`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`QwenPERewriteT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
