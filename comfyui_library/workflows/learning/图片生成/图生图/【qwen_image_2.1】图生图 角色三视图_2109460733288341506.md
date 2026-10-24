---
key: 图片生成/图生图/【qwen_image_2.1】图生图 角色三视图_2109460733288341506.json
name: 【qwen_image_2.1】图生图 角色三视图_2109460733288341506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【qwen_image_2.1】图生图 角色三视图_2109460733288341506.json
hash: 0fbdfcfda0ca1268
coverage: 0.842105
learned_at: 2026-10-23 11:49:11
nodes: [CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, StringConcatenate, PrimitiveStringMultiline, EmptyLatentImage, ResolutionSelector, QwenImage21Cache, ModelAttentionBackend, UNETLoader, KSamplerSelect, Reroute, ManualSigmas, TextEncodeQwenImage21, SamplerCustom, PrimitiveStringMultiline, SaveImage, VAEDecode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/【qwen_image_2.1】图生图 角色三视图_2109460733288341506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【qwen_image_2.1】图生图 角色三视图_2109460733288341506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `ManualSigmas`
- `TextEncodeQwenImage21`
- `SamplerCustom` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`StringConcatenate`、`EmptyLatentImage`、`ResolutionSelector`、`QwenImage21Cache`、`ModelAttentionBackend`、`UNETLoader`、`KSamplerSelect`、`ManualSigmas`、`TextEncodeQwenImage21`、`SamplerCustom`、`SaveImage`、`VAEDecode`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
