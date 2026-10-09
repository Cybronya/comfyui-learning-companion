---
key: 图片生成/图生图/Qwen Image 2.1 PE 图像编辑2609_2106042591421747201.json
name: Qwen Image 2.1 PE 图像编辑2609_2106042591421747201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 图像编辑2609_2106042591421747201.json
hash: 38d714a165f41e3f
coverage: 0.821429
learned_at: 2026-10-09 22:09:18
nodes: [VAELoader, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, LoadImage, UNETLoader, easy showAnything, CLIPLoader, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21Cache, KSampler, easy cleanGpuUsed, SaveImage, VAEDecode, Note, TextEncodeQwenImage21, ComfySwitchNode, ResolutionSelector, EmptyLatentImage, LoadImage]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen Image 2.1 PE 图像编辑2609_2106042591421747201.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2106042591421747201.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAELoader`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `LoadImage`
- `UNETLoader` ★核心
- `easy showAnything`
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `VAEDecode` ★核心
- `Note`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LoadImage`

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

覆盖率 **82%**（23/28）

**有卡**：`VAELoader`、`LoadImage`、`QwenPERewriteT8`、`UNETLoader`、`CLIPLoader`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`QwenImage21Cache`、`KSampler`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
