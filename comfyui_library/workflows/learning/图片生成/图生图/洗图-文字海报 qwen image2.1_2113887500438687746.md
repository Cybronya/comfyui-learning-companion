---
key: 图片生成/图生图/洗图-文字海报 qwen image2.1_2113887500438687746.json
name: 洗图-文字海报 qwen image2.1_2113887500438687746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/洗图-文字海报 qwen image2.1_2113887500438687746.json
hash: e20126fb3ab0ff41
coverage: 0.842105
learned_at: 2026-10-26 22:06:30
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, CR Text, ShowText|pysssss, RHLLMChatNode, QwenImage21Cache, CR Text, LayerUtility: TextJoin, Image Comparer (rgthree), SaveImage, KSampler, VAEDecode, LoadImage, UNETLoader, TextEncodeQwenImage21, Note, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 1107779573592698, "steps": 25, "width": 1920}
---

# 图片生成/图生图/洗图-文字海报 qwen image2.1_2113887500438687746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/洗图-文字海报 qwen image2.1_2113887500438687746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `ShowText|pysssss`
- `RHLLMChatNode`
- `QwenImage21Cache`
- `CR Text`
- `LayerUtility: TextJoin`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `Note`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `1107779573592698`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`RHLLMChatNode`、`QwenImage21Cache`、`LayerUtility: TextJoin`、`SaveImage`、`KSampler`、`VAEDecode`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
