---
key: 图片生成/文生图/（最强T8版加速）Qwen Image 2.1 PE(Un) 文生图v2_2108631026816868353.json
name: （最强T8版加速）Qwen Image 2.1 PE(Un) 文生图v2_2108631026816868353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（最强T8版加速）Qwen Image 2.1 PE(Un) 文生图v2_2108631026816868353.json
hash: 20a819ffe9929dd3
coverage: 0.84
learned_at: 2026-10-21 03:03:32
nodes: [Note, CLIPLoader, VAELoader, VAEDecode, Note, CR Prompt Text, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, easy cleanGpuUsed, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, QwenImage21SpectrumT8, SaveImage, LoraLoaderModelOnly, QwenPERewriteT8, CFGGuider, KSamplerSelect, ManualSigmas, RandomNoise, QwenImage21Cache, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/（最强T8版加速）Qwen Image 2.1 PE(Un) 文生图v2_2108631026816868353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（最强T8版加速）Qwen Image 2.1 PE(Un) 文生图v2_2108631026816868353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `CR Prompt Text`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `easy cleanGpuUsed`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `QwenPERewriteT8`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `QwenImage21Cache`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`CR Prompt Text`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`easy cleanGpuUsed`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`SaveImage`、`LoraLoaderModelOnly`、`QwenPERewriteT8`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`QwenImage21Cache`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
