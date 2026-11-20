---
key: 视频生成/图生视频/加速版Qwen+Image+2.1+PEUn+文生图和图片编辑_2116717933350182914.json
name: 加速版Qwen+Image+2.1+PEUn+文生图和图片编辑_2116717933350182914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/加速版Qwen+Image+2.1+PEUn+文生图和图片编辑_2116717933350182914.json
hash: fc47f1830ed9f5fd
coverage: 0.806452
learned_at: 2026-11-02 19:19:22
nodes: [Note, QwenImage21Cache, QwenImage21SageAttentionT8, VAEDecode, LoadImage, LoadImage, LoadImage, easy showAnything, CLIPLoader, UNETLoader, VAELoader, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, easy cleanGpuUsed, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LoraLoaderModelOnly, QwenPERewriteT8, RandomNoise, SaveImage, CR Prompt Text, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, 孤海注释, Int, 孤海注释, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 视频生成/图生视频/加速版Qwen+Image+2.1+PEUn+文生图和图片编辑_2116717933350182914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/加速版Qwen+Image+2.1+PEUn+文生图和图片编辑_2116717933350182914.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
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
- `孤海注释`
- `Int`
- `孤海注释`
- `孤海注释`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`QwenImage21Cache`、`QwenImage21SageAttentionT8`、`VAEDecode`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`easy cleanGpuUsed`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`QwenPERewriteT8`、`RandomNoise`、`SaveImage`、`CR Prompt Text`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`Int`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
