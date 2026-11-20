---
key: 图片生成/文生图/加速版Qwen+Image+2.1+PE（Un）+文生图和图片编辑_2116426459043688450.json
name: 加速版Qwen+Image+2.1+PE（Un）+文生图和图片编辑_2116426459043688450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/加速版Qwen+Image+2.1+PE（Un）+文生图和图片编辑_2116426459043688450.json
hash: 125ec4dcc0ade07c
coverage: 0.78125
learned_at: 2026-11-02 19:16:22
nodes: [Note, QwenImage21Cache, QwenImage21SageAttentionT8, VAEDecode, LoadImage, LoadImage, LoadImage, easy showAnything, CLIPLoader, UNETLoader, VAELoader, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, easy cleanGpuUsed, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LoraLoaderModelOnly, QwenPERewriteT8, RandomNoise, SaveImage, CR Prompt Text, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, MarkdownNote, 孤海注释, Int, 孤海注释, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/加速版Qwen+Image+2.1+PE（Un）+文生图和图片编辑_2116426459043688450.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/加速版Qwen+Image+2.1+PE（Un）+文生图和图片编辑_2116426459043688450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `Note`
- `QwenImage21Cache`
- `QwenImage21SageAttentionT8`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `easy cleanGpuUsed`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenPERewriteT8`
- `RandomNoise`
- `SaveImage`
- `CR Prompt Text`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `MarkdownNote`
- `孤海注释`
- `Int`
- `孤海注释`
- `孤海注释`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`QwenImage21Cache`、`QwenImage21SageAttentionT8`、`VAEDecode`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`easy cleanGpuUsed`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`QwenPERewriteT8`、`RandomNoise`、`SaveImage`、`CR Prompt Text`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`Int`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
