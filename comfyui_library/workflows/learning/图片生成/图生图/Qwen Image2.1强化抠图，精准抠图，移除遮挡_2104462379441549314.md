---
key: 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314.json
name: Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314.json
hash: 357bcad7f15c8df0
coverage: 0.833333
learned_at: 2026-10-21 00:42:52
nodes: [UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, Seed (rgthree), LoadImage, TextEncodeQwenImage21, KSampler, ImageConcanate, VAEDecode, SaveImageAdvanced, SaveImage, Image Comparer (rgthree), PreviewAny, Text Concatenate, Text Multiline, Text Multiline, Text Multiline, XinbaoImageStandardizer, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 253891744581820, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Seed (rgthree)`
- `LoadImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ImageConcanate`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewAny`
- `Text Concatenate`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `XinbaoImageStandardizer`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `253891744581820`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`ResolutionSelector`、`EmptyLatentImage`、`Seed (rgthree)`、`LoadImage`、`TextEncodeQwenImage21`、`KSampler`、`ImageConcanate`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`Text Concatenate`、`Text Multiline`、`XinbaoImageStandardizer`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
