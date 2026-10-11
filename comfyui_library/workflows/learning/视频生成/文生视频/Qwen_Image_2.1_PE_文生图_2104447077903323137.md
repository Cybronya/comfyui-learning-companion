---
key: 视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json
name: Qwen_Image_2.1_PE_文生图_2104447077903323137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json
hash: 8dfa17b91a897a50
coverage: 0.666667
learned_at: 2026-10-11 22:12:46
nodes: [Note, UNETLoader, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, KSampler, CR Prompt Text, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, QwenPERewriteT8, easy cleanGpuUsed, SaveImage, EmptyImage, PreviewImage]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `CR Prompt Text`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `QwenPERewriteT8`
- `easy cleanGpuUsed`
- `SaveImage`
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **67%**（12/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`KSampler`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`QwenPERewriteT8`、`SaveImage`、`EmptyImage`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
