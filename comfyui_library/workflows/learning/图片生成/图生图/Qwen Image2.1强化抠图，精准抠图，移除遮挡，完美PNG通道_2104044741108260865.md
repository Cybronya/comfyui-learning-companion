---
key: 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865.json
name: Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865.json
hash: 5f9665b8f2b8c4bb
coverage: 0.884615
learned_at: 2026-10-21 00:42:52
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, Seed (rgthree), SaveImageAdvanced, LoraLoaderModelOnly, LoadImage, XinbaoImageStandardizer, StringToAnyNode, StringToAnyNode, easy ifElse, easy boolean, Image Comparer (rgthree), ImageConcanate, SaveImage, ttN concat, Text Multiline, Text Multiline, Text Multiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 429407134982510, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
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
- `SaveImageAdvanced`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `XinbaoImageStandardizer`
- `StringToAnyNode`
- `StringToAnyNode`
- `easy ifElse`
- `easy boolean`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `SaveImage`
- `ttN concat`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `429407134982510`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`SaveImageAdvanced`、`LoraLoaderModelOnly`、`LoadImage`、`XinbaoImageStandardizer`、`StringToAnyNode`、`easy boolean`、`ImageConcanate`、`SaveImage`、`ttN concat`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
