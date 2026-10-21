---
key: 图片生成/文生图/qwen-image-2.1多合一极简版_2106953656892481538.json
name: qwen-image-2.1多合一极简版_2106953656892481538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1多合一极简版_2106953656892481538.json
hash: 1cbcde0212c32593
coverage: 0.894737
learned_at: 2026-10-21 02:57:31
nodes: [EmptyLatentImage, QwenImage21Cache, VAEDecode, MiniMaxH3EasyMediaSplitter, MiniMaxH3EasyMediaSplitter, PreviewAny, QwenPERewriteT8, CR Prompt Text, Fast Groups Bypasser (rgthree), Seed (rgthree), SaveImage, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, ResolutionSelector, KSampler, TextEncodeQwenImage21, MiniMaxH3EasyMediaLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 526733745915763, "steps": 40, "width": 1024}
---

# 图片生成/文生图/qwen-image-2.1多合一极简版_2106953656892481538.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1多合一极简版_2106953656892481538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `MiniMaxH3EasyMediaSplitter`
- `MiniMaxH3EasyMediaSplitter`
- `PreviewAny`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `MiniMaxH3EasyMediaLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `526733745915763`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`MiniMaxH3EasyMediaSplitter`、`QwenPERewriteT8`、`CR Prompt Text`、`Seed (rgthree)`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ResolutionSelector`、`KSampler`、`TextEncodeQwenImage21`、`MiniMaxH3EasyMediaLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
