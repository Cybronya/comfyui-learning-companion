---
key: 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json
name: Qwen Image 2.1 PE 文生图_2102653627042189314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json
hash: 59082f566bc67fd0
coverage: 0.526316
learned_at: 2026-10-06 21:47:24
nodes: [QwenImage21Cache, QwenPERewriteT8, CLIPLoader, easy showAnything, VAEDecode, CR Prompt Text, easy cleanGpuUsed, SaveImage, TextEncodeQwenImage21, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, UNETLoader, QwenImage21SpectrumT8, KSampler, Note, VAELoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode]
patterns: []
missing: [QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenPERewriteT8, easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `CLIPLoader`
- `easy showAnything`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `SaveImage`
- `TextEncodeQwenImage21`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `KSampler` ★核心
- `Note`
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`

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

覆盖率 **53%**（10/19）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`UNETLoader`、`KSampler`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`

**缺卡**（6）：`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`QwenPERewriteT8`、`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
