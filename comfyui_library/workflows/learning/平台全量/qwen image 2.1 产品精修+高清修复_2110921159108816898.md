---
key: 平台全量/qwen image 2.1 产品精修+高清修复_2110921159108816898.json
name: qwen image 2.1 产品精修+高清修复_2110921159108816898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen image 2.1 产品精修+高清修复_2110921159108816898.json
hash: f36a0aea91e0c745
coverage: 0.862069
learned_at: 2026-11-14 01:15:59
nodes: [QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, KSampler, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, SaveImage, Note, TextEncodeQwenImage21, Image Comparer (rgthree), LoadImage, MuyeTextEditOutput, ShowText|pysssss, LayerUtility: ImageScaleByAspectRatio V2, QwenImagePromptOptimizer, LayerMask: SegmentAnythingUltra V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, WujiUpscaler2, VAEDecode, SaveImage, ImpactConditionalBranch, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1066858181304763, "steps": 30}
---

# 平台全量/qwen image 2.1 产品精修+高清修复_2110921159108816898.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen image 2.1 产品精修+高清修复_2110921159108816898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Note`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `LoadImage`
- `MuyeTextEditOutput`
- `ShowText|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `QwenImagePromptOptimizer`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WujiUpscaler2`
- `VAEDecode` ★核心
- `SaveImage`
- `ImpactConditionalBranch`
- `MarkdownNote`

## 关键参数

- `seed` = `1066858181304763`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`KSampler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`SaveImage`、`TextEncodeQwenImage21`、`LoadImage`、`MuyeTextEditOutput`、`LayerUtility: ImageScaleByAspectRatio V2`、`QwenImagePromptOptimizer`、`LayerMask: SegmentAnythingUltra V2`、`WujiUpscaler2`、`VAEDecode`、`ImpactConditionalBranch`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、SaveImage、LoadImage
