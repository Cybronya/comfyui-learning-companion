---
key: 图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2108372055283560450.json
name: Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2108372055283560450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2108372055283560450.json
hash: 6ae58f14b30af009
coverage: 0.894737
learned_at: 2026-10-21 00:43:55
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, Seed (rgthree), LoadImage, Text Multiline, LoraLoaderModelOnly, Image Comparer (rgthree), XinbaoImageStandardizer, SaveImageAdvanced, ImageConcanate, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 671645295963475, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2108372055283560450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2108372055283560450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `LoadImage`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `XinbaoImageStandardizer`
- `SaveImageAdvanced`
- `ImageConcanate`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `671645295963475`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`LoadImage`、`Text Multiline`、`LoraLoaderModelOnly`、`XinbaoImageStandardizer`、`SaveImageAdvanced`、`ImageConcanate`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
