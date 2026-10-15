---
key: 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json
name: Qwen Image 2.1 PE 文生图_2102653627042189314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json
hash: 59082f566bc67fd0
coverage: 0.736842
learned_at: 2026-10-10 20:58:50
nodes: [QwenImage21Cache, QwenPERewriteT8, CLIPLoader, easy showAnything, VAEDecode, CR Prompt Text, easy cleanGpuUsed, SaveImage, TextEncodeQwenImage21, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, UNETLoader, QwenImage21SpectrumT8, KSampler, Note, VAELoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json`

## 结构

**节点**（19 个）：
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `CLIPLoader`
- `easy showAnything`
- `VAEDecode`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `SaveImage`
- `TextEncodeQwenImage21`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `UNETLoader`
- `QwenImage21SpectrumT8`
- `KSampler`
- `Note`
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage`
- `ComfySwitchNode`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `19960422`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`QwenImage21Cache`、`QwenPERewriteT8`、`CLIPLoader`、`easy showAnything`、`VAEDecode`、`CR Prompt Text`、`easy cleanGpuUsed`、`SaveImage`、`TextEncodeQwenImage21`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`KSampler`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
