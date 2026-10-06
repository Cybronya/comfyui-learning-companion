---
key: 图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json
name: Qwen2.1-文生图_2106946374871904257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json
hash: 7df83dbccb2d5e79
coverage: 0.545455
learned_at: 2026-10-06 21:50:16
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, SamplerCustomAdvanced, SaveImageAdvanced, TextEncodeQwenImage21, QwenImage21FunPDDLoader, BasicGuider, RandomNoise]
patterns: []
missing: [BasicGuider, QwenImage21FunPDDLoader, RandomNoise, SamplerCustomAdvanced, SaveImageAdvanced]
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
discoveries: [次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识, 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识, 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1-文生图_2106946374871904257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `QwenImage21FunPDDLoader`
- `BasicGuider`
- `RandomNoise`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（6/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`TextEncodeQwenImage21`

**缺卡**（5）：`BasicGuider`、`QwenImage21FunPDDLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`SaveImageAdvanced`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识
- 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
