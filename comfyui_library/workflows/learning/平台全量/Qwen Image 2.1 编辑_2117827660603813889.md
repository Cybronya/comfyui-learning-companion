---
key: 平台全量/Qwen Image 2.1 编辑_2117827660603813889.json
name: Qwen Image 2.1 编辑_2117827660603813889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1 编辑_2117827660603813889.json
hash: 30d472995243cbee
coverage: 1
learned_at: 2026-11-14 00:49:59
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, TextEncodeQwenImage21, SaveImageAdvanced, SaveImage, easy int, easy int, LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, BasicScheduler, UNETLoader, ModelAttentionBackend, CFGGuider, QwenImage21SpectrumT8, FluxKontextImageScale]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Qwen Image 2.1 编辑_2117827660603813889.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1 编辑_2117827660603813889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `SaveImage`
- `easy int`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `CFGGuider`
- `QwenImage21SpectrumT8`
- `FluxKontextImageScale`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`SaveImage`、`easy int`、`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`BasicScheduler`、`ModelAttentionBackend`、`CFGGuider`、`QwenImage21SpectrumT8`、`FluxKontextImageScale`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、EmptyLatentImage、LoadImage
