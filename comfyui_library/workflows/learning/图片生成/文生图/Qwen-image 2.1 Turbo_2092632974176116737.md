---
key: 图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json
name: Qwen-image 2.1 Turbo_2092632974176116737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json
hash: 5191665165846638
coverage: 0.875
learned_at: 2026-10-21 02:54:37
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, LoadImage, LoadImage, TextEncodeQwenImage21, QwenImage21Cache, RandomNoise, KSamplerSelect, VAEDecode, SaveImage, BasicGuider, SamplerCustomAdvanced, ManualSigmas, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, PrimitiveBoolean, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, CLIPLoader, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image 2.1 Turbo_2092632974176116737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `LoadImage`
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
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`LoadImage`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`SaveImage`、`BasicGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`ResolutionSelector`、`EmptyLatentImage`、`PrimitiveBoolean`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
