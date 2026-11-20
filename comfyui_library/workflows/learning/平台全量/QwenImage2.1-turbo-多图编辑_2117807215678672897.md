---
key: 平台全量/QwenImage2.1-turbo-多图编辑_2117807215678672897.json
name: QwenImage2.1-turbo-多图编辑_2117807215678672897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/QwenImage2.1-turbo-多图编辑_2117807215678672897.json
hash: 7358724e52c19612
coverage: 0.740741
learned_at: 2026-11-14 00:53:22
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, LoadImage, LoadImage, CLIPLoader, TextEncodeQwenImage21, UNETLoader, QwenImage21Cache, RandomNoise, KSamplerSelect, VAEDecode, SaveImage, BasicGuider, SamplerCustomAdvanced, ManualSigmas, EmptyLatentImage, ComfySwitchNode, PrimitiveBoolean, Fast Groups Bypasser (rgthree), Note, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/QwenImage2.1-turbo-多图编辑_2117807215678672897.json

> 来源文件 `comfyui_library/workflows/平台全量/QwenImage2.1-turbo-多图编辑_2117807215678672897.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`UNETLoader`、`QwenImage21Cache`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`SaveImage`、`BasicGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`EmptyLatentImage`、`PrimitiveBoolean`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache、UNETLoader
