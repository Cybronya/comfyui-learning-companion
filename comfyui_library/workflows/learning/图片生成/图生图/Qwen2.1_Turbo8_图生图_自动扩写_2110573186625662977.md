---
key: 图片生成/图生图/Qwen2.1_Turbo8_图生图_自动扩写_2110573186625662977.json
name: Qwen2.1_Turbo8_图生图_自动扩写_2110573186625662977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1_Turbo8_图生图_自动扩写_2110573186625662977.json
hash: 7730d7230e458704
coverage: 0.904762
learned_at: 2026-10-23 11:19:06
nodes: [CLIPLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, SamplerCustomAdvanced, VAEDecode, SaveImage, ResolutionSelector, ImageScale, MarkdownNote, ImageCompare, PathchSageAttentionKJ, MiniMaxLowVRAMAttention, MarkdownNote, LoadImage, RH_LLMAPI_Pro_Node, UNETLoader, BasicGuider, ManualSigmas, KSamplerSelect, RandomNoise]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen2.1_Turbo8_图生图_自动扩写_2110573186625662977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1_Turbo8_图生图_自动扩写_2110573186625662977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `ImageScale`
- `MarkdownNote`
- `ImageCompare`
- `PathchSageAttentionKJ`
- `MiniMaxLowVRAMAttention`
- `MarkdownNote`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `UNETLoader` ★核心
- `BasicGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`ImageScale`、`ImageCompare`、`PathchSageAttentionKJ`、`MiniMaxLowVRAMAttention`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`UNETLoader`、`BasicGuider`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、QwenImage21Cache、UNETLoader
