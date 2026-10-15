---
key: 图片生成/图生图/qwen image2.1产品细节图_2102470856244031490.json
name: qwen image2.1产品细节图_2102470856244031490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image2.1产品细节图_2102470856244031490.json
hash: 45a9981ce8ba6ca9
coverage: 0.678571
learned_at: 2026-10-15 22:25:36
nodes: [VAELoader, CLIPLoader, TextGenerateLTX2Prompt, TextEncodeQwenImage21, KSampler, easy setNode, VAEDecode, ShowText|pysssss, EmptyLatentImage, ComfySwitchNode, LoadImage, CLIPLoader, CLIPLoader, SetNode, SetNode, GetNode, ResolutionSelector, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, UNETLoader, SaveImage, PreviewImage, Image Comparer (rgthree), CR Prompt Text, Note, LoraLoaderModelOnly, QwenImage21Cache, Anything Everywhere3]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 783330575672886, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen image2.1产品细节图_2102470856244031490.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image2.1产品细节图_2102470856244031490.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `CLIPLoader`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `ResolutionSelector`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `CR Prompt Text`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `Anything Everywhere3`

## 关键参数

- `seed` = `783330575672886`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（19/28）

**有卡**：`VAELoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`KSampler`、`easy setNode`、`VAEDecode`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`UNETLoader`、`SaveImage`、`CR Prompt Text`、`LoraLoaderModelOnly`、`QwenImage21Cache`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
