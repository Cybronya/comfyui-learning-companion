---
key: 平台全量/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2105640635368820738.json
name: Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2105640635368820738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2105640635368820738.json
hash: 3cc0ab9f310fcb7c
coverage: 0.888889
learned_at: 2026-11-14 00:53:28
nodes: [VAELoader, XinbaoImageStandardizer, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoraLoaderModelOnly, CLIPLoader, UNETLoader, QwenImage21Cache, KSampler, Seed (rgthree), LoadImage, Text Multiline, VAEDecode, TextEncodeQwenImage21, SaveImageAdvanced, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 935262885936672, "steps": 25, "width": 1024}
---

# 平台全量/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2105640635368820738.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2105640635368820738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `XinbaoImageStandardizer`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `Seed (rgthree)`
- `LoadImage`
- `Text Multiline`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `935262885936672`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`VAELoader`、`XinbaoImageStandardizer`、`ResolutionSelector`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`KSampler`、`Seed (rgthree)`、`LoadImage`、`Text Multiline`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
