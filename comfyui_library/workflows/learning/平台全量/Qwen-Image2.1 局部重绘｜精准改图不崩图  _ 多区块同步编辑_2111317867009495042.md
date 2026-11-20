---
key: 平台全量/Qwen-Image2.1 局部重绘｜精准改图不崩图  _ 多区块同步编辑_2111317867009495042.json
name: Qwen-Image2.1 局部重绘｜精准改图不崩图  _ 多区块同步编辑_2111317867009495042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image2.1 局部重绘｜精准改图不崩图  _ 多区块同步编辑_2111317867009495042.json
hash: ffe23d1713e48d34
coverage: 0.580645
learned_at: 2026-11-14 00:51:49
nodes: [UNETLoader, CLIPLoader, KSampler, VAELoader, easy int, GetNode, Any Switch (rgthree), GetNode, SaveImage, Image Comparer (rgthree), MarkdownNote, LoadImage, MarkdownNote, PrimitiveStringMultiline, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadVAEModel, easy imageSize, VAEDecode, easy imageSize, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SetNode, GetNode, SetNode, GetNode, TextEncodeQwenImage21, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Mask Fill Holes, RHHiddenNodes, InpaintModelConditioning]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 580504116133585, "steps": 25}
---

# 平台全量/Qwen-Image2.1 局部重绘｜精准改图不崩图  _ 多区块同步编辑_2111317867009495042.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image2.1 局部重绘｜精准改图不崩图  _ 多区块同步编辑_2111317867009495042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `easy int`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2LoadVAEModel`
- `easy imageSize`
- `VAEDecode` ★核心
- `easy imageSize`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Mask Fill Holes`
- `RHHiddenNodes`
- `InpaintModelConditioning`

## 关键参数

- `seed` = `580504116133585`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（18/31）

**有卡**：`UNETLoader`、`CLIPLoader`、`KSampler`、`VAELoader`、`easy int`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadVAEModel`、`easy imageSize`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`TextEncodeQwenImage21`、`Mask Fill Holes`、`RHHiddenNodes`、`InpaintModelConditioning`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、SeedVR2LoadDiTModel
