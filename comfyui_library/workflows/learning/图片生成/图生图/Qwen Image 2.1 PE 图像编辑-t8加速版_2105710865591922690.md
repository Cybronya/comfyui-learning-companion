---
key: 图片生成/图生图/Qwen Image 2.1 PE 图像编辑-t8加速版_2105710865591922690.json
name: Qwen Image 2.1 PE 图像编辑-t8加速版_2105710865591922690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 图像编辑-t8加速版_2105710865591922690.json
hash: 869f6b38a4c7aca0
coverage: 0.923077
learned_at: 2026-10-21 00:42:06
nodes: [CLIPLoader, UNETLoader, KSampler, VAEDecode, easy cleanGpuUsed, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, QwenPERewriteT8, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, QwenImage21SageAttentionT8, SaveImage, ResolutionSelector, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 PE 图像编辑-t8加速版_2105710865591922690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 图像编辑-t8加速版_2105710865591922690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `QwenPERewriteT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `QwenImage21SageAttentionT8`
- `SaveImage`
- `ResolutionSelector`
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `CR Prompt Text`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`QwenImage21SageAttentionT8`、`SaveImage`、`ResolutionSelector`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
