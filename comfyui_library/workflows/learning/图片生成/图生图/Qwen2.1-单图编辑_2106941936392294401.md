---
key: 图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json
name: Qwen2.1-单图编辑_2106941936392294401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json
hash: e4fa0c02348ce8eb
coverage: 0.545455
learned_at: 2026-10-06 21:42:12
nodes: [SaveImageAdvanced, VAEDecode, BasicGuider, QwenImage21FunPDDLoader, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage]
patterns: []
missing: [BasicGuider, QwenImage21FunPDDLoader, RandomNoise, SamplerCustomAdvanced, SaveImageAdvanced]
discoveries: [次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识, 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识, 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-单图编辑_2106941936392294401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `SaveImageAdvanced`
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

## 知识

覆盖率 **55%**（6/11）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`

**缺卡**（5）：`BasicGuider`、`QwenImage21FunPDDLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`SaveImageAdvanced`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识
- 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
