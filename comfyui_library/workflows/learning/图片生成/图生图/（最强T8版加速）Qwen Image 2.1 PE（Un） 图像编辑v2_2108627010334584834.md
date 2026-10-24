---
key: 图片生成/图生图/（最强T8版加速）Qwen Image 2.1 PE（Un） 图像编辑v2_2108627010334584834.json
name: （最强T8版加速）Qwen Image 2.1 PE（Un） 图像编辑v2_2108627010334584834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（最强T8版加速）Qwen Image 2.1 PE（Un） 图像编辑v2_2108627010334584834.json
hash: 6a11fea9c355de7f
coverage: 0.857143
learned_at: 2026-10-23 13:37:44
nodes: [Note, CLIPLoader, VAELoader, Note, LoadImage, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, UNETLoader, QwenImage21SageAttentionT8, Note, VAEDecode, easy cleanGpuUsed, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, SaveImage, CR Prompt Text, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, RandomNoise, LoraLoaderModelOnly, QwenPERewriteT8]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/（最强T8版加速）Qwen Image 2.1 PE（Un） 图像编辑v2_2108627010334584834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（最强T8版加速）Qwen Image 2.1 PE（Un） 图像编辑v2_2108627010334584834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Note`
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
- `Note`
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

覆盖率 **86%**（30/35）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`UNETLoader`、`QwenImage21SageAttentionT8`、`VAEDecode`、`easy cleanGpuUsed`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`SaveImage`、`CR Prompt Text`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`LoraLoaderModelOnly`、`QwenPERewriteT8`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
