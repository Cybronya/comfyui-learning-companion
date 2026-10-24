---
key: 图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json
name: Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json
hash: 4667852d121707c9
coverage: 0.416667
learned_at: 2026-10-23 11:13:30
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, Seed (rgthree), KSampler, VAEDecode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, Int, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, EmptyLatentImage, GetNode, LoadImage, ResolutionSelector, CR Prompt Text, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 910861866516069, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `SaveImage`

## 关键参数

- `seed` = `910861866516069`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **42%**（15/36）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`KSampler`、`VAEDecode`、`Int`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
