---
key: 图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json
name: Qwen Image 2.1 PE 文生图_2102401855983808514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json
hash: eded267f4a93f25e
coverage: 0.6875
learned_at: 2026-10-07 02:40:58
nodes: [CLIPLoader, Note, UNETLoader, VAELoader, QwenImage21Cache, KSampler, VAEDecode, easy cleanGpuUsed, EmptyLatentImage, SaveImage, easy showAnything, QwenPERewriteT8, CR Prompt Text, TextEncodeQwenImage21, ComfySwitchNode, ResolutionSelector]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `Note`
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `easy showAnything`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ResolutionSelector`

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

覆盖率 **69%**（11/16）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`ResolutionSelector`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
