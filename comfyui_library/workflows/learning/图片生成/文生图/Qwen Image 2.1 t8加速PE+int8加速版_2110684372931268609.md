---
key: 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2110684372931268609.json
name: Qwen Image 2.1 t8加速PE+int8加速版_2110684372931268609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2110684372931268609.json
hash: 033916971d761274
coverage: 0.833333
learned_at: 2026-10-21 02:54:06
nodes: [CLIPLoader, CFGGuider, RandomNoise, easy cleanGpuUsed, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, VAELoader, QwenPERewriteT8, LoraLoaderModelOnly, QwenImage21SageAttentionT8, TextEncodeQwenImage21, ComfySwitchNode, ManualSigmas, easy showAnything, LoadImage, EmptyLatentImage, Note, LoadImage, UNETLoader, UNETLoader, 孤海注释, SaveImage, 孤海注释, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2110684372931268609.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2110684372931268609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `CFGGuider`
- `RandomNoise`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `QwenPERewriteT8`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21SageAttentionT8`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ManualSigmas`
- `easy showAnything`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Note`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `孤海注释`
- `SaveImage`
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`CLIPLoader`、`CFGGuider`、`RandomNoise`、`easy cleanGpuUsed`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`VAELoader`、`QwenPERewriteT8`、`LoraLoaderModelOnly`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`ManualSigmas`、`LoadImage`、`EmptyLatentImage`、`UNETLoader`、`SaveImage`、`CR Prompt Text`、`ResolutionSelector`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
