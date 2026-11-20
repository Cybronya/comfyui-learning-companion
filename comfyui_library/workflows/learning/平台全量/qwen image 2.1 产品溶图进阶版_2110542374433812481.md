---
key: 平台全量/qwen image 2.1 产品溶图进阶版_2110542374433812481.json
name: qwen image 2.1 产品溶图进阶版_2110542374433812481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen image 2.1 产品溶图进阶版_2110542374433812481.json
hash: e8d23fa17aee718e
coverage: 0.75
learned_at: 2026-11-14 01:15:58
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageAutoCrop V2, FastCanvasTool, RembgByBiRefNet, LoadRembgByBiRefNetModel, Note, LoadImage, LoadImage, Image Comparer (rgthree), QwenImage21SageAttentionT8, QwenImage21SpectrumT8, ShowText|pysssss, QwenImagePromptOptimizer, QwenImage21BlockCacheT8, KSampler, UNETLoader, VAELoader, CLIPLoader, Reroute, EmptyLatentImage, SaveImage, PrimitiveStringMultiline, VAEDecode, PreviewImage, FastCanvas, WujiUpscaler2, LoraLoaderModelOnly, Note, PrimitiveBoolean, ComfySwitchNode, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 291805213925184, "steps": 30, "width": 1024}
---

# 平台全量/qwen image 2.1 产品溶图进阶版_2110542374433812481.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen image 2.1 产品溶图进阶版_2110542374433812481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageAutoCrop V2`
- `FastCanvasTool`
- `RembgByBiRefNet`
- `LoadRembgByBiRefNetModel`
- `Note`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `ShowText|pysssss`
- `QwenImagePromptOptimizer`
- `QwenImage21BlockCacheT8`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `Reroute`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `PreviewImage`
- `FastCanvas`
- `WujiUpscaler2`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `291805213925184`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（24/32）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageAutoCrop V2`、`FastCanvasTool`、`RembgByBiRefNet`、`LoadRembgByBiRefNetModel`、`LoadImage`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`QwenImagePromptOptimizer`、`QwenImage21BlockCacheT8`、`KSampler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`FastCanvas`、`WujiUpscaler2`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
