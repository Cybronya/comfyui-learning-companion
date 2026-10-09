---
key: 图片生成/图生图/超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json
name: 超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json
hash: 4a86f24f029758a9
coverage: 0.846154
learned_at: 2026-10-09 22:09:16
nodes: [CLIPLoader, UNETLoader, KSampler, VAEDecode, easy cleanGpuUsed, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, QwenPERewriteT8, LoadImage, LoadImage, ResolutionSelector, LoadImage, SaveImage, TextEncodeQwenImage21, CR Prompt Text, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21SageAttentionT8]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2103518802859352065.json`

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
- `ResolutionSelector`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `QwenImage21SageAttentionT8`

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

覆盖率 **85%**（22/26）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`QwenPERewriteT8`、`ResolutionSelector`、`SaveImage`、`TextEncodeQwenImage21`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`QwenImage21SageAttentionT8`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
