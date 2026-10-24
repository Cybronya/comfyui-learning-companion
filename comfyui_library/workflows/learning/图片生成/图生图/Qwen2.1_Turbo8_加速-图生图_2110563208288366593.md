---
key: 图片生成/图生图/Qwen2.1_Turbo8_加速-图生图_2110563208288366593.json
name: Qwen2.1_Turbo8_加速-图生图_2110563208288366593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1_Turbo8_加速-图生图_2110563208288366593.json
hash: 6b432b5b9257b1e6
coverage: 0.947368
learned_at: 2026-10-23 11:19:05
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, RandomNoise, BasicGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, ImageScale, MarkdownNote, ImageCompare, PathchSageAttentionKJ, MiniMaxLowVRAMAttention, ResolutionSelector, LoadImage, UNETLoader, TextEncodeQwenImage21]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen2.1_Turbo8_加速-图生图_2110563208288366593.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1_Turbo8_加速-图生图_2110563208288366593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageScale`
- `MarkdownNote`
- `ImageCompare`
- `PathchSageAttentionKJ`
- `MiniMaxLowVRAMAttention`
- `ResolutionSelector`
- `LoadImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ImageScale`、`ImageCompare`、`PathchSageAttentionKJ`、`MiniMaxLowVRAMAttention`、`ResolutionSelector`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、QwenImage21Cache、UNETLoader
