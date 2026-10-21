---
key: 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2109835098110648321.json
name: Qwen Image 2.1 t8加速PE+int8加速版_2109835098110648321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2109835098110648321.json
hash: ba3c54490155fcbd
coverage: 0.833333
learned_at: 2026-10-21 02:54:05
nodes: [CLIPLoader, CFGGuider, RandomNoise, LoadImage, LoadImage, easy cleanGpuUsed, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, VAELoader, QwenPERewriteT8, LoraLoaderModelOnly, QwenImage21SageAttentionT8, TextEncodeQwenImage21, ComfySwitchNode, ManualSigmas, easy showAnything, LoadImage, LoadImage, EmptyLatentImage, Note, ResolutionSelector, LoadImage, UNETLoader, UNETLoader, 孤海注释, LoadImage, CR Prompt Text, 孤海注释, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2109835098110648321.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 t8加速PE+int8加速版_2109835098110648321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `CFGGuider`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
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
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Note`
- `ResolutionSelector`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `孤海注释`
- `LoadImage`
- `CR Prompt Text`
- `孤海注释`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`CLIPLoader`、`CFGGuider`、`RandomNoise`、`LoadImage`、`easy cleanGpuUsed`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`VAELoader`、`QwenPERewriteT8`、`LoraLoaderModelOnly`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`ManualSigmas`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CR Prompt Text`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
