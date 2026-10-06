---
key: 图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json
name: Qwen2.1-双图组合_2106944403725185025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-双图组合_2106944403725185025.json
hash: 0d8f0214243440a8
coverage: 0.615385
learned_at: 2026-10-06 21:42:15
nodes: [SaveImage, VAEDecode, BasicGuider, QwenImage21FunPDDLoader, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, LoadImage, PrimitiveInt]
patterns: []
missing: [BasicGuider, QwenImage21FunPDDLoader, RandomNoise, SamplerCustomAdvanced]
discoveries: [次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识, 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识, 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **62%**（8/13）

**有卡**：`SaveImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`

**缺卡**（4）：`BasicGuider`、`QwenImage21FunPDDLoader`、`RandomNoise`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage、sd15-t2i-basic

## 学习发现

- 次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识
- 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明
