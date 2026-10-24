---
key: 图片生成/图生图/【qwen_image_2.1】图生图 多宫格_2109499886868713474.json
name: 【qwen_image_2.1】图生图 多宫格_2109499886868713474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【qwen_image_2.1】图生图 多宫格_2109499886868713474.json
hash: a25017c26d0fbc68
coverage: 0.882353
learned_at: 2026-10-23 11:49:11
nodes: [CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, QwenImage21Cache, ModelAttentionBackend, UNETLoader, KSamplerSelect, Reroute, ManualSigmas, TextEncodeQwenImage21, SamplerCustom, VAEDecode, ResolutionSelector, LoadImage, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/【qwen_image_2.1】图生图 多宫格_2109499886868713474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【qwen_image_2.1】图生图 多宫格_2109499886868713474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `ManualSigmas`
- `TextEncodeQwenImage21`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `LoadImage`
- `SaveImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`QwenImage21Cache`、`ModelAttentionBackend`、`UNETLoader`、`KSamplerSelect`、`ManualSigmas`、`TextEncodeQwenImage21`、`SamplerCustom`、`VAEDecode`、`ResolutionSelector`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
