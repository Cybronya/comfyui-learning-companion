---
key: 图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json
name: QwenImage2.1-turbo专用工作流_2109185736493850625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json
hash: 1d30c6af951f9f1f
coverage: 0.84
learned_at: 2026-10-21 02:54:48
nodes: [LoadImage, LoadImage, LoadImage, VAELoader, LoadImage, LoadImage, TextEncodeQwenImage21, QwenImage21Cache, RandomNoise, KSamplerSelect, VAEDecode, SaveImage, BasicGuider, SamplerCustomAdvanced, ManualSigmas, EmptyLatentImage, ComfySwitchNode, LoadImage, UNETLoader, CLIPLoader, ResolutionSelector, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PrimitiveBoolean, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage2.1-turbo专用工作流_2109185736493850625.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
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
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`LoadImage`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`SaveImage`、`BasicGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
