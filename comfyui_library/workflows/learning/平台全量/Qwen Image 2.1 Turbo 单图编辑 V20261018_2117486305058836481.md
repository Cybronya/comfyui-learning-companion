---
key: 平台全量/Qwen Image 2.1 Turbo 单图编辑 V20261018_2117486305058836481.json
name: Qwen Image 2.1 Turbo 单图编辑 V20261018_2117486305058836481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1 Turbo 单图编辑 V20261018_2117486305058836481.json
hash: fe9198a5d5cd5ff0
coverage: 1
learned_at: 2026-11-14 00:49:49
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, TextEncodeQwenImage21, SaveImageAdvanced, SaveImage, CR Prompt Text, easy int, easy int, LoraLoaderModelOnly, RandomNoise, BasicGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Qwen Image 2.1 Turbo 单图编辑 V20261018_2117486305058836481.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1 Turbo 单图编辑 V20261018_2117486305058836481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `SaveImage`
- `CR Prompt Text`
- `easy int`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`SaveImage`、`CR Prompt Text`、`easy int`、`LoraLoaderModelOnly`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
