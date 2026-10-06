---
key: 图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json
name: Qwen2.1-透明抠图_2106946708730105858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json
hash: 3d89d53534e70209
coverage: 0.583333
learned_at: 2026-10-06 21:42:18
nodes: [SaveImage, VAEDecode, BasicGuider, QwenImage21FunPDDLoader, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, PrimitiveInt]
patterns: []
missing: [BasicGuider, QwenImage21FunPDDLoader, RandomNoise, SamplerCustomAdvanced]
discoveries: [次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识, 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识, 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
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
- `PrimitiveInt`

## 知识

覆盖率 **58%**（7/12）

**有卡**：`SaveImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`

**缺卡**（4）：`BasicGuider`、`QwenImage21FunPDDLoader`、`RandomNoise`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage、sd15-t2i-basic

## 学习发现

- 次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识
- 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明
