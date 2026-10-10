---
key: Flux.1 Krea Dev：文生图王者，独特美学，细节拉满！去除AI感_真实感摄影_1951065960218304513.json
name: Flux.1 Krea Dev：文生图王者，独特美学，细节拉满！去除AI感_真实感摄影_1951065960218304513
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev：文生图王者，独特美学，细节拉满！去除AI感_真实感摄影_1951065960218304513.json
hash: 9a26b18db0583f6c
coverage: 0.833333
learned_at: 2026-10-10 20:58:36
nodes: [UNETLoader, DualCLIPLoader, VAELoader, RH_Translator, EmptyLatentImage, ConditioningZeroOut, VAEDecode, KSampler, Text Multiline, SaveImage, easy showAnything, CLIPTextEncode]
patterns: [text_to_image]
missing: [Text Multiline]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 879282594993616, "steps": 20, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# Flux.1 Krea Dev：文生图王者，独特美学，细节拉满！去除AI感_真实感摄影_1951065960218304513.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev：文生图王者，独特美学，细节拉满！去除AI感_真实感摄影_1951065960218304513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `RH_Translator`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Text Multiline`
- `SaveImage`
- `easy showAnything`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `879282594993616`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`RH_Translator`、`EmptyLatentImage`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`SaveImage`、`CLIPTextEncode`

**缺卡**（1）：`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader、SaveImage

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
