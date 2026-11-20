---
key: 平台全量/千问qwen2.1文生图工作流（超快、超好看、不可商用）_2119269537064509441.json
name: 千问qwen2.1文生图工作流（超快、超好看、不可商用）_2119269537064509441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/千问qwen2.1文生图工作流（超快、超好看、不可商用）_2119269537064509441.json
hash: ceaeedaa094c9c0c
coverage: 1
learned_at: 2026-11-14 01:47:39
nodes: [UNETLoader, LoraLoaderModelOnly, EmptyLatentImage, LoraLoaderModelOnly, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, LoraLoaderModelOnly, QwenImage21Cache, BasicGuider, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecode, LoadImage, SaveImage, ExtendIntermediateSigmas]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1920, "width": 1080}
---

# 平台全量/千问qwen2.1文生图工作流（超快、超好看、不可商用）_2119269537064509441.json

> 来源文件 `comfyui_library/workflows/平台全量/千问qwen2.1文生图工作流（超快、超好看、不可商用）_2119269537064509441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `ExtendIntermediateSigmas`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`LoadImage`、`SaveImage`、`ExtendIntermediateSigmas`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
