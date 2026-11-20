---
key: 平台全量/文生图｜Qwen-Image 2.1 完整 Turbo 模型（8 步）_2119357398690394114.json
name: 文生图｜Qwen-Image 2.1 完整 Turbo 模型（8 步）_2119357398690394114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/文生图｜Qwen-Image 2.1 完整 Turbo 模型（8 步）_2119357398690394114.json
hash: e807460f93ba8852
coverage: 1
learned_at: 2026-11-14 02:12:08
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, SaveImage, QwenImage21Cache, ManualSigmas, EmptyHunyuanImageLatent]
patterns: []
missing: []
---

# 平台全量/文生图｜Qwen-Image 2.1 完整 Turbo 模型（8 步）_2119357398690394114.json

> 来源文件 `comfyui_library/workflows/平台全量/文生图｜Qwen-Image 2.1 完整 Turbo 模型（8 步）_2119357398690394114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `ManualSigmas`
- `EmptyHunyuanImageLatent`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`ManualSigmas`、`EmptyHunyuanImageLatent`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、QwenImage21Cache、UNETLoader、CFGGuider、KSamplerSelect
