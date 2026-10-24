---
key: 图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2110647588159578114.json
name: Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2110647588159578114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2110647588159578114.json
hash: c12c873c1883472c
coverage: 0.826087
learned_at: 2026-10-23 11:18:28
nodes: [KSampler, WujiCleaner, WujiUpscaler, SaveImage, RH_RhartImageG2ImageToImage, SaveImage, LoadImage, LoadImage, LoadImage, easy promptConcat, Fast Groups Muter (rgthree), VAEDecode, PreviewAny, CLIPLoader, RH_LLMAPI_NODE, TextEncodeQwenImage21, UNETLoader, VAELoader, EmptyLatentImage, PrimitiveStringMultiline, Fast Groups Muter (rgthree), WujiPromptEditor, RH_LLMAPI_NODE]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 904, "sampler_name": "euler", "scheduler": "simple", "seed": 127940642947996, "steps": 8, "width": 1560}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2110647588159578114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2110647588159578114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSampler` ★核心
- `WujiCleaner`
- `WujiUpscaler`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy promptConcat`
- `Fast Groups Muter (rgthree)`
- `VAEDecode` ★核心
- `PreviewAny`
- `CLIPLoader`
- `RH_LLMAPI_NODE`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `Fast Groups Muter (rgthree)`
- `WujiPromptEditor`
- `RH_LLMAPI_NODE`

## 关键参数

- `seed` = `127940642947996`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1560`
- `height` = `904`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`KSampler`、`WujiCleaner`、`WujiUpscaler`、`SaveImage`、`RH_RhartImageG2ImageToImage`、`LoadImage`、`easy promptConcat`、`VAEDecode`、`CLIPLoader`、`RH_LLMAPI_NODE`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`WujiPromptEditor`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
