---
key: 图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json
name: 千问iamge2.1文生图_2102716967022063618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json
hash: 5b8b7fa80731ddb9
coverage: 0.785714
learned_at: 2026-10-07 02:36:43
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, EmptyLatentImage, TextEncodeQwenImage21, VAEDecode, SaveImage, TextGenerateLTX2Prompt, ResolutionSelector, MarkdownNote, easy showAnything, CLIPLoader, CR Text]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 804997194651257, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `MarkdownNote`
- `easy showAnything`
- `CLIPLoader`
- `CR Text`

## 关键参数

- `seed` = `804997194651257`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`TextGenerateLTX2Prompt`、`ResolutionSelector`

**缺卡**（1）：`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
