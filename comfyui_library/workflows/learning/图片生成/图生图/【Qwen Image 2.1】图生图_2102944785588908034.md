---
key: 图片生成/图生图/【Qwen Image 2.1】图生图_2102944785588908034.json
name: 【Qwen Image 2.1】图生图_2102944785588908034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图生图_2102944785588908034.json
hash: 6476b25338c903ed
coverage: 0.727273
learned_at: 2026-10-21 00:46:37
nodes: [LayerUtility: ImageReelComposit, PreviewImage, LayerUtility: ImageReel, TextEncodeQwenImage21, ComfySwitchNode, SaveImage, easy setNode, UNETLoader, QwenImage21Cache, VAELoader, KSampler, TextGenerateLTX2Prompt, EmptyLatentImage, ShowText|pysssss, ResolutionSelector, CLIPLoader, CR Prompt Text, GetNode, SetNode, Image Comparer (rgthree), VAEDecode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 122470033610442, "steps": 40, "width": 1024}
---

# 图片生成/图生图/【Qwen Image 2.1】图生图_2102944785588908034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图生图_2102944785588908034.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `SaveImage`
- `easy setNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `ShowText|pysssss`
- `ResolutionSelector`
- `CLIPLoader`
- `CR Prompt Text`
- `GetNode`
- `SetNode`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `122470033610442`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`SaveImage`、`easy setNode`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`KSampler`、`TextGenerateLTX2Prompt`、`EmptyLatentImage`、`ResolutionSelector`、`CLIPLoader`、`CR Prompt Text`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
