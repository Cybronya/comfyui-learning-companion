---
key: 图片生成/文生图/Qwen2.1_Turbo8_RunningHub_文生图_LLM自动扩写_2110569692946591746.json
name: Qwen2.1_Turbo8_RunningHub_文生图_LLM自动扩写_2110569692946591746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1_Turbo8_RunningHub_文生图_LLM自动扩写_2110569692946591746.json
hash: a784e3e6ad3b34fc
coverage: 0.894737
learned_at: 2026-10-21 02:54:42
nodes: [CLIPLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, RandomNoise, BasicGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, ResolutionSelector, MarkdownNote, EmptyLatentImage, PathchSageAttentionKJ, MiniMaxLowVRAMAttention, MarkdownNote, RH_LLMAPI_Pro_Node, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1376, "width": 768}
---

# 图片生成/文生图/Qwen2.1_Turbo8_RunningHub_文生图_LLM自动扩写_2110569692946591746.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1_Turbo8_RunningHub_文生图_LLM自动扩写_2110569692946591746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `PathchSageAttentionKJ`
- `MiniMaxLowVRAMAttention`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `UNETLoader` ★核心

## 关键参数

- `width` = `768`
- `height` = `1376`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`、`PathchSageAttentionKJ`、`MiniMaxLowVRAMAttention`、`RH_LLMAPI_Pro_Node`、`UNETLoader`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache、UNETLoader
