---
key: 图片生成/文生图/Qwen2.1_Turbo8_加速-文生图_2110563232632107010.json
name: Qwen2.1_Turbo8_加速-文生图_2110563232632107010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1_Turbo8_加速-文生图_2110563232632107010.json
hash: 0f86cedfb9449323
coverage: 0.941176
learned_at: 2026-10-21 02:54:43
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, RandomNoise, BasicGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, MarkdownNote, PathchSageAttentionKJ, MiniMaxLowVRAMAttention, UNETLoader, ResolutionSelector, TextEncodeQwenImage21, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1376, "width": 768}
---

# 图片生成/文生图/Qwen2.1_Turbo8_加速-文生图_2110563232632107010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1_Turbo8_加速-文生图_2110563232632107010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
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
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `MiniMaxLowVRAMAttention`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心

## 关键参数

- `width` = `768`
- `height` = `1376`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`PathchSageAttentionKJ`、`MiniMaxLowVRAMAttention`、`UNETLoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache、UNETLoader
