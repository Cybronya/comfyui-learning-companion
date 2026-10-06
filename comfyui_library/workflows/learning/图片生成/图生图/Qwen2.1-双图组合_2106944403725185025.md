---
key: 图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json
name: Qwen2.1-双图组合_2106944403725185025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json
hash: 0d8f0214243440a8
coverage: 0.923077
learned_at: 2026-10-07 02:41:29
nodes: [SaveImage, VAEDecode, BasicGuider, QwenImage21FunPDDLoader, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, LoadImage, PrimitiveInt]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `BasicGuider`
- `QwenImage21FunPDDLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`SaveImage`、`VAEDecode`、`BasicGuider`、`QwenImage21FunPDDLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SaveImage
