---
key: 图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json
name: [Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json
hash: ec6b24dc396157f2
coverage: 0.761905
learned_at: 2026-10-21 02:56:39
nodes: [EmptyLatentImage, Seed (rgthree), UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, CLIPLoader, CLIPLoader, CLIPLoader, VAEDecode, Text, RHLLMChatNode, PreviewAny, TextEncodeQwenImage21, KSampler, SaveImage, Text, PreviewImage, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 662800525719862, "steps": 40, "width": 1024}
---

# 图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Text`
- `RHLLMChatNode`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `SaveImage`
- `Text`
- `PreviewImage`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `662800525719862`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`EmptyLatentImage`、`Seed (rgthree)`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`Text`、`RHLLMChatNode`、`TextEncodeQwenImage21`、`KSampler`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
