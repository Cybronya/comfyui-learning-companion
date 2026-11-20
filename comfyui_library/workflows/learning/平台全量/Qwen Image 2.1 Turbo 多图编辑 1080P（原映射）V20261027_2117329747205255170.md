---
key: 平台全量/Qwen Image 2.1 Turbo 多图编辑 1080P（原映射）V20261027_2117329747205255170.json
name: Qwen Image 2.1 Turbo 多图编辑 1080P（原映射）V20261027_2117329747205255170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1 Turbo 多图编辑 1080P（原映射）V20261027_2117329747205255170.json
hash: 3900ef6ca8c043c5
coverage: 1
learned_at: 2026-11-14 00:49:52
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, QwenImage21Cache, TextEncodeQwenImage21, SaveImageAdvanced, LoadImage, LoadImage, SaveImage, CR Prompt Text, easy int, easy int, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, RandomNoise, BasicGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, ImageScale]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Qwen Image 2.1 Turbo 多图编辑 1080P（原映射）V20261027_2117329747205255170.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1 Turbo 多图编辑 1080P（原映射）V20261027_2117329747205255170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `CR Prompt Text`
- `easy int`
- `easy int`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `ImageScale`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`SaveImage`、`CR Prompt Text`、`easy int`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`ImageScale`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache、UNETLoader
