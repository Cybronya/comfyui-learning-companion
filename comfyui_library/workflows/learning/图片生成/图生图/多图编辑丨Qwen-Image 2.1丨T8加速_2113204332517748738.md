---
key: 图片生成/图生图/多图编辑丨Qwen-Image 2.1丨T8加速_2113204332517748738.json
name: 多图编辑丨Qwen-Image 2.1丨T8加速_2113204332517748738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑丨Qwen-Image 2.1丨T8加速_2113204332517748738.json
hash: 2f0e9099c499fa33
coverage: 0.9375
learned_at: 2026-10-26 22:05:53
nodes: [CLIPLoader, VAELoader, LoadImage, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, UNETLoader, QwenImage21SageAttentionT8, VAEDecode, easy cleanGpuUsed, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, SaveImage, CR Prompt Text, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, RandomNoise, LoraLoaderModelOnly, QwenPERewriteT8]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/多图编辑丨Qwen-Image 2.1丨T8加速_2113204332517748738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑丨Qwen-Image 2.1丨T8加速_2113204332517748738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `SaveImage`
- `CR Prompt Text`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `QwenPERewriteT8`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`UNETLoader`、`QwenImage21SageAttentionT8`、`VAEDecode`、`easy cleanGpuUsed`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`SaveImage`、`CR Prompt Text`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`LoraLoaderModelOnly`、`QwenPERewriteT8`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
