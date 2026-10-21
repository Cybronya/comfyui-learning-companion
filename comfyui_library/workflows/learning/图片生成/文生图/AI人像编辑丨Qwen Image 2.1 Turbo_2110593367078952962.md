---
key: 图片生成/文生图/AI人像编辑丨Qwen Image 2.1 Turbo_2110593367078952962.json
name: AI人像编辑丨Qwen Image 2.1 Turbo_2110593367078952962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI人像编辑丨Qwen Image 2.1 Turbo_2110593367078952962.json
hash: fa14ee2e51a836de
coverage: 0.875
learned_at: 2026-10-21 02:51:11
nodes: [CLIPLoader, VAELoader, LoadImage, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, UNETLoader, QwenImage21SageAttentionT8, VAEDecode, easy cleanGpuUsed, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, SaveImage, CR Prompt Text, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, RandomNoise, LoraLoaderModelOnly, QwenPERewriteT8, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 2016, "width": 1152}
---

# 图片生成/文生图/AI人像编辑丨Qwen Image 2.1 Turbo_2110593367078952962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI人像编辑丨Qwen Image 2.1 Turbo_2110593367078952962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
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
- `ComfySwitchNode`

## 关键参数

- `width` = `1152`
- `height` = `2016`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`UNETLoader`、`QwenImage21SageAttentionT8`、`VAEDecode`、`easy cleanGpuUsed`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`SaveImage`、`CR Prompt Text`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`LoraLoaderModelOnly`、`QwenPERewriteT8`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
