---
key: Qwen Image 2.1 PE 文生图2609_2106042102424629249.json
name: Qwen Image 2.1 PE 文生图2609_2106042102424629249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图2609_2106042102424629249.json
hash: 3e9dff137dacdb05
coverage: 0.736842
learned_at: 2026-10-10 20:58:50
nodes: [VAELoader, CR Prompt Text, QwenPERewriteT8, QwenImage21Cache, KSampler, VAEDecode, easy cleanGpuUsed, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, Note, easy showAnything, UNETLoader, CLIPLoader, TextEncodeQwenImage21, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21SageAttentionT8, SaveImage]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 639673362874167, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# Qwen Image 2.1 PE 文生图2609_2106042102424629249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图2609_2106042102424629249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAELoader`
- `CR Prompt Text`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `Note`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `QwenImage21SageAttentionT8`
- `SaveImage`

## 关键参数

- `seed` = `639673362874167`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`VAELoader`、`QwenPERewriteT8`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`QwenImage21SageAttentionT8`、`SaveImage`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
