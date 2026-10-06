---
key: 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2104456492933013506.json
name: Qwen Image 2.1 文生图-PE版_2104456492933013506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图-PE版_2104456492933013506.json
hash: 62fd3c1b1cb572ae
coverage: 0.733333
learned_at: 2026-10-07 02:15:58
nodes: [QwenImage21Cache, CLIPLoader, UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, VAELoader, easy cleanGpuUsed, VAEDecode, ResolutionSelector, CR Prompt Text, easy showAnything, QwenPERewriteT8, SaveImage, KSampler]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 775977268571152, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2104456492933013506.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图-PE版_2104456492933013506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `CR Prompt Text`
- `easy showAnything`
- `QwenPERewriteT8`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `775977268571152`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`ResolutionSelector`、`QwenPERewriteT8`、`SaveImage`、`KSampler`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
