---
key: 图片生成/文生图/qwen-image-2.1多合一极简版_2101993261010345985.json
name: qwen-image-2.1多合一极简版_2101993261010345985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1多合一极简版_2101993261010345985.json
hash: 6502122fe5be2e9e
coverage: 0.888889
learned_at: 2026-10-20 01:51:55
nodes: [Seed (rgthree), UNETLoader, EmptyLatentImage, QwenImage21Cache, CLIPLoader, KSampler, VAEDecode, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyMediaSplitter, VAELoader, MiniMaxH3EasyMediaSplitter, PreviewAny, ResolutionSelector, QwenPERewriteT8, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1008780361661227, "steps": 40, "width": 1024}
---

# 图片生成/文生图/qwen-image-2.1多合一极简版_2101993261010345985.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1多合一极简版_2101993261010345985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `MiniMaxH3EasyMediaLoader`
- `MiniMaxH3EasyMediaSplitter`
- `VAELoader`
- `MiniMaxH3EasyMediaSplitter`
- `PreviewAny`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1008780361661227`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`Seed (rgthree)`、`UNETLoader`、`EmptyLatentImage`、`QwenImage21Cache`、`CLIPLoader`、`KSampler`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`MiniMaxH3EasyMediaLoader`、`MiniMaxH3EasyMediaSplitter`、`VAELoader`、`ResolutionSelector`、`QwenPERewriteT8`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
