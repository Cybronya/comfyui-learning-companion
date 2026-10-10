---
key: Qwen Image 2.1 文生图-PE版_2102793929358929921.json
name: Qwen Image 2.1 文生图-PE版_2102793929358929921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json
hash: 428ce7a9815eb97a
coverage: 0.6875
learned_at: 2026-10-10 20:58:51
nodes: [QwenImage21Cache, CLIPLoader, UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, VAELoader, easy showAnything, QwenPERewriteT8, KSampler, easy cleanGpuUsed, VAEDecode, Note, SaveImage, ResolutionSelector, CR Prompt Text]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 360346436452785, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# Qwen Image 2.1 文生图-PE版_2102793929358929921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `easy showAnything`
- `QwenPERewriteT8`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Note`
- `SaveImage`
- `ResolutionSelector`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `360346436452785`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAELoader`、`QwenPERewriteT8`、`KSampler`、`VAEDecode`、`SaveImage`、`ResolutionSelector`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
